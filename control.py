#controlling your mouse
#using pynput you can listen and control your keyboard and mouse
#using keyboard function we can type anything wherever the cursor points
from pynput.mouse import Controller
from pynput.keyboard import Controller
#(left to right,top to bottom)
#from top left of the screen you can imagine the top left to be (0,0)
def controlMouse():
    mouse = Controller()
    mouse.position = (10,20)
controlMouse()
def controlKeyboard():
    keyboard = Controller()
    keyboard.type('I am tired of this')
controlKeyboard()
