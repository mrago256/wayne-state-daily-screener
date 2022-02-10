#!/bin/sh

echo Updating...

version=`google-chrome --version | cut -d ' ' -f3`

wget -N -q https://chromedriver.storage.googleapis.com/$version/chromedriver_linux64.zip

unzip -o -q *.zip

rm *.zip

echo ChromeDriver version successfully matched with chrome version: $version
