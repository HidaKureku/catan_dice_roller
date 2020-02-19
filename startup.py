import os
import RPi.GPIO as GPIO
import time

num = [GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.HIGH]

for x in range(0,4):
    GPIO.setup(decoder1[x],GPIO.OUT)
    GPIO.output(decoder1[x],GPIO.LOW)
    GPIO.setup(decoder2[x],GPIO.OUT)
    GPIO.output(decoder2[x],GPIO.LOW)
    GPIO.setup(decoder3[x],GPIO.OUT)
    GPIO.output(decoder3[x],GPIO.LOW)
    GPIO.setup(decoder4[x],GPIO.OUT)
    GPIO.output(decoder4[x],GPIO.LOW)

#Blank Displays
for x in range(0,4):
    GPIO.output(decoder1[x],blank[x])
    GPIO.output(decoder2[x],blank[x])
    GPIO.output(decoder3[x],blank[x])
    GPIO.output(decoder4[x],blank[x])

#Display all 8s
for x in range(0,4):
    GPIO.output(decoder1[x],num[8][x])
    GPIO.output(decoder2[x],num[8][x])
    GPIO.output(decoder3[x],num[8][x])
    GPIO.output(decoder4[x],num[8][x])
time.sleep(1)

#Display all 0s
for x in range(0,4):
    GPIO.output(decoder1[x],num[0][x])
    GPIO.output(decoder2[x],num[0][x])
    GPIO.output(decoder3[x],num[0][x])
    GPIO.output(decoder4[x],num[0][x])
time.sleep(1)

#Display all 8s
for x in range(0,4):
    GPIO.output(decoder1[x],num[8][x])
    GPIO.output(decoder2[x],num[8][x])
    GPIO.output(decoder3[x],num[8][x])
    GPIO.output(decoder4[x],num[8][x])
time.sleep(1)

os.system("sudo python3 /home/pi/catan_dice_roller/catan_dice_roller.py")
GPIO.cleanup()
