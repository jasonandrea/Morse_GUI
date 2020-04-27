def longBlink():
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.95)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.45)
    
def shortBlink():
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.45)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.45)
    
def morseCode(letter):
    lowLetter = letter.lower()
    
    if lowLetter == 'a':
        shortBlink()
        longBlink()
        time.sleep(0.9)
    elif lowLetter == 'b':
        longBlink()
        for i in range(3):
            shortBlink()
        time.sleep(0.9)
    elif lowLetter == 'c':
        for i in range(2):
            longBlink()
            shortBlink()
        time.sleep(0.9)
    elif lowLetter == 'd':
        longBlink()
        for i in range(2):
            shortBlink()
        time.sleep(0.9)
    elif lowLetter == 'e':
        shortBlink()
        time.sleep(0.9)
    elif lowLetter == 'f':
        for i in range(2):
            shortBlink()
        longBlink()
        shortBlink()
        time.sleep(0.9)
    elif lowLetter == 'g':
        for i in range(2):
            longBlink()
        shortBlink()
        time.sleep(0.9)
    elif lowLetter == 'h':
        for i in range(4):
            shortBlink()
        time.sleep(0.9)
    elif lowLetter == 'i':
        for i in range(2):
            shortBlink()
        time.sleep(0.9)
    elif lowLetter == 'j':
        shortBlink()
        for i in range(3):
            longBlink()
        time.sleep(0.9)
    elif lowLetter == 'k':
        longBlink()
        shortBlink()
        longBlink()
        time.sleep(0.9)
    elif lowLetter == 'l':
        shortBlink()
        longBlink()
        for i in range(2):
            shortBlink()
        time.sleep(0.9)
    elif lowLetter == 'm':
        for i in range(2):
            longBlink()
        time.sleep(0.9)
    elif lowLetter == 'n':
        longBlink()
        shortBlink()
        time.sleep(0.9)
    elif lowLetter == 'o':
        for i in range(3):
            longBlink()
        time.sleep(0.9)
    elif lowLetter == 'p':
        shortBlink()
        for i in range(2):
            longBlink()
        shortBlink()
        time.sleep(0.9)
    elif lowLetter == 'q':
        for i in range(2):
            longBlink()
        shortBlink()
        longBlink()
        time.sleep(0.9)
    elif lowLetter == 'r':
        shortBlink()
        longBlink()
        shortBlink()
        time.sleep(0.9)
    elif lowLetter == 's':
        for i in range(3):
            shortBlink()
        time.sleep(0.9)
    elif lowLetter == 't':
        longBlink()
        time.sleep(0.9)
    elif lowLetter == 'u':
        for i in range(2):
            shortBlink()
        longBlink()
        time.sleep(0.9)
    elif lowLetter == 'v':
        for i in range(3):
            shortBlink()
        longBlink()
        time.sleep(0.9)
    elif lowLetter == 'w':
        shortBlink()
        for i in range(2):
            longBlink()
        time.sleep(0.9)
    elif lowLetter == 'x':
        longBlink()
        for i in range(2):
            shortBlink()
        longBlink()
        time.sleep(0.9)
    elif lowLetter == 'y':
        longBlink()
        shortBlink()
        for i in range(2):
            longBlink()
        time.sleep(0.9)
    elif lowLetter == 'z':
        for i in range(2):
            longBlink()
        for i in range(2):
            shortBlink()
        time.sleep(0.9)
    elif letter == '0':
        for i in range(5):
            longBlink()
        time.sleep(0.9)
    elif letter == '1':
        shortBlink()
        for i in range(4):
            longBlink()
        time.sleep(0.9)
    elif letter == '2':
        for i in range(2):
            shortBlink()
        for i in range(3):
            longBlink()
        time.sleep(0.9)
    elif letter == '3':
        for i in range(3):
            shortBlink()
        for i in range(2):
            longBlink()
        time.sleep(0.9)
    elif letter == '4':
        for i in range(4):
            shortBlink()
        longBlink()
        time.sleep(0.9)
    elif letter == '5':
        for i in range(5):
            shortBlink()
        time.sleep(0.9)
    elif letter == '6':
        longBlink()
        for i in range (4):
            shortBlink()
        time.sleep(0.9)
    elif letter == '7':
        for i in range(2):
            longBlink()
        for i in range(3):
            shortBlink()
        time.sleep(0.9)
    elif letter == '8':
        for i in range(3):
            longBlink()
        for i in range(2):
            shortBlink()
        time.sleep(0.9)
    else:
        for i in range(4):
            longBlink()
        shortBlink()
        time.sleep(0.9)
        
def blinkCode():
    chars = [char for char in word.get()]
    if len(chars) <= 12:
        for char in chars:
            morseCode(char)
    else:
        messagebox.showerror('Error', 'Cannot blink more than 12 characters!')
        
def close():
    GPIO.cleanup()
    win.destroy()

from tkinter import *
from tkinter import messagebox
import RPi.GPIO as GPIO
import time

led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

# Make sure the LED is off when starting the program
GPIO.output(led, GPIO.LOW)

win = Tk()
win.title('Morse Code Creator')

word = StringVar()
textInput = Entry(win, width = 15, textvariable = word)
textInput.grid(row = 1, column = 1)

button = Button(win, text = 'Blink!', command = blinkCode)
button.grid(row = 2, column = 1)

win.protocol('WM_DELETE_WINDOW', close)

win.mainloop()