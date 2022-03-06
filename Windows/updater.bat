@echo off

echo Installing...

for /F "tokens=* USEBACKQ" %%F IN (`reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version`) DO (
set string=%%F
)

set version=%string:*Z    =%

curl -LO -s https://chromedriver.storage.googleapis.com/%version%/chromedriver_win32.zip

tar -xf chromedriver_win32.zip

del chromedriver_win32.zip

echo Chromedriver version successfully matched with Chrome version: %version%
