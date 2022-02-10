#!/bin/sh

version=`google-chrome --version | cut -d ' ' -f3`
echo $version

wget https://chromedriver.storage.googleapis.com/$version/chromedriver_linux64.zip
