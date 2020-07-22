# GcodeSender
A python program that sends gcode files to a 3d printer

To use run the python3 file giving the 3D printer baudrate and file as arguememts.
The 3D printer address is usually found in the /dev folder. /dev/cu.usbserial... works best for me.

`python3 gcode_sender.py [printer] [baudrate] [gcode file]`

I also included mousetrack.py which is a pygame window which allows the user to control the 3D Printer position with their mouse. Tracking to a new point only occurs onces the printer reaches the previous point (estimated)
Run using `python3 mousetrack.py [printer] [baudrate]`
