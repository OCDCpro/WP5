# SPDX-FileCopyrightText: 2025 Fabio Ramirez Stern
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Put this on the RPi Pico controlling the RFID chip, not the RP2040 on the TT04 dev board!

# IMPORTS
import board
import busio
import digitalio

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
10110101
"""


print("Present a card to write to the NFC board")
while True:
    uid = pn532.read_passive_target(timeout=0.5)
    # Try again if no card is available.
    if uid is None:
        led.value = False
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
        print("Card UID: ", uid.hex())
        led.value = True
        
        print("Reading card...")
        blockRead = pn532.mifare_classic_get_value_block(4)
        if blockRead is None:
            print("Card read failed")
        else:
            print("Card read successfully")

            dout0.value = bool(blockRead[0] & 0b00000001)
            dout1.value = bool(blockRead[0] & 0b00000010)
            dout2.value = bool(blockRead[0] & 0b00000100)
            dout3.value = bool(blockRead[0] & 0b00001000)
            dout4.value = bool(blockRead[0] & 0b00010000)
            dout5.value = bool(blockRead[0] & 0b00100000)
            dout6.value = bool(blockRead[0] & 0b01000000)
            dout7.value = bool(blockRead[0] & 0b10000000)

            
            




