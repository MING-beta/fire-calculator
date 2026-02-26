import os
import subprocess
import datetime
from google import genai
from google.genai import types

def get_git_diff():
    """가장 최근 커밋의 변경 사항(diff)을 가져옵니다."""
    try:
        # README와 .github 하위 파일들을 제외한 변경 사항만 추출합니다.
        result = subprocess.run(
            ['git', 'diff', 'HEAD^', 'HEAD', '--', '.', ':(exclude)README.md', ':(exclude).github/'],
            capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error getting diff: {e}")
        return ""

def generate_content_with_gemini(diff_text):
    """Gemini 3.0 Pro API를 호출하여 커밋 메시지와 마크다운 요약을 생성합니다."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY is not set.")
        return None, None
        
    client = genai.Client(api_key=api_key)
    
    prompt = f"""
다음은 코드 변경 사항(git diff)입니다:

{diff_text}

이 변경 사항을 바탕으로 다음 두 가지를 만들어주세요:
1. 해당 변경건을 요약하는 짧은 한 줄짜리 커밋 메시지 (예: "로그인 버튼 UI 색상 변경 및 컴포넌트 최적화")
2. README.md 파일의 '업데이트 기록'에 추가할 마크다운 형식의 상세 요약 (글머리기호 사용, 한국어로 작성)

응답은 반드시 아래와 같이 두 파트로 나누어서 작성해야 하며, 구분자 '---' 를 사용하세요.

[응답 형식 예시]
커밋 메시지 한 줄 요약
---
* 수정사항 1: ~~~
* 수정사항 2: ~~~
"""
    try:
        response = client.models.generate_content(
            model='gemini-2.5-pro', # NOTE: As of today, the actual model id mapped to the "Pro" variant is gemini-2.5-pro
            contents=prompt,
        )
        
        response_text = response.text
        if "---" in response_text:
            parts = response_text.split("---", 1)
            commit_msg = parts[0].strip()
            readme_update = parts[1].strip()
            return commit_msg, readme_update
        else:
            return "코드 수정 및 업데이트", response_text.strip()
            
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return None, None

def update_readme(update_text):
    """README.md 파일의 특정 마커 사이에 요약 내용을 추가합니다."""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    new_entry = f"### {today} 업데이트\n{update_text}\n\n"
    
    readme_path = "README.md"
    marker = "<!-- UPDATE_LOG_START -->"
    
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if marker in content:
            # 마커 바로 아래에 새로운 내용을 추가합니다.
            parts = content.split(marker)
            new_content = parts[0] + marker + "\n\n" + new_entry + parts[1].lstrip('\n')
        else:
            # 마커가 없다면 맨 아래에 추가합니다.
            new_content = content + f"\n\n## 업데이트 내역\n{marker}\n\n{new_entry}"
            
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
    else:
        # README가 아예 없다면 새로 생성합니다.
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"# Project\n\n## 업데이트 내역\n{marker}\n\n{new_entry}")

def main():
    diff_text = get_git_diff()
    if not diff_text or len(diff_text.strip()) == 0:
        print("No meaningful code changes found.")
        return
        
    print("Generating AI content...")
    commit_msg, readme_update = generate_content_with_gemini(diff_text)
    
    if commit_msg and readme_update:
        print(f"Generated Commit Msg: {commit_msg}")
        update_readme(readme_update)
        
        # 커밋 메시지를 파일로 저장하여 GitHub Actions 배시 셸에서 읽을 수 있게 합니다.
        with open(".github/scripts/commit_msg.txt", "w", encoding="utf-8") as f:
            f.write(commit_msg.split('\n')[0]) # 혹시 여러줄이면 첫줄만
    else:
        print("Failed to generate content.")

if __name__ == "__main__":
    main()
