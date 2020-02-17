#Sleep Button

import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(7,GPIO.OUT) #Blanking
GPIO.setup(5,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.output(7,GPIO.LOW)
os.system("sudo python3 /home/pi/catan_dice_roller/catan_dice_roller.py")

#Sleep Function
def sleep(channel):
  GPIO.output(7,GPIO.LOW)
  os.system("sudo shutdown -h now")
  
  GPIO.add_event_detect(5,GPIO.FALLING,callback=sleep)
  
 while 1:
  time.sleep(1)
