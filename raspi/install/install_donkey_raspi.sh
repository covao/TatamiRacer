#!/bin/sh -x
#Install donkeycar

printf "Install donkeycar automatically\n"
printf " Please see https://docs.donkeycar.com/guide/robot_sbc/setup_raspberry_pi/\n"

#Raspi-config
sudo raspi-config nonint do_vnc 0
sudo raspi-config nonint do_onewire 0
sudo raspi-config nonint do_camera 0

#Update and Upgrade
yes | sudo apt-get update
yes | sudo apt-get upgrade

#Install Dependencies
yes | sudo apt-get install build-essential python3 python3-dev python3-pip python3-virtualenv python3-numpy python3-picamera python3-pandas python3-rpi.gpio i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran libatlas-base-dev libopenblas-dev libhdf5-serial-dev git ntp

#Optional - Install OpenCV Dependencies
yes | sudo apt-get install libilmbase-dev libopenexr-dev libgstreamer1.0-dev libjasper-dev libwebp-dev libatlas-base-dev libavcodec-dev libavformat-dev libswscale-dev libqtgui4 libqt4-test

#Setup Virtual Env
python3 -m virtualenv -p python3 env --system-site-packages
echo "source env/bin/activate" >> ~/.bashrc
source ~/.bashrc

#Install Donkeycar Python Code
mkdir projects
cd projects
git clone https://github.com/autorope/donkeycar
cd donkeycar
git checkout master
yes | pip install -e .[pi]
yes | pip install numpy --upgrade

curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=1DCfoSwlsdX9X4E3pLClE1z0fvw8tFESP" > /dev/null
CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=1DCfoSwlsdX9X4E3pLClE1z0fvw8tFESP" -o tensorflow-2.2.0-cp37-cp37m-linux_armv7l.whl
yes | pip install tensorflow-2.2.0-cp37-cp37m-linux_armv7l.whl

#Optional - Install OpenCV
yes | sudo apt install python3-opencv

#Create Donkeycar from Template
donkey createcar --path ~/mycar

