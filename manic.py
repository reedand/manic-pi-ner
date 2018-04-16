#!/usr/bin/env python

"""Draws a scrolling Miner Willy sprite and banner animation/screensaver in homage to Manic Miner by Matthew Smith."""

import signal
import sys
import time
from sys import exit
from collections import deque

import dot3k.backlight as backlight
import dot3k.lcd as lcd
import dot3k.joystick as nav

is_active = True
bl_mode = False

STDERR = sys.stderr
def excepthook(*args):
    print >> STDERR, 'caught'
    print >> STDERR, args

sys.excepthook = excepthook

def signal_handler(signal, frame):
        global is_active
	is_active = False
	backlight.set_graph(0)
        lcd.clear()
	backlight.off()
        exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM,signal_handler)
signal.signal(signal.SIGQUIT,signal_handler)
signal.signal(signal.SIGHUP,signal_handler)

lcd.set_contrast(45)

#red
backlight.left_rgb(255,0,0)
#blue
backlight.mid_rgb(0, 255, 0)
#green
backlight.right_rgb(0,0, 255)

pos = 0

#all black char
black =[0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111,
	0b11111]

#bitmaps for custom letter m,n,r
m =    [
       [0b00000,
	0b00000,
	0b00000,
	0b11010,
	0b10101,
	0b10101,
	0b10001,
	0b10001],
       [0b00000,
        0b00000,
        0b11010,
        0b10101,
        0b10101,
        0b10001,
        0b10001,
	0b00000],
       [0b00000,
        0b11010,
        0b10101,
        0b10101,
        0b10001,
        0b10001,
        0b00000,
	0b00000],
       [0b11010,
        0b10101,
        0b10101,
        0b10001,
        0b10001,
        0b00000,
        0b00000,
	0b00000],
	[0b00000,
        0b11010,
        0b10101,
        0b10101,
        0b10001,
        0b10001,
        0b00000,
        0b00000],
	[0b00000,
        0b00000,
        0b11010,
        0b10101,
        0b10101,
        0b10001,
        0b10001,
        0b00000]
	]

n =    [
	[0b10110,
        0b11001,
        0b10001,
        0b10001,
        0b10001,
	0b00000,
	0b00000,
	0b00000],
       [0b00000,
	0b10110,
        0b11001,
        0b10001,
        0b10001,
        0b10001,
        0b00000,
        0b00000],
       [0b00000,
	0b00000,
        0b10110,
        0b11001,
        0b10001,
        0b10001,
        0b10001,
        0b00000],
       [0b00000,
        0b00000,
        0b00000,
        0b10110,
        0b11001,
        0b10001,
        0b10001,
        0b10001],
       [0b00000,
        0b00000,
        0b10110,
        0b11001,
        0b10001,
        0b10001,
        0b10001,
	0b00000],
       [0b00000,
        0b10110,
        0b11001,
        0b10001,
        0b10001,
        0b10001,
	0b00000,
	0b00000]
	]

r =    [
       [0b00000,
        0b10110,
        0b11001,
        0b10000,
        0b10000,
        0b10000,
        0b00000,
        0b00000],
       [0b00000,
        0b00000,
        0b10110,
        0b11001,
        0b10000,
        0b10000,
        0b10000,
	0b00000],
       [0b00000,
	0b00000,
	0b00000,
	0b10110,
	0b11001,
	0b10000,
	0b10000,
	0b10000],
       [0b00000,
        0b00000,
        0b10110,
        0b11001,
        0b10000,
        0b10000,
        0b10000,
        0b00000],
       [0b00000,
        0b10110,
        0b11001,
        0b10000,
        0b10000,
        0b10000,
        0b00000,
	0b00000],
       [0b10110,
        0b11001,
        0b10000,
        0b10000,
        0b10000,
        0b00000,
        0b00000,
	0b00000]
	]

#create the plain black char
lcd.create_char(4, black)

#combine the standard font m,n,r with our custom a,i,c,e to spell out manic miner on the first line of the display
line0 = chr(4) + chr(5) + 'a' + chr(7) + 'i' + 'c' + chr(4) * 2 + chr(5) + 'i' + chr(7) + 'e' + chr(6) + chr(4) * 2
#draw the background and manic miner sprite on display lines 2 and 3
line1 = chr(0) + chr(1) + chr(4) * 13
line2 = chr(2) + chr(3) + chr(4) * 13

#bitmap for the manic miner sprite in sections top left, top right, bottom left and bottom right
top_left = [
               [~0b00000,
                ~0b00011,
                ~0b00111,
                ~0b00011,
                ~0b00011,
                ~0b00011,
                ~0b00001,
                ~0b00011],

	       [~0b00000,
                ~0b00011,
                ~0b00111,
                ~0b00011,
                ~0b00011,
                ~0b00011,
                ~0b00001,
                ~0b00011],

	       [~0b00000,
                ~0b00011,
                ~0b00111,
                ~0b00011,
                ~0b00011,
                ~0b00011,
                ~0b00001,
                ~0b00011],

	       [~0b00000,
                ~0b00011,
                ~0b00111,
                ~0b00011,
                ~0b00011,
                ~0b00011,
                ~0b00001,
                ~0b00011]
           ]

top_right = [
	       [~0b01100,
                ~0b11100,
                ~0b11000,
                ~0b01000,
                ~0b11100,
                ~0b11000,
                ~0b10000,
                ~0b11000],

	       [~0b01100,
                ~0b11100,
                ~0b11000,
                ~0b01000,
                ~0b11100,
                ~0b11000,
                ~0b10000,
                ~0b11000],

	       [~0b01100,
                ~0b11100,
                ~0b11000,
                ~0b01000,
                ~0b11100,
                ~0b11000,
                ~0b10000,
                ~0b11000],

	       [~0b01100,
                ~0b11100,
                ~0b11000,
                ~0b01000,
                ~0b11100,
                ~0b11000,
                ~0b10000,
                ~0b11000]
           ]

bottom_left = [
	       [~0b00110,
                ~0b00110,
                ~0b00110,
                ~0b00111,
                ~0b00011,
                ~0b00001,
                ~0b00001,
                ~0b00001],

	       [~0b00111,
                ~0b00111,
                ~0b01111,
                ~0b01111,
                ~0b00011,
                ~0b00111,
                ~0b00110,
                ~0b00111],

	       [~0b00111,
                ~0b01111,
                ~0b11111,
                ~0b11011,
                ~0b00011,
                ~0b00111,
                ~0b01100,
                ~0b01110],

		[~0b00111,
                ~0b00111,
                ~0b01111,
                ~0b01111,
                ~0b00011,
                ~0b00111,
                ~0b00110,
                ~0b00111]
           ]

bottom_right = [
	       [~0b11100,
                ~0b11100,
                ~0b11100,
                ~0b01100,
                ~0b11000,
                ~0b10000,
                ~0b10000,
                ~0b11000],

	       [~0b11100,
                ~0b11100,
                ~0b01110,
                ~0b10110,
                ~0b11000,
                ~0b01100,
                ~0b11100,
                ~0b01110],
		
	       [~0b11100,
                ~0b11110,
                ~0b11111,
                ~0b11011,
                ~0b11100,
                ~0b01101,
                ~0b00111,
                ~0b00110],

	       [~0b11100,
                ~0b11100,
                ~0b01110,
                ~0b10110,
                ~0b11000,
                ~0b01100,
                ~0b11100,
                ~0b01110]
           ]

#handle left joystick press
@nav.on(nav.LEFT)
def handle_left(pin):
    global is_active
    is_active = False

#handle joystick button press
@nav.on(nav.BUTTON)
def handle_button(pin):
    global is_active
    is_active = False


def getAnimFrame(char, fps):
    return char[int(round(time.time() * fps) % len(char))]

while is_active:

    lcd.create_char(0, getAnimFrame(top_left, 4))
    lcd.create_char(1, getAnimFrame(top_right, 4))
    lcd.create_char(2, getAnimFrame(bottom_left, 4))
    lcd.create_char(3, getAnimFrame(bottom_right, 4))

    lcd.create_char(5, getAnimFrame(m,1))
    lcd.create_char(6, getAnimFrame(r,1))
    lcd.create_char(7, getAnimFrame(n,1))
  
    lcd.set_cursor_position(0,0)
    lcd.write(line0)
    lcd.set_cursor_position(0,1)
    lcd.write(line1)
    lcd.set_cursor_position(0, 2)
    lcd.write(line2)

    pos+= 1

    if pos % 10 == 0:
	str_dq = deque(line0)
	str_dq.rotate(-1)
	line0 = ''.join(str_dq)
	
    if pos % 5 == 0:
	str_dq = deque(line1)
	str_dq.rotate(1)
	line1 = ''.join(str_dq)
	str_dq = deque(line2)
	str_dq.rotate(1)
	line2 = ''.join(str_dq)
	
    if pos % 500 == 0:
	if bl_mode:
                #yellow
                backlight.left_rgb(255,0,255)
                #magenta
                backlight.mid_rgb(255,255, 0)
                #green
                backlight.right_rgb(0,255, 255)
                bl_mode = ~bl_mode
        else:
                #red
                backlight.left_rgb(255,0,0)
                #blue
                backlight.mid_rgb(0, 255, 0)
                #green
                backlight.right_rgb(0,0, 255)
                bl_mode = ~bl_mode

    if pos >= sys.maxint - 100000:
	pos = 0 

    time.sleep(0.005)

#reset the display and turn off backlight when quitting
if not(is_active):
    backlight.set_graph(0)
    lcd.clear()
    backlight.off()
    time.sleep(0.005)
    exit(0)
    
