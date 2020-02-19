#Catan Dice Roller Installation

import os

#Create roll_logs folder
os.system("sudo mkdir /home/pi/catan_dice_roller/roll_logs")

#Replace rc.local
os.system("sudo rm -r /etc/rc.local")
os.system("sudo cp /home/pi/catan_dice_roller/install/rc.local /etc")
os.system("sudo chmod +x /etc/rc.local")
os.system("sudo chmod +x /home/pi/catan_dice_roller/catan_dice_roller.py")
os.system("sudo chmod +x /home/pi/catan_dice_roller/startup.py")

#Install Libraries
os.system("sudo apt-get update -y")
os.system("sudo apt-get upgrade -y")
os.system("sudo apt-get install python-dev -y")
os.system("sudo apt-get install python3-dev -y")
os.system("sudo apt-get install RPi.GPIO -y")
os.system("sudo apt-get install usbmount -y")

#Reboot
os.system("sudo reboot")
