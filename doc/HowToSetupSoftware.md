# How To Setup Software

TatamiRacer can use Donkey Car software.
This article is installation of Donkey car software and custaiization for TatamiRacer.

# Install Raspberry Pi OS using Raspberry Pi Imager
1. Download Raspberry pi Imager from Raspberry Pi official site.
2. Install Raspberry Pi Imager.
3. Lunch Raspberry Pi imager
4. Choose "Raspberry Pi OS(32BIT)
<img src="../img/RaspberryPiImager.jpg" alt="" title="" width="640" height="">  
5. Write Raspbian OS to your micro SD card. 
6. Un plugging and re-inserting micro SD card.
7. Check the SD card drive. Boot files are appeared if OS image was flashed successfuly.

# Setup the WiFi for Raspberry Pi
Internet connection on Raspberry Pi is required before setup of donkeycar.
## - Method 1: WiFi setting in the Raspberry Pi Desktop (monitor and keyboard for Raspberry pi are required)
1. Insert micro SD card into Raspi.
2. Plug USB power supply of Raspi.
3.  Set Wifi configuration from Raspberry pi Desktop 
 Please see [Wireless connectivity in the Raspberry Pi Desktop](https://bwww.raspberrypi.org/documentation/configuration/wireless/desktop.md)
## - Method 2: WiFi setting by boot configuration file (Remote access is available without Raspi monitor and keyboard) 
1. Create wpa_supplicant.conf in the top of SD card then edit ssid and password by texteditor
 Please see [Setting up a Raspberry Pi headless](https://docs.donkeycar.com/guide/robot_sbc/setup_raspberry_pi/)
2. Create ssh file (empty file) in the top of SD card to enable SSH.
 Please see[SSH (Secure Shell)>3. Enable SSH on a headless Raspberry Pi](https://www.raspberrypi.org/documentation/remote-access/ssh/)
3. Insert micro SD card into Raspi.
4. Plug USB power supply of Raspi and wait about 1 minutes.
5. Launch command prompt and enter following command.Check network connection between host pc and raspberry pi.
 ~~~
 ping raspberrypi.local
~~~
6. Launch ssh with following command and press enter.
~~~
ssh pi@raspberrypi
~~~
7. Enter password. (Initial password:raspberry)

# Setup VNC
Remote desktop environment is useful to access raspberry pi from host pc. 
Please see [VNC (Virtual Network Computing)](https://www.raspberrypi.org/documentation/remote-access/vnc/)

# Install Donkey Software
~~~
wget "https://raw.githubusercontent.com/covao/TatamiRacer/master/raspi/install/install_donkey_raspi.sh" -O "install_donkey_raspi.sh"
sh install_donkey_raspi.sh
~~~
If you install manually, please see[Get Your Raspberry Pi Working Step6-](https://docs.donkeycar.com/guide/robot_sbc/setup_raspberry_pi/#step-6-update-and-upgrade)

# Setup TatamiRacer
~~~
wget "https://raw.githubusercontent.com/covao/TatamiRacer/master/raspi/install/setup_tatamiracer.sh" -O "setup_tatamiracer.sh"
sh setup_tatamiracer.sh
~~~
