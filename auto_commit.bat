@echo off
chcp 65001 >nul
cd /d "C:\Users\user\Desktop\dopaming\fire-calculator"

echo 작업 내역을 GitHub에 업로드 합니다...
git add .

if "%~1"=="" (
    git commit -m "chore: 작업 내역 임시 커밋 (GitHub Action에서 AI 요약 진행)"
) else (
    git commit -m "%~1"
)

echo 최신 작업 내역(AI 요약 포함)을 가져옵니다...
git pull --rebase origin main

echo GitHub에 푸시합니다...
git push origin main
echo 완료!
