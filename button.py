from gpiozero import Button
from signal import pause

print "HELLO"

def doStuff():
  print "PRESSED!"

button = Button(3)
button.when_pressed = doStuff

pause()
