#!/bin/sh

version=`google-chrome --version | cut -d ' ' -f3`
echo $version

wget -N https://chromedriver.storage.googleapis.com/$version/chromedriver_linux64.zip

unzip -o *.zip

rm *.zip

echo ChromeDriver version successfully matched with chrome version: $version
