# SPDX-FileCopyrightText: 2025 Fabio Ramirez Stern
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Put this on the RP2040 on the TT04 dev board, NOT the RPi Pico controlling the RFID chip!

# This script runs on the TT04 board and selects the digital cipher interlock system project.

print("BOOT: Tiny Tapeout SDK")
import gc # Garbage collector
GCThreshold = gc.threshold()
gc.threshold(80000) # agressive collection threshold for boot

from ttboard.demoboard import DemoBoard
from ttboard.mode import RPMode
gc.collect()

tt = DemoBoard(RPMode.SAFE)
gc.collect()
gc.threshold(GCThreshold) # end being so aggressive on collection

tt.shuttle.wokwi_digital_cipher_interlock_system_521.enable()
