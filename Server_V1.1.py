#Date: Tue 22 Sep 2020 10:14

#Libraries
from pydbus import SessionBus
from gi.repository import GLib
import time
import json

#Varaiables
#instantiate #System Bus
bus = SessionBus()

#constant for a well known name
BUS = "com.semaconnect.S8_Displayd"

#GLib loop Instantiate
loop = GLib.MainLoop()

#global varaibale to hold iteration count
count = 1 
	
class DBusService_XML():
	"""
	DBus Service XML Definition
	type= "i" for integer, "s" for string, "d" for double, "as" list of string data
	"""
	dbus = """
	<node>
		<interface name="{}">
			<method name="setScreen">
				<arg type="s" name="screen_data" direction="in">
				</arg>
			</method>
		</interface>
	</node>
	""".format(BUS)
	
	def setScreen(self, screen_data):
		global count
		print('\n\nPrint iteration: {}\n'.format(count))
		count += 1
		
		#formats string into json
		data = json.loads(screen_data)
		
		#prints screen data in a formatted manner
		print(json.dumps(data, indent = 1))
		return True
		
if __name__ == "__main__":
	#Publish
	bus.publish(BUS, DBusService_XML())

	#GLib loop
	loop.run()
