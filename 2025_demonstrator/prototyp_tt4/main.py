# SPDX-FileCopyrightText: 2025 Fabio Ramirez Stern
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Put this on the RP2040 on the TT04 dev board, not the RPi Pico controlling the RFID chip!

# IMPORTS
import micropython
from ttboard.boot.demoboard_detect import DemoboardDetect
from ttboard.demoboard import DemoBoard
import ttboard.util.colors as colors

# Initialize the demo board
tt = DemoBoard()

# Initialize the project
tt.shuttle.wokwi_digital_cipher_interlock_system_52.enable()
