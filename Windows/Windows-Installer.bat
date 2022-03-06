@echo off

where pip >nul 2>&1 && (
    @REM echo Python Installed
) || (
    echo Error: Python either not installed or not installed correctly.
    echo Please refer to the readme for further information.
    pause
    exit
)

echo What would you like to do?
echo 1. Set up script to run on computer startup (recommended)
echo 2. Install dependencies; Don't set up autorun
echo 3. Disable/Uninstall autoscreener

set /p choice= ""

if %choice%==1 (
  cls
  echo Installing...

  pip install -q --upgrade pip
  pip install -q -r requirements.txt
  cls

  echo Running CreateFile.py
  python CreateFile.py

  xcopy "screener-startup.bat" "%userprofile%\AppData\Local\Autoscreener\" /Y >nul
  xcopy "AutoScreener.py" "%userprofile%\AppData\Local\Autoscreener\" /Y >nul
  xcopy "updater.bat" "%userprofile%\AppData\Local\Autoscreener\" /Y >nul
  xcopy "notification.py" "%userprofile%\AppData\Local\Autoscreener\" /Y >nul
  xcopy "screenerData.csv" "%userprofile%\AppData\Local\Autoscreener\" /Y >nul
  xcopy "Autorun.vbs" "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /Y >nul

  cls
  echo Screener successfully set up and installed
  pause
  exit
)

if %choice%==2 (
  cls
  echo Installing...

  pip install -q -r requirements.txt
  cls

  echo Installation successful
  echo Running CreateFily.py...

  python CreateFile.py
  pause
  exit

)

if %choice%==3 (
  cls
  echo Uninstalling...

  pip uninstall -q -y -r requirements.txt
  rmdir /s %userprofile%\AppData\Local\Autoscreener /Q >nul
  del "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Autorun.vbs" /Q 2>nul
  cls

  echo Uninstall successful
  pause
  exit
)

cls
echo Invalid Choice
pause
