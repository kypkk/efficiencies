import psutil
import osascript
from time import sleep
import threading
import os

def check_battery():
    while True:
        battery = psutil.sensors_battery() # get battery info
        # print(battery)
        if battery.percent <= 40 and battery.power_plugged == False:
            osascript.run('tell application "battery" to notify("Plug the cable in", "Battery is now lower than 40%")')
        elif battery.percent >= 90 and battery.power_plugged == True:
            osascript.run('tell application "battery" to notify("Plug the  cable out", "Battery is now higher than 80%")')
        sleep(600)

def check_volume():
    while True:
        osascript.run('tell application "set_volume" to run')
        sleep(60)
        
def open_message():
    while True:
        os.system("cd /Users/kangkang/kypkk/efficiencies/open_school_messages.app/Contents/MacOS \n ./applet")
        sleep(3600)

# driver code
if __name__ == '__main__':
    battery = threading.Thread(target=check_battery)
    volume = threading.Thread(target=check_volume)
    message = threading.Thread(target=open_message)
    battery.start()
    volume.start()
    message.start()
    battery.join()
    volume.join()
    message.join()