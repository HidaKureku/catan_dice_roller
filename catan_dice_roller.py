#Catan Dice Roller v1
#Mar 15, 2020

import RPi.GPIO as GPIO
import time
from random import randrange
import os
import shutil
from decimal import *
import pyudev

#Global Variables
roll_count = [0]
d1_rolls = [0]
d2_rolls = [0]
total_rolls = [0]
roll_logs = [0]

#Maps
decoder1 = [16,8,10,12]
decoder2 = [36,18,24,32]
decoder3 = [19,29,23,21]
decoder4 = [31,37,35,33]
blank = [GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.HIGH]
num = {0: [GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW],
       1: [GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.LOW],
       2: [GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.LOW],
       3: [GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW],
       4: [GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.LOW],
       5: [GPIO.HIGH,GPIO.LOW,GPIO.HIGH,GPIO.LOW],
       6: [GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW],
       7: [GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.LOW],
       8: [GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.HIGH],
       9: [GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH]}

#Save Button Function
def save_button(channel):
    #Blank Displays
    for x in range(0,4):
        GPIO.output(decoder1[x],blank[x])
        GPIO.output(decoder2[x],blank[x])
        GPIO.output(decoder3[x],blank[x])
        GPIO.output(decoder4[x],blank[x])
    time.sleep(1)
    #Display all 8s to denote roll log save
    for x in range(0,4):
        GPIO.output(decoder1[x],num[8][x])
        GPIO.output(decoder2[x],num[8][x])
        GPIO.output(decoder3[x],num[8][x])
        GPIO.output(decoder4[x],num[8][x])
    #Save Roll Log
    logs = str(roll_logs.count(1))
    log = open(r"/home/pi/catan_dice_roller/roll_logs/roll_log" + logs + ".txt","w+")
    count = roll_count.count(1) + 1
    for x in range(1,count):
        d1 = d1_rolls[x]
        d2 = d1_rolls[x]
        tot = total_rolls[x]
        line = ("\nRoll " + str(x) + "   Dice 1: " + str(d1) + "   Dice 2: " + str(d2) + "   Total Roll: " + str(tot))
        log.writelines(line)
    #Add Game Summary
    #Dice 1 Roll Totals
    line = ("\n\nDice 1 Roll Summary")
    log.writelines(line)
    for x in range(1,7):
        number = d1_rolls.count(x)
        getcontext().prec = 4
        dec = (Decimal(number)/Decimal(count))*100
        line = ("\n" + str(x) + ": " + str(number) + "   " + str(dec) + "%")
        log.writelines(line)
    #Dice 2 Roll Totals
    line = ("\n\nDice 2 Roll Summary")
    log.writelines(line)
    for x in range(1,7):
        number = d2_rolls.count(x)
        getcontext().prec = 4
        dec = (Decimal(number)/Decimal(count))*100
        line = ("\n" + str(x) + ": " + str(number) + "   " + str(dec) + "%")
        log.writelines(line)
    #Total Roll Totals
    line = ("\n\nTotal Roll Summary")
    log.writelines(line)
    for x in range(2,13):
        number = total_rolls.count(x)
        getcontext().prec = 4
        dec = (Decimal(number)/Decimal(count))*100
        line = ("\n" + str(x) + ": " + str(number) + "   " + str(dec) + "%")
        log.writelines(line)
    log.close()
    roll_count.clear()
    roll_count.append(0)
    d1_rolls.clear()
    d1_rolls.append(0)
    d2_rolls.clear()
    d2_rolls.append(0)
    total_rolls.clear()
    total_rolls.append(0)
    roll_logs.append(1)
    time.sleep(3)
    #Blank Displays
    for x in range(0,4):
        GPIO.output(decoder1[x],blank[x])
        GPIO.output(decoder2[x],blank[x])
        GPIO.output(decoder3[x],blank[x])
        GPIO.output(decoder4[x],blank[x])
    time.sleep(1)

#Reset Button Function
def reset_button(channel):
    #Blank Displays
    for x in range(0,4):
        GPIO.output(decoder1[x],blank[x])
        GPIO.output(decoder2[x],blank[x])
        GPIO.output(decoder3[x],blank[x])
        GPIO.output(decoder4[x],blank[x])
    time.sleep(1)
    #Display all 0s to denote roll log reset
    for x in range(0,4):
        GPIO.output(decoder1[x],num[0][x])
        GPIO.output(decoder2[x],num[0][x])
        GPIO.output(decoder3[x],num[0][x])
        GPIO.output(decoder4[x],num[0][x])
    #Mount USB Drive
    os.system("sudo mount /dev/sda1 /media/usb")
    #Copy Roll Log folder to USB
    os.system("sudo cp /home/pi/catan_dice_roller/roll_logs /media/usb")
    #Reset Roll Logs
    shutil.rmtree(r"/home/pi/catan_dice_roller/roll_logs")
    os.mkdir(r"/home/pi/catan_dice_roller/roll_logs")
    roll_logs.clear()
    roll_logs.append(1)
    time.sleep(3)
    #Blank Displays
    for x in range(0,4):
        GPIO.output(decoder1[x],blank[x])
        GPIO.output(decoder2[x],blank[x])
        GPIO.output(decoder3[x],blank[x])
        GPIO.output(decoder4[x],blank[x])
    time.sleep(1)

#Roll Button Function
def roll_button(channel):
    dice1 = randrange(1,7)
    dice2 = randrange(1,7)
    total = dice1 + dice2
    roll_count.append(1)
    roll = roll_count.count(1)
    d1_rolls.append(dice1)
    d2_rolls.append(dice2)
    total_rolls.append(total)
    #Blank Displays
    for x in range(0,4):
        GPIO.output(decoder1[x],blank[x])
        GPIO.output(decoder2[x],blank[x])
        GPIO.output(decoder3[x],blank[x])
        GPIO.output(decoder4[x],blank[x])
    time.sleep(1)
    #Output Rolls
    if total < 10:
        for x in range(0,4):
            GPIO.output(decoder3[x],blank[x])
            GPIO.output(decoder1[x],num[dice1][x])
            GPIO.output(decoder2[x],num[dice2][x])
            GPIO.output(decoder4[x],num[total][x])
    else:
        dig1 = int(total / 10)
        dig2 = int(total % 10)
        for x in range(0,4):
            GPIO.output(decoder1[x],num[dice1][x])
            GPIO.output(decoder2[x],num[dice2][x])
            GPIO.output(decoder3[x],num[dig1][x])
            GPIO.output(decoder4[x],num[dig2][x])
    time.sleep(3)

#Turn Button Function
def turn_button(channel):
    turn_dice = randrange(1,7)
    #Blank Displays
    for x in range(0,4):
        GPIO.output(decoder1[x],blank[x])
        GPIO.output(decoder2[x],blank[x])
        GPIO.output(decoder3[x],blank[x])
        GPIO.output(decoder4[x],blank[x])
    time.sleep(1)
    #Output Turn Roll
    for x in range(0,4):
        GPIO.output(decoder4[x],num[turn_dice][x])
    time.sleep(3)

#Sleep Button Function
def sleep(channel):
    GPIO.output(38,GPIO.HIGH)
    for x in range(0,4):
        GPIO.output(decoder1[x],num[8][x])
        GPIO.output(decoder2[x],num[8][x])
        GPIO.output(decoder3[x],num[8][x])
        GPIO.output(decoder4[x],num[8][x])
    time.sleep(5)
    GPIO.output(38,GPIO.LOW)
    os.system("sudo shutdown -h now")

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(38,GPIO.OUT) #Blanking
GPIO.output(38,GPIO.HIGH)

#Set up decoders
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
time.sleep(3)  

#Set up Buttons
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #save
GPIO.setup(11,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #reset
GPIO.setup(15,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #roll
GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #turn
GPIO.setup(40,GPIO.IN,pull_up_down=GPIO.PUD_UP) #sleep

#Butten Event Detection
GPIO.add_event_detect(8,GPIO.RISING,callback=save_button)
GPIO.add_event_detect(10,GPIO.RISING,callback=reset_button)
GPIO.add_event_detect(19,GPIO.RISING,callback=roll_button)
GPIO.add_event_detect(21,GPIO.RISING,callback=turn_button)
GPIO.add_event_detect(5,GPIO.FALLING,callback=sleep)

while True:
    time.sleep(1)
    
GPIO.cleanup()
