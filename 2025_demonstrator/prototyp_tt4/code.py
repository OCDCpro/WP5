# SPDX-FileCopyrightText: 2025 Fabio Ramirez Stern
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Put this on the RPi Pico controlling the RFID chip, NOT the RP2040 on the TT04 dev board!

# This script continuously reads an NFC card and sends the door code saved on it to the TT04 board.

# IMPORTS
import board
import busio
import digitalio
from time import sleep

from adafruit_pn532.spi import PN532_SPI

# SPI-Interface & PN532 SETUP
spi = busio.SPI(board.GP2, board.GP3, board.GP4) # SPI0 inteface standard pins
cs_pin = digitalio.DigitalInOut(board.GP5)
pn532 = PN532_SPI(spi, cs_pin, debug=False)
ic, ver, rev, support = pn532.firmware_version
print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))
pn532.SAM_configuration()


# LED SETUP
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Digital Out to TT04 board
dout0 = digitalio.DigitalInOut(board.GP6)
dout0.direction = digitalio.Direction.OUTPUT
dout1 = digitalio.DigitalInOut(board.GP7)
dout1.direction = digitalio.Direction.OUTPUT
dout2 = digitalio.DigitalInOut(board.GP8)
dout2.direction = digitalio.Direction.OUTPUT
dout3 = digitalio.DigitalInOut(board.GP9)
dout3.direction = digitalio.Direction.OUTPUT
dout4 = digitalio.DigitalInOut(board.GP10)
dout4.direction = digitalio.Direction.OUTPUT
dout5 = digitalio.DigitalInOut(board.GP11)
dout5.direction = digitalio.Direction.OUTPUT
dout6 = digitalio.DigitalInOut(board.GP12)
dout6.direction = digitalio.Direction.OUTPUT
dout7 = digitalio.DigitalInOut(board.GP13)
dout7.direction = digitalio.Direction.OUTPUT

# TT04 BOARD SETUP
"""
TT04 project 17 : Digital Cipher & Interlock System
MUX: 10110101
"""


print("Present a card open the door")
while True:
    uid = pn532.read_passive_target(timeout=0.5)
    if uid is None: # Try again if no card is available.
        led.value = False # turn everything off
        dout0.value = False
        dout1.value = False
        dout2.value = False
        dout3.value = False
        dout4.value = False
        dout5.value = False
        dout6.value = False
        dout7.value = False
        continue
    if uid is not None:
        print("Card detected")
        #print("Card UID: ", uid.hex())
        
        print("Reading card...")
        blockRead = pn532.mifare_classic_read_block(4) # reads from block 4, which is where the door code is saved
        if blockRead is None:
            print("Card read failed") # defective chip, card moved, or not formatted
        else:
            #print("Card read successfully")
            led.value = True
            entered_key = blockRead[1]
            print(bin(entered_key))
            
            # transmit the key to the TT04 board
            dout0.value = bool(entered_key & 0b10000000)
            dout1.value = bool(entered_key & 0b01000000)
            dout2.value = bool(entered_key & 0b00100000)
            dout3.value = bool(entered_key & 0b00010000)
            dout4.value = bool(entered_key & 0b00001000)
            dout5.value = bool(entered_key & 0b00000100)
            dout6.value = bool(entered_key & 0b00000010)
            dout7.value = bool(entered_key & 0b00000001)
            sleep(0.5) # time for the user to open the door
