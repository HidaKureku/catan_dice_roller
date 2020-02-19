import os
import RPi.GPIO as GPIO
import time

num = [GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.HIGH]

decoder = {[40,38,37,36],[35,33,32,31],[29,22,18,16],[15,13,12,11]}

for x in range(0,4):
    for y in range(0,4):
        GPIO.setup(decoder[x][y],GPIO.OUT)

for loop in range(0,3):
    for x in range(0,4):
        for y in range(0,4):
            GPIO.output(decoder[x][y],num[y])
    time.sleep(1)

os.system("sudo python3 /home/pi/catan_dice_roller/catan_dice_roller.py")
