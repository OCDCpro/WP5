# Specification of the 2025 Hardware Kit

## Requirements

* Power measurement points
  * Shunt resistor along vdd (or gnd) line
  * SMA connector for easy access
* RFID reader compatible with common Mifare standards
    * Mifare Ultralight + DESFire?
    * based on [NXP MFRC522](https://www.nxp.com/docs/en/data-sheet/MFRC522.pdf) or similar

## Other Ideas

* Integrated low-cost USB oscilloscope for measuring power consumption of the chip without additional equipment
  * For reference: See [ChipWhisperer Nano](https://rtfm.newae.com/Capture/ChipWhisperer-Nano/)
  * Cortex-M4 based microcontroller + 8bit TI ADC1173 or similar