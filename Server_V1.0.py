#Date: Tue 22 Sep 2020 10:14

#Libraries
from pydbus import SessionBus
from gi.repository import GLib
import time

#Varaiables
bus = SessionBus() #instantiate #System Bus
BUS = "org.example.demo.test" #constant for a well known name
loop = GLib.MainLoop()	#GLib loop Instantiate

	
class DBusService_XML():
	"""
	DBus Servie XML Definition
	type= "i" for integer, "s" for string, "d" for double, "as" list of string data
	"""
	dbus = """
	<node>
		<interface name="{}">
			<method name="echo_string">
				<arg type="s" name="card_data" direction="in">
				</arg>
			</method>
			<method name="activation_status">
				<arg type= "i" name = "slot" direction = "out">
				</arg>
			</method>
		</interface>
	</node>
	""".format(BUS)
	
	def echo_string(self, card_data):
		"Prints the string as is"
		print("Received: {}\n".format(card_data))
		return True
	
	def activation_status(self):
		tap = int(input('Enter 1 to emulate slot 0: '))
		return tap

		
if __name__ == "__main__":
	bus.publish(BUS, DBusService_XML())  #Publish
	loop.run()	#GLib loop Instantiate
