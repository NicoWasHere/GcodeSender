import pygame
import serial
import time
import sys

printer = serial.Serial(str(sys.argv[1]),int(sys.argv[2]))

time.sleep(1)
printer.write(str.encode("G28 \n"))
printer.write(str.encode("G1 Z5\n"))

pygame.init()

lastPos = (0,0)
screen = pygame.display.set_mode([750,750])
w, h = pygame.display.get_surface().get_size()

running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    #gets the mouse position
    mouse_position = pygame.mouse.get_pos()

    if mouse_position!=lastPos:
        print(mouse_position)
        printer.write(str.encode('G1X'+str(mouse_position[0]/750*300)+"Y"+str(300-mouse_position[1]/750*300)+"\n"))
        xchange = abs((mouse_position[0]-lastPos[0])/750*300)
        ychange = abs((mouse_position[1]-lastPos[1])/750*300)
        time.sleep(xchange/25 if xchange>ychange else ychange/25)
    lastPos = mouse_position

    pygame.draw.line(screen,(0,0,0),(0,mouse_position[1]),(w,mouse_position[1]),3)
    pygame.draw.line(screen,(0,0,0),(mouse_position[0],0),(mouse_position[0],h),3)

    #puts a dot at the mouse position
    pygame.draw.circle(screen,(255,0,0),mouse_position, 5)

    pygame.draw.line(screen,(0,0,0),(0,mouse_position[1]),(w,mouse_position[1]),3)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()