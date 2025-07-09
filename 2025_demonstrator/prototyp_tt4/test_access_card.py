# SPDX-FileCopyrightText: 2025 Fabio Ramirez Stern
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Put this on the RPi Pico controlling the RFID chip, not the RP2040 on the TT04 dev board!

# TT04 BOARD SETUP
"""
TT04 project 17 : Digital Cipher & Interlock System
"""

secret = 0b10110101

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

# Check the block of data to the card

print("Present a card to write to the NFC board")
while True:
    uid = pn532.read_passive_target(timeout=0.5)
    # Try again if no card is available.
    if uid is None:
        led.value = False
        continue
    if uid is not None:
        print("Card detected")
        print("Card UID: ", uid.hex())
        led.value = True
        break


print("Reading card...")
blockRead = pn532.mifare_classic_get_value_block(4)
if blockRead is None:
    print("Card read failed")
else:
    print("Card read successfully")
    print("Data in block 4: ", blockRead)
    print("target: ", hex(secret))
