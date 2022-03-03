#!/bin/bash

if [[ $OS.TYPE == "win32" ]]
then
  echo "This is the wrong script. Run Windows-Installer instead"
  exit
fi

echo "What whould you like to do?
1. Set up script to run on computer startup (recommended)
2. Install dependencies; Don't set up autorun
3. Disable/Uninstall autorun"

read choice

if [ $choice == "1" ]
then
  screenerDirectory=~/.local/share/screener
  clear

  echo "Installing..."
  pip install -q -r requirements.txt

  rm -r ~/.local/share/screener
  (mkdir $screenerDirectory && cp AutoScreener.py $screenerDirectory \
  && cp updater.sh $screenerDirectory && cp notification.py $screenerDirectory \
  && cp screener.desktop ~/.config/autostart/) || (clear \
  && echo "Installation failed: screener.desktop file missing" && exit)

  clear
  echo "Running CreateFile.py..."
  python3 CreateFile.py

  (cp screenerData.csv $screenerDirectory) || (clear \
  && echo "Installation failed: screenerData.csv file missing" && exit)

  clear
  echo "Screener successfully set up and installed"
  exit

elif [ $choice == "2" ]
then
  clear

  echo "Installing..."
  pip install -q -r requirements.txt
  clear

  echo "Installation Successful"
  echo "Run CreateFile.py? (Y/N)"
  read choice

  if [ $choice == "y" ] || [ $choice == "Y" ]
  then
    clear
    python3 CreateFile.py
  fi

  exit

elif [ $choice == "3" ]
then
  clear

  echo "Uninstalling..."
  # pip uninstall -q -r requirements.txt
  rm ~/.config/autostart/screener.desktop
  rm -r ~/.local/share/screener
  clear

  echo "Uninstall successful. AutoScreener.py can still be run manually"
  exit

else
  echo "Invalid Choice"
  exit
fi
