import os
import subprocess
import datetime
from google import genai
from google.genai import types

def get_git_diff():
    """가장 최근 커밋의 변경 사항(diff)을 가져옵니다."""
    try:
        # README, VERSION과 .github 하위 파일들을 제외한 변경 사항만 추출합니다.
        result = subprocess.run(
            ['git', 'diff', 'HEAD^', 'HEAD', '--', '.', ':(exclude)README.md', ':(exclude)VERSION', ':(exclude).github/'],
            capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error getting diff: {e}")
        return ""

def bump_version():
    """VERSION 파일을 읽어 패치 버전을 1 올리고 반환합니다."""
    version_file = "VERSION"
    version = "1.0.0"
    if os.path.exists(version_file):
        with open(version_file, "r", encoding="utf-8") as f:
            version = f.read().strip()
    
    try:
        parts = version.split(".")
        if len(parts) == 3:
            parts[2] = str(int(parts[2]) + 1)
            new_version = ".".join(parts)
        else:
            new_version = version + ".1"
    except Exception:
        new_version = "1.0.1"
        
    with open(version_file, "w", encoding="utf-8") as f:
        f.write(new_version)
    
    return new_version

def generate_content_with_gemini(diff_text, version):
    """Gemini API를 호출하여 커밋 메시지와 마크다운 요약을 생성합니다."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY is not set.")
        return None, None
        
    client = genai.Client(api_key=api_key)
    
    prompt = f"""
현재 프로젝트의 새 버전은 v{version} 입니다.
다음은 코드 변경 사항(git diff)입니다:

{diff_text}

이 변경 사항을 바탕으로 다음 두 가지를 만들어주세요:
1. 해당 변경건을 요약하는 짧은 한 줄짜리 커밋 메시지 (예: "[DOPAMING] v{version}: 로그인 버튼 UI 색상 변경 및 컴포넌트 최적화")
   - 주의: 항상 제일 앞에 '[DOPAMING] v{version}: '을 붙이세요.
2. README.md 파일의 '업데이트 기록'에 추가할 마크다운 형식의 상세 요약 (글머리기호 사용, 한국어로 작성)

응답은 반드시 아래와 같이 두 파트로 나누어서 작성해야 하며, 구분자 '---' 를 사용하세요.

[응답 형식 예시]
[DOPAMING] v{version}: 커밋 메시지 한 줄 요약
---
* 수정사항 1: ~~~
* 수정사항 2: ~~~
"""
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash', # Or another model if needed
            contents=prompt,
        )
        
        response_text = response.text
        if "---" in response_text:
            parts = response_text.split("---", 1)
            commit_msg = parts[0].strip()
            readme_update = parts[1].strip()
            return commit_msg, readme_update
        else:
            return f"[DOPAMING] v{version}: 코드 수정 및 업데이트", response_text.strip()
            
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return None, None

def update_readme(update_text, version):
    """README.md 파일의 특정 마커 사이에 요약 내용을 추가합니다."""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    new_entry = f"### v{version} ({today}) 업데이트\n{update_text}\n\n"
    
    readme_path = "README.md"
    marker = "<!-- UPDATE_LOG_START -->"
    
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if marker in content:
            parts = content.split(marker)
            new_content = parts[0] + marker + "\n\n" + new_entry + parts[1].lstrip('\n')
        else:
            new_content = content + f"\n\n## 업데이트 내역\n{marker}\n\n{new_entry}"
            
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)

def main():
    diff_text = get_git_diff()
    if not diff_text or len(diff_text.strip()) == 0:
        print("No meaningful code changes found.")
        return
        
    print("Bumping version...")
    new_version = bump_version()
    
    print(f"Generating AI content for v{new_version}...")
    commit_msg, readme_update = generate_content_with_gemini(diff_text, new_version)
    
    if commit_msg and readme_update:
        print(f"Generated Commit Msg: {commit_msg}")
        update_readme(readme_update, new_version)
        
        # 커밋 메시지 파일 저장
        with open(".github/scripts/commit_msg.txt", "w", encoding="utf-8") as f:
            f.write(f"{commit_msg.strip()}\n\n{readme_update.strip()}")
    else:
        print("Failed to generate content.")

if __name__ == "__main__":
    main()
