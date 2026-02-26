@echo off
:loop
:: 10분(600초)마다 한 번씩 변경된 내용이 있는지 확인하고 업로드합니다.
echo 작업 내역을 GitHub에 자동 업로드 합니다...
git add .
git commit -m "자동 저장 커밋"
git push origin main

echo 완료! 10분 뒤에 다시 실행됩니다.
timeout /t 600
goto loop
