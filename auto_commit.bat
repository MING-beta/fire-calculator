@echo off
chcp 65001 >nul
cd /d "C:\Users\user\Desktop\dopaming\fire-calculator"

echo 작업 내역을 GitHub에 업로드 합니다...
git add .

if "%~1"=="" (
    git commit -m "chore: 작업 내역 커밋 (Antigravity IDE)"
) else (
    git commit -m "%~1"
)

git push origin main
echo 완료!
