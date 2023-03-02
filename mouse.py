from ctypes import Structure, windll, c_uint, sizeof, byref
import time

# http://stackoverflow.com/questions/911856/detecting-idle-time-in-python
class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

user32 = windll.user32
while True:
    d = get_idle_duration()
    if(d > 60 * 5):
        user32.mouse_event(1,1,1,0,0)
    time.sleep(60)

