#!/usr/bin/env python
 
import notify2
import gc

def battery_check():
 
	state = open("/sys/class/power_supply/BAT1/status","r").readline().strip()
	percentage = int(open("/sys/class/power_supply/BAT1/capacity","r").readline().strip())
	print(state,percentage)

	notify2.init("Battery Alert!")
 
	if state == "Discharging" and percentage < 20:
		notification = notify2.Notification("Battery Low!",str(percentage)+"%. I'm hungry. ","/home/balumn/dev/battery-alert/battery-low.png")
		notification.show()
		del notification

	if state == "Discharging" and percentage < 10:
		notification = notify2.Notification("Battery Empty!",str(percentage)+"%. Now or never!! ","/home/balumn/dev/battery-alert/battery-low.png")
		notification.show()
		del notification
	
	elif state == "Charging" and percentage == 100:
		notification = notify2.Notification("Battery Full!",str(percentage)+"%. Unplug me.","/home/balumn/dev/battery-alert/battery-full.png")
		notification.show()
		del notification

	elif state == "Charging" and percentage > 90:
		notify2.init("Battery Alert!")
		notification = notify2.Notification("Battery About to full!",str(percentage)+"%. Unplug me.","/home/balumn/dev/battery-alert/battery-full.png")
		notification.show()
		del notification
	gc.collect()
	
if __name__ == "__main__": battery_check()