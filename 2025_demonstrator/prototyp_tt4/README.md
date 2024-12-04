# 2025 Demonstrator Prototyp mit existierenden Design von TT04

## Overview

Um das Prinzip zu testen/anschaulich darzustellen wird ein RFID-Modul mit einem bereits bestehenden Schloss-Design von Tiny Tapeout 4 verbunden. Ein RPi Pico fungiert als Bridge zwischen dem RFID-Modul (SPI) und dem TT04 Board (Parallel/Seriell). Dazu wird im CircuitPython ein Übersetzer-Programm geschrieben.

### Hardware-Chip

Es wird das Projekt "Digital Cipher & Interlock System" mit __Index 17__ aus Tiny Tapeout Run 4 (TT4) benutzt.
Dieses legt eine feste Kombination von 8 bit fest, die parallel übergeben werden. Das Projekt arbeitet ausschließlich kombinatorisch und benötigt keine Clock oder Reset.
Wenn die Kombination vollständig übereinstimmt, werden alle Outputs HIGH. Partielle Übereinstimmung sorgt für partielle HIGHs an den 8 Ausgängen.
Pin 0 (oberstes waagerechtes Segment in der 7-Segmentanzeige) wird nur HIGH, wenn die Kombination stimmt.

### Raspberry Pi

Ein Rapsberry Pi (RPi) Pico (RP2040) steuert das RFID-Modul via SPI an, und gibt in einem regelmäßigen Takt eine Signatur oder einen Trunk der gelesenen Daten an den Hardware-Chip weiter.
Er überwacht die Outputs des Hardware-Chips und gibt ein Erfolgssignal (TBD) aus.

### RFID-Modul

Ein Elechouse "NFC Module V3", basierend auf einem PN532-Chip wird über SPI vom RPi angesprochen.

### RFID-Chip

Ein RFID/NFC-Tag.
