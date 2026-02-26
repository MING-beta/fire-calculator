@echo off
chcp 65001 >nul
cd /d "C:\Users\user\Desktop\dopaming\fire-calculator"

:loop
echo 작업 내역을 GitHub에 자동 업로드 합니다...
git add .
git commit -m "자동 저장 커밋"
git push origin main

echo 완료! 10분 뒤에 다시 실행됩니다.
timeout /t 600 /nobreak
goto loop
