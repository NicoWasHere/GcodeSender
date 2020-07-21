import serial
import sys
import time

#reads the gcode file
gcodeFile = open(str(sys.argv[3]),'r')
gcode = gcodeFile.readlines()

#connects to the printer
printer = serial.Serial(str(sys.argv[1]),int(sys.argv[2]))

#executes each line of the gcode
for line in gcode:
    response = ''
    #removes comments
    line = line.split(";")[0]
    #makes sure line is a valid command
    if(line != "" and line != "\n"):
        print("line: "+line)
        #writes the gcode to the printer
        printer.write(str.encode(line+'\n'))
        #waits for OK response from printer
        while response.count("ok") == 0:
            #waits for response
            while printer.in_waiting == 0:
                time.sleep(0.5)
            response = ''
            #gets response info
            while printer.in_waiting > 0:
                response += str(printer.readline())
            print(response)