#!/bin/bash

echo "What would you like to do?"
echo "1. Set up script to run on computer startup (recommended)"
echo "2. Install dependencies; Don't set up autorun"
echo "3. Disable/Uninstall autoscreener"

read choice

if [ $choice == "1" ]
then
  clear
  screenerDirectory=~/.local/share/screener
  echo "Installing..."

  pip install -q -r requirements.txt

  clear
  echo "Running CreateFile.py..."
  python3 CreateFile.py
  clear

  rm -r $screenerDirectory
  mkdir $screenerDirectory
  cp AutoScreener.py $screenerDirectory || clear && echo "Installation failed: Autoscreener.py missing" && exit
  cp notification.py $screenerDirectory || clear && echo "Installation failed: notification.py missing" && exit
  cp updater.sh $screenerDirectory || clear && echo "Installation failed: updater.sh missing" && exit
  cp screener.desktop ~/.config/autostart/ || clear && echo "Installation failed: screener.desktop missing" && exit
  cp screenerData.csv $screenerDirectory || clear && echo "Installation failed: screenerData.csv file missing" && exit

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

  pip uninstall -q -y -r requirements.txt
  rm ~/.config/autostart/screener.desktop
  rm -r ~/.local/share/screener
  clear

  echo "Uninstall successful"

else
  echo "Invalid Choice"
  exit
fi
