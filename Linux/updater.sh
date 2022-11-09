#!/bin/sh

echo "Updating..."

version=`curl https://chromedriver.storage.googleapis.com/LATEST_RELEASE`

wget -N -q https://chromedriver.storage.googleapis.com/$version/chromedriver_linux64.zip &&

unzip -o -q *.zip &&

rm *.zip &&

echo "Chromedriver version successfully matched with Chrome version: $version" &&

exit

echo "Chromedriver failed to install"
