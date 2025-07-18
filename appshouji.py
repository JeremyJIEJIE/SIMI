import os
import time

def tap(x, y):
    os.system(f"input tap {x} {y}")
    time.sleep(1)

def launch_home():
    # 启动遥控器 App 首页
    os.system("am start -n com.duokan.phone.remotecontroller/com.xiaomi.mitv.phone.remotecontroller.HoriWidgetMainActivityV2")
    time.sleep(3)  # 等待遥控器首页加载

def control_aircon():
    launch_home()
    
    tap(300, 700)   # 点击空调设备
    time.sleep(3)   # 等待进入设备界面
    
    tap(300, 1167)  # 点击电源按钮

while True:
    os.system("termux-toast ✅ 开机中")
    control_aircon()
    time.sleep(1800)

    os.system("termux-toast ❎ 关机中")
    control_aircon()
    time.sleep(1800)
