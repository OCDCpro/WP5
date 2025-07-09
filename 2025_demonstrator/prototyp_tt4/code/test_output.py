# SPDX-FileCopyrightText: 2025 Fabio Ramirez Stern
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Put this on the RPi Pico controlling the RFID chip, NOT the RP2040 on the TT04 dev board!

# This script sends the correct door code to the TT04 board, which will light up all the segments of the 7 segment display.

# IMPORTS
import board
import busio
import digitalio
from time import sleep

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

# Test TT04 board setup, should light up all segments
dout0.value = True
dout1.value = False
dout2.value = True
dout3.value = True
dout4.value = False
dout5.value = True
dout6.value = False
dout7.value = True
