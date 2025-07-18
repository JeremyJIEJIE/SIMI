import os
import time

def tap(x, y):
    os.system(f"input tap {x} {y}")
    time.sleep(1)

def launch_home():
    os.system("am start -n com.duokan.phone.remotecontroller/com.xiaomi.mitv.phone.remotecontroller.HoriWidgetMainActivityV2")
    time.sleep(5)

def control_aircon():
    launch_home()
    tap(300, 700)   # 点设备
    time.sleep(2)
    tap(300, 1167)  # 点电源

while True:
    os.system("termux-toast 开机")
    control_aircon()
    time.sleep(1800)

    os.system("termux-toast 关机")
    control_aircon()
    time.sleep(1800)
