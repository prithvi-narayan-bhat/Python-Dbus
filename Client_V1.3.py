# Date: Mon 21 Sep 2020 12:12

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
	sys.exit('Please pass "card_data.json" in the command line\n')
	

with open(sys.argv[1]) as f:			

	data = json.load(f)																													#vriable to hold json data
	tap = 0																																			#global variable to hold the tap status
		
	def Bootup_Sequence(): 																											#function prints all data relating to Bootup sequence cards
		for i in data["Bootup_Sequence"]: 
			print("Screen Type:\t", i['screen_type'])
			print("Card Type:\t", i['card_type'])
			print("slot_index:\t", i['slot_index'])
			print("String1:\t", i['string1'])		
			print("String2:\t", i['string2'])
			print("Media Path:\t", i['media_path'])
			if i['screen_type'] == "SCREEN_TYPE_S0":
				print("Header:\t\t", i['header'])
		
		print()
		
		print('Sending Bootup_Sequence card data to server..\n')
		string = ",".join(str(i) for i in data["Bootup_Sequence"])
		reply = server_object.echo_string(string)
		time.sleep(2)
		print('Received by server\n')
		#return True


############################################################################################################################



	def Dormant_Rest():																													#function prints data of two cards relating to the dormant status of the station  
		print('\n\n')
		print('Dormant State\n')
		for i in data["Dormant_Rest"]: 
			print("Screen Type:\t", i['screen_type'])
			print("Card Type:\t", i['card_type'])
			print("slot_index:\t", i['slot_index'])	
			print("String1:\t", i['string1'])
			print("String2:\t", i['string2'])
			print("media_type:\t", i['media_type'])
			print("Media Path:\t", i['media_path'])

			if i['screen_type'] == "SCREEN_TYPE_S1":
				print("Flipper_Vis:\t", i['flipper_visibility'])
				
				if i['flipper_visibility'] != "Show": 
					print("Flipper Index:\t", i['flipper_index'])
			print()
		global tap
		print('Sending Dormant_State card data to server..\n')
		string = ",".join(str(i) for i in data["Dormant_Rest"])
		reply = server_object.echo_string(string)
		time.sleep(2)
		print('Waiting for input from server\n')

		tap = server_object.activation_status()
		#return True
		
	
	def left_tap():																															#function prints the data of cards invoked when the left slot is activated
		print('\n\n')
		print('Slot 0 Activated\n')
		for i in data["Slot_0_activated"]: 
			print("\nScreen Type:\t", i['screen_type'])
			print("Card Type:\t", i['card_type'])
			print("slot_index:\t", i['slot_index'])
			print("Flipper_Vis:\t", i['flipper_visibility'])
			if i['flipper_visibility'] != "Show": 
				print("Flipper Index:\t", i['flipper_index'])
			if i['card_type'] == "CARD_TYPE_W50_GREEN_TITLE_STRING4​":
				print("Title:\t\t", i['Title'])
				print("String1:\t", i['string1'])
				print("String2:\t", i['string2'])
				print("String2:\t", i['string3'])
				print("String2:\t", i['string4'])
			if i['card_type'] == "CARD_TYPE_W50_GREEN_TITLE_STRING3":
				print("Title:\t\t", i['Title'])
				print("String1:\t", i['string1'])
				print("String2:\t", i['string2'])
				print("String2:\t", i['string3'])
			time.sleep(1)
		print()
		
		print('Sending Slot 0 card data to server..\n')
		string = ",".join(str(i) for i in data["Slot_0_activated"])
		reply = server_object.echo_string(string)
		time.sleep(2)
		print('Received by server\n')
		#return True
			
		
	def all_call():
		global tap
		Bootup_Sequence()																														#calls the method to emulate bootup state
		time.sleep(1)
		while tap != 1 and tap != 2:																								#tap == 1 emulates activation of slot 0 tap == 1 exit()
			Dormant_Rest()																														#calls the method to emulate dormant state
			time.sleep(2)
		if tap == 1:
			left_tap()																																#calls the method to emulate activation of the left slot
			print('Charging Done\nSlot freed\n')
			tap = 0
			time.sleep(2)
			Dormant_Rest()																														#Again calls the dormant state upon the completion of charging in slot 0			
		reply = server_object.echo_string(Bootup_Sequence())
		print("Message echoed from server: {}".format(reply))
		#return True
		

if __name__ == "__main__":																										#main function that mimics station display infinitely
	print("Starting Client Demo..")
	GLib.timeout_add_seconds(interval=INT, function=all_call)
	loop.run()																																	#infinite loop
