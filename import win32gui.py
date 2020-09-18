import win32gui
from PIL import Image, ImageGrab
TITLESTRING = "EVE - Tank Shitty"
import win32ui
import win32con
from time import sleep

def screenshot(hwnd = None):
    if not hwnd:
        hwnd=win32gui.GetDesktopWindow()
    l,t,r,b=win32gui.GetWindowRect(hwnd)
    h=b-t
    w=r-l
    hDC = win32gui.GetWindowDC(hwnd)
    myDC=win32ui.CreateDCFromHandle(hDC)
    newDC=myDC.CreateCompatibleDC()

    myBitMap = win32ui.CreateBitmap()
    myBitMap.CreateCompatibleBitmap(myDC, w, h)

    newDC.SelectObject(myBitMap)

    win32gui.SetForegroundWindow(hwnd)
    sleep(.2) #lame way to allow screen to draw before taking shot
    newDC.BitBlt((0,0),(w, h) , myDC, (0,0), win32con.SRCCOPY)
    myBitMap.Paint(newDC)
    myBitMap.SaveBitmapFile(newDC,'tmp.bmp')
def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append( (hwnd, win32gui.GetWindowText(hwnd) ) )

def get_app_list(handles=[]):
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst

def get_window_info():
    window_info={}
    win32gui.EnumWindows(set_window_coordinates, window_info)
    return window_info

def set_window_coordinates(hwnd, window_info):
    if win32gui.IsWindowVisible(hwnd):
        if TITLESTRING in win32gui.GetWindowText(hwnd):
            rect = win32gui.GetWindowRect(hwnd)
            x= rect[0]
            y= rect[1]
            w= rect[2]-x
            h= rect[3]-y
            window_info['x']=x
            window_info['y']=y
            window_info['width']=w
            window_info['height']=h
            window_info['name']=win32gui.GetWindowText(hwnd)
            win32gui.SetForegroundWindow(hwnd)

def Get_screen (x1, y1, x2, y2):
    box(x1 + 8, y1 + 30, x2 - 8, y2)
    screen = ImageGrab(box)
    img=array(screen.getdata(), dtype = uint8).reshape((screen.size[1], screen.size[0], 3))
    return img

appwindows = get_app_list()
meme = get_window_info()

for i in appwindows:
    str2 = i[1]
    if str2 == TITLESTRING:
        print(i[0])
        screenshot(i[0])
print(meme["name"])
img1 = ImageGrab.grab()
img2 = ImageGrab.grab((
    meme["x"],
    meme["y"],
    meme["x"] + meme["width"],
    meme["y"] + meme["height"]
))
#img1.show()
#img2.show()