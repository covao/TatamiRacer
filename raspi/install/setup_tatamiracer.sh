#!/bin/sh -x
#Setup TatamiRacer

printf "Setup TatamiRacer\n"

source env/bin/activate

#Install pigpio
yes | sudo apt install pigpio python-pigpio python3-pigpio
sudo systemctl enable pigpiod.service
sudo systemctl start pigpiod

#Install lxshortcut
#Create TatamiRacer Shortcut
yes | sudo apt-get install lxshortcut

#Download TatamiRacer files
cd ~/mycar

# Backup original file
sudo mv manage.py manage_bak.py
sudo mv manage.py mayconfig_bak.py

wget "https://raw.githubusercontent.com/covao/TatamiRacer/master/raspi/mycar/manage.py"  -O "manage.py"
wget "https://raw.githubusercontent.com/covao/TatamiRacer/master/raspi/mycar/myconfig.py"  -O "myconfig.py"
wget "https://raw.githubusercontent.com/covao/TatamiRacer/master/raspi/mycar/tatamiracer_test.py" -O "tatamiracer_test.py"
wget "https://raw.githubusercontent.com/covao/TatamiRacer/master/raspi/mycar/tatamiracer_icon.png" -O "tatamiracer_icon.png"

#Download TatamiRacer ShortCut
sudo mkdir shortcut
cd shortcut
wget "https://raw.githubusercontent.com/covao/TatamiRacer/master/raspi/mycar/shortcut/donkey_clean_data"  -O "donkey_clean_data"
wget "https://raw.githubusercontent.com/covao/TatamiRacer/master/raspi/mycar/shortcut/donkey_drive"  -O "donkey_drive"
wget "https://raw.githubusercontent.com/covao/TatamiRacer/master/raspi/mycar/shortcut/donkey_drive_with_model"  -O "donkey_drive_with_model"
wget "https://raw.githubusercontent.com/covao/TatamiRacer/master/raspi/mycar/shortcut/donkey_training_on_board"  -O "donkey_training_on_board"
wget "https://raw.githubusercontent.com/covao/TatamiRacer/master/raspi/mycar/shortcut/tatamiracer_test"  -O "tatamiracer_test"

