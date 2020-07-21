# GcodeSender
A python program that sends gcode files to a 3d printer

To use run the python3 file giving the 3D printer baudrate and file as arguememts.
The 3D printer address is usually found in the /dev folder. /dev/cu.usbserial... works best for me.

`python3 gcode_sender.py [3D Printer] [Baudrate] [Gcode File]`
