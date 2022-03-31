import psutil
from pync import Notifier
from time import sleep

def check_battery():
    # get battery info
    battery = psutil.sensors_battery()
    if battery.percent <= 40 and battery.power_plugged == False:
        Notifier.notify("再不充電老子就死啦",title="現在電池低於40趕快給老子充電")
    elif battery.percent >= 90 and battery.power_plugged == True:
        Notifier.notify("再充電老子就死啦",title="現在電池高於80趕快給拔掉充電線")
while True:
    check_battery()
    sleep(600)