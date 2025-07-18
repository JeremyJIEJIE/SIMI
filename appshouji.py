import os
import time

# 点击指定坐标
def tap(x, y):
    os.system(f"input tap {x} {y}")
    time.sleep(1)

# 启动遥控器首页
def launch_home():
    os.system("am start -n com.duokan.phone.remotecontroller/com.xiaomi.mitv.phone.remotecontroller.HoriWidgetMainActivityV2")
    time.sleep(8)  # 增加等待时间，确保页面加载完成

# 控制空调（点设备 → 点电源）
def control_aircon():
    launch_home()
    tap(300, 700)   # 点击空调设备（坐标请视实际微调）
    time.sleep(3)   # 等待设备界面加载
    tap(300, 1167)  # 点击电源按钮

# 循环每 30 分钟开/关空调
while True:
    os.system("termux-toast ✅ 开机中")
    control_aircon()
    time.sleep(1800)

    os.system("termux-toast ❎ 关机中")
    control_aircon()
    time.sleep(1800)
