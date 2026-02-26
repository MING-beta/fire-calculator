@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo [DOPAMING] 로컬 변경 사항을 확인합니다...
git status -s

set /p choice="위 변경 사항을 GitHub에 커밋하고 푸시하시겠습니까? (Y/N): "
if /i not "%choice%"=="Y" (
    echo 작업을 취소했습니다.
    exit /b 0
)

set /p commit_msg="커밋 메시지를 입력하세요 (비워두면 기본 메시지 사용): "

git add .

if "%commit_msg%"=="" (
    git commit -m "[DOPAMING] 작업 내역 임시 커밋 (GitHub Action에서 AI 요약 진행)"
) else (
    git commit -m "[DOPAMING] %commit_msg%"
)

echo 최신 작업 내역(AI 요약 포함)을 가져옵니다...
git pull --rebase origin main

echo GitHub에 푸시합니다...
git push origin main
echo 완료!
pause
