#!/bin/sh -x
#Install donkeycar

printf "Install donkeycar automatically by shell-script\n"
printf "About manual installation  Please see https://docs.donkeycar.com/guide/robot_sbc/setup_raspberry_pi/\n"

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
. ~/.bashrc
. env/bin/activate

#Install Donkeycar Python Code
cd ~/
sudo rm -rf projects
mkdir ~/projects
cd ~/projects
git clone https://github.com/autorope/donkeycar
cd donkeycar
git checkout master
pip install -e .[pi]
pip install https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.2.0/tensorflow-2.2.0-cp37-none-linux_armv7l.whl

#Optional - Install OpenCV
yes | sudo apt install python3-opencv

#Create Donkeycar from Template
donkey createcar --path ~/mycar

