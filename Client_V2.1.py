# Date: Wed 23 Sep 2020 09:35

#imports the necessary libraies
import json
import sys
import time
from gi.repository import GLib
from pydbus import SessionBus

#variable declarations
bus = SessionBus()
#bus name
BUS = "com.semaconnect.S8_Displayd"
server_object = bus.get(BUS)
#instantiating the MainLoop() method
loop = GLib.MainLoop()
#global variables
INT = 2
count = 1
end = '}'

#the application expects the user to provide a json file initially
if len(sys.argv) == 1:
	sys.exit('Please pass "card_data_V1.2.json" in the command line\n')
	

with open(sys.argv[1]) as f:
	#to hold json dictionary			
	JSON_data = json.load(f)


def getScreen():
	global count
	while True:
		print('Print iteration: {}\n'.format(count))
		count += 1
		print(json.dumps(JSON_data, indent = 1))
		
		#prints screen_ui_t data in formatted manner
		JSON_string = json.dumps(JSON_data)
		
		#reformats the string
		screen_ui_t = JSON_string[: 1220] + JSON_string[1233 :]
		
		#appends a } to the end of json string
		screen_ui_t = " ".join((screen_ui_t, end))
		
		print('Sending screen data to server..\n')
		
		#passes SERVER_string as object to server via dbus
		reply = server_object.setScreen(screen_ui_t)
		time.sleep(JSON_data["delay"])
		return True


#main function that mimics station display infinitely
if __name__ == "__main__":
	print("\t\t\t\n\nScreen Data Emulator\n")
	GLib.timeout_add_seconds(interval=INT, function=getScreen)
	loop.run()
