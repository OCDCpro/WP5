# 2025 Demonstrator Prototyp mit existierenden Design von TT04

## Overview

Um das Prinzip zu testen/anschaulich darzustellen wird ein RFID-Modul mit einem bereits bestehenden Design von Tiny Tapeout 4 verbunden. Ein RPi Pico fungiert als Bridge zwischen dem RFID-Modul und dem TT04-Board. Dazu wird im CircuitPython ein Übersetzer-Programm geschrieben. Der tatsächliche Check, ob der angebotene Schlüssel stimmt, findet im TT04-Board statt.

### Bill of Materials

- 12V Quelle (z.B. Barrel Plug + Netzteil)
- Raspberry Pi Pico
- TT04 Demoboard
- PN532 RFID Reader
- MiFare NFC-Tag
- Buck-Converter
- 12V Relais-Modul
- Kabel zum Verbinden
- Gehäuse-Material und Kleber/Leim
  
### Empfohlene/Benötigte Software

- [Thonny IDE](https://thonny.org/) für MicroPython/CircuitPython code uploads
- [TinyTapeout MicroPython Firmware](https://github.com/TinyTapeout/tt-micropython-firmware) für das Demoboard
- [Adafruit CircuitPython Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle) für dem RPi

## Anleitung Gehäuse

Die Gehäuse-Bestandteile müssen aus einem 1.5mm dicken Material geschnitten, oder zu 1.5mm dicken Material 3D-gedruckt werden. Hier wurde KRAFTPLEX ST 1.5mm verwendet, und mit einem Emblaser 2 geschnitten.

Die Wände nacheinander in den Boden einsetzen und alle Kontaktflächen untereinander vorher mit Leim bestreichen. Es wird empfohlen, die PCB-Halterungen erst in die Platinen einzuhaken und erst dann in die Wände einzusetzen und festzukleben.

## Anleitung Elektronik

### Hardware-Chip (TT04)

Es wird das Projekt ["Digital Cipher & Interlock System"](https://tinytapeout.com/chips/tt04/tt_um_wokwi_371604537887211521) mit Index 17 aus Tiny Tapeout Run 4 (TT04) benutzt.
Dieses legt eine feste Kombination von 8 bit fest, die parallel übergeben werden. Das Projekt arbeitet ausschließlich kombinatorisch und benötigt keine Clock oder Reset.
Wenn die Kombination vollständig übereinstimmt, werden alle Outputs ``HIGH``. Partielle Übereinstimmung sorgt für partielle ``HIGH``'s an den hinteren 7 Ausgängen.
Pin 0 (oberstes waagerechtes Segment in der 7-Segmentanzeige) wird nur ``HIGH``, wenn die gesamte Kombination stimmt.
Um bei Anliegen einer Stromversorgung automatisch das richtige Projekt zu laden, befindet sich auf dem Demoboard ein RP2040 Chip, wie er in RPi Picos verbaut wird. Durch Drücken der ``BOOT``-Taste, während man das Board über ein USB-C Kabel an einen Computer anschließt, geht der Chip in eine Art Bootloader-Modus und man kann die ``.UF2`` Datei der TinyTapeout Firmware hochladen, als wäre es ein USB-Stick. Nach Entfernen und Wiedereinstecken des Boards ist die Firmware geladen. Der Chip erscheint weiterhin als USB-Speicher, jedoch ist dieser read-only. Zum Ändern der Dateien muss eine Verbindung über einen COM-Port hergestellt werden. Ein einfacher Plug & Play Weg dazu ist Thonny. Nach dem Verbinden kann der Code in ``main.py`` und ``config.ini`` in zwei gleichnamige Dateien kopiert werden. Damit ist das TT04-Board fertig konfiguriert.

### Raspberry Pi Pico & RFID-Modul

Ein Rapsberry Pi (RPi) Pico steuert das RFID-Modul via SPI an, und gibt in einem regelmäßigen Takt das zweite Byte aus dem Datenblock 4 an das TT04-Board weiter.
Dazu wird der RFID-Reader wie folgt verbunden: ``SCK`` an ``GP02``, ``MOSI`` an ``GP03``, ``MISO`` an ``GP04`` und ``SS`` an ``GP05``. Außerdem muss SPI als Kommunikationsprotokoll mithilfe der zwei DIP-Switches gewählt werden, indem man ``1`` auf ``OFF`` und ``2`` auf ``ON`` stellt.
Im gebauten Demonstrator wird ein Elechouse "NFC Module V3", basierend auf einem PN532-Chip, verwendet.
Für die Software wird Adafruits CircuitPython Firmware mit allen benötigten Bibliotheken ähnlich wie beim TT04-Board mithilfe des ``BOOT``-Knopfes auf den RPi Pico geladen. Dann kann das reguläre Programm mithilfe von Thonny in ``code.py`` gespeichert werden. Um die NFC-Karten/Chips zur Nutzung als Schlüssel zu beschreiben und Diagnosetests durchzuführen, befinden sich im Ordner "setup and test code" weiter Programme, die stattdessen in ``code.py`` geladen werden können.
Der RPi Pico wird mit den Ausgängen ``GP06`` bis ``GP13`` an die Eingänge ``in0`` bis ``in7`` verbunden.

### Relais

Der Ausgang ``out0`` des TT04-Boards wird mit dem Eingang ``IN`` des Relais-Moduls verbunden.

### Stromversorgung

Da das Türschloss 12 Volt benötigt, ist es am einfachsten, den ganzen Demonstrator mit 12V zu versorgen und für die Logikverbraucher auf 3.3V herunterzuregeln. Dazu wird ein Buck-Converter benötigt, der entsprechend eingestellt wird und mit einem der ``3V3``-Pins des TT04-Boards verbunden wird. Dadurch wird das Demoboard selbst und alle an einen ``3V3``-Pin angeschlossenen Verbraucher mit Strom versorgt. Nun kann man den RPi Pico und die Logikseite des Relaismoduls jeweils an einen dieser Pins anschließen. ``VCC`` des RFID-Readers kann man entweder ebenfalls mit einen solchen Pin verbinden, oder man schließt ihn an den ``3V3(OUT)``-Pin des RPi Pico an.
Die Schaltseite des Relais und das Türschloss sind so mit der 12V-Versorgungsspannung zu verbinden, dass eine Aktivierung des Relais den Stromkreis temporär schließt (normally open). Eine mögliche Verschaltung ist ``Schematic.pdf`` entnehmbar, die Polarisierung ist hier jedoch unerheblich.

### NFC-Karte/Chip

Ein RFID/NFC-Tag mit MiFare-Unterstützung. Der Türschlüssel wird im Datenblock 4 im zweiten Byte gespeichert.

___``2025 Fabio Ramirez Stern @ Hochschule Rheinmain``___