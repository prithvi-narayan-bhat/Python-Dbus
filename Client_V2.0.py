# Date: Tue 22 Sep 2020 19:35

#imports the necessary libraies
import json
import sys
import time
from gi.repository import GLib
from pydbus import SessionBus

bus = SessionBus()
BUS = "org.example.demo.test"
server_object = bus.get(BUS)
loop = GLib.MainLoop()																												#instantiating the MainLoop() method
INT = 2

if len(sys.argv) == 1:																												#the application expects the user to provide a json file initially
	sys.exit('Please pass "card_data_V1.2.json" in the command line\n')
	

with open(sys.argv[1]) as f:			
	data = json.load(f)																													#instance to hold json dictionary

	def send_to_server():
		print(json.dumps(data, indent = 2))																				#prints json data in a formatted manner
			
		print('Sending screen data to server..\n')
		string = json.dumps(data)
		reply = server_object.echo_string(string)
#		print (len(data['screen_ui_t']))


if __name__ == "__main__":																										#main function that mimics station display infinitely
	GLib.timeout_add_seconds(interval=INT, function=send_to_server)
	loop.run()																																	#infinite loop
