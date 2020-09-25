#Version 1.1
#Draft Time: Wed 16 Sep 2020 11:43


# importing the necessary libraries
from enum import Enum
from gi.repository import GLib


#class enumerates the types of media that can be displayed	
class media_type_t(Enum):
	MEDIA_TYPE_QRCODE = 0
	MEDIA_TYPE_IMAGE = 1
	MEDIA_TYPE_GIF = 2


#class enumerates the types of screens
class screen_type_t(Enum):
	SCREEN_TYPE_S1 = 0
	SCREEN_TYPE_S2  = 1


#class enumerates the types of cards
class card_type_t_100(Enum):
	CARD_TYPE_W100_BLUE_SPLASH = 0
	CARD_TYPE_W100_GRAY_STRING3 = 1
	CARD_TYPE_W100_GRAY_MEDIA = 2
	CARD_TYPE_W100_GRAY_MEDIA_STRING3 = 3
	CARD_TYPE_W100_RED_MEDIA_STRING3 = 4
	CARD_TYPE_W100_USERCOLOR_MEDIA_STRING_3 = 5


class card_type_t_50(Enum):
	CARD_TYPE_W50_GRAY_MEDIA_STRING2 = 6
	CARD_TYPE_W50_GREEN_MEDIA_STRING2 = 7
	CARD_TYPE_W50_BLUE_MEDIA_STRING2 = 8
	CARD_TYPE_W50_RED_MEDIA_STRING2 = 9
	CARD_TYPE_W50_AMBER_MEDIA_STRING2 = 10
	CARD_TYPE_W50_GREEN_TITLE_STRING4 = 11
	CARD_TYPE_W50_GREEN_TITLE_STRING3 = 12
	CARD_TYPE_W50_USERCOLOR_MEDIA_STRING2 = 13


class screen_ui_t():		

		"""
		Method 1
			This reads the type of screen from the user
		"""
		screen_type = 0
		def screen_type(self):
			global screen_type
			screen_type = int(input('Enter a screen type (0=SCREEN_TYPE_S1 / 1=SCREEN_TYPE_S2): '))
			if screen_type == 0:
				print('Screen set to: {}\n'.format(screen_type_t(screen_type)))
			elif screen_type == 1:
				print('Screen set to: {}\n'.format(screen_type_t(screen_type)))
			else:
				print('Invalid input\n')


		"""
		Method 2
			This reads and sets the Station's Serial Address
		"""
		def station_info_t(self):
			serial = str(input('Enter Serial number of station: '))
			#reads Serial number of the station
			print('Serial address set as: {}\n'.format(serial))


		"""
		Method 3
			This sets or clears the header visiblity on the screen
		"""
		def HEADER_VIS(self):
			header = int(input('Header visibility (0=HIDE/1=SHOW): '))
			#reads the choice to show or hide header (sets Bool values based on user choice)
			if header == 0:
				header_visibility = False
				print('Header set to HIDE\n')
			elif header == 1:
				header_visibility = True
				print('Header set to SHOW\n')
			else:
				print('Invalid input\n')
				exit()

		
		"""
		Child Class 1
			This reads Card parameters from the user and sets the same to each card
		"""
		class card_ui_t:
			"""
			Child-Method 1
				This reads and sets the type of card to be displayed on the screen
			"""
			card_type = 0 	#default card type
			def Card_Type(self):
				#parameter 1
				global screen_type
				global card_type
				if screen_type == 0:
					i = 0 #to display count of ENUM listing
					for types in card_type_t_100:
						print('{}'.format(i), types)
						i += 1
					card_type = int(input('Enter ENUM index (0-5)\nSelect Card type: '))
					#reads card type from user
					#assigns through ENUM index
					try:
						print('Card type set to: ')
						print(card_type_t_100(card_type))
					except:
						print('Input value does not match any defined card types')
						exit()
				
				elif screen_type == 1:
					i = 6 #to display count of ENUM listing
					for types in card_type_t_50:
						print('{}'.format(i), types)
						i += 1
					card_type = int(input('Enter ENUM index (6-13)\nSelect Card type: '))
					#reads card type from user
					#assigns through ENUM index
					try:
						print('Card type set to: ')
						print(card_type_t_50(card_type))
					except:
						print('Input value does not match any defined card types')
						exit()


			"""
			Child-Method 2
				This sets or clears the header visiblity on the screen
			"""
			#parameter 2
			#this parameter is read only if the user chooses 
			#5 card_type_t.CARD_TYPE_W100_USERCOLOR_MEDIA_STRING_3 or 
			#11 card_type_t.CARD_TYPE_W50_USERCOLOR_MEDIA_STRING2
			def BackGround_Color(self):
				global card_type
				if card_type == 5 or card_type == 13:
					card_bgcolor = int(input('\nEnter Background Color: '))
					#reads background color from user
					#assumed to be a integer value
					print('\nBackground color set to: {}\n'.format(card_bgcolor))
				else:
					print('\nBackground color set by default as per card formatting\n')


			"""
			Child-Method 3
				This reads the slot index of the card from the user
			"""
			slot_index = -1
			def SlotIndex(self):
				global slot_index
				global screen_type
				#parameter 3
				if screen_type == 1:
					slot_index = int(input('Enter the slot index (0=LEFT/1=RIGHT): '))
					print('Slot index set as: {}\n'.format(slot_index))

			"""
			Child-Method 4
				This Shows or hides the Flipper
			"""
			#parameter 4
			flipper_visibility = -1
			def FlipperVisibility(self):
				global screen_type
				if screen_type == 1:
					choice = int(input('FLIPPER Visibility (0=HIDE/1=SHOW): '))
					#reads users choice to either show or hide flipper.
					#sets Bool value appropriately
					global flipper_visibility
					if choice == 0:
						flipper_visibility = False
						print('Flipper set to HIDE\n')
					elif choice == 1:
						flipper_visibility = True
						print('Flipper set to SHOW\n')
					else:
						print('Invalid choice\n')
						print('Flipper set to default value: HIDE\n')
						flipper_visibility = False
				else:
					flipper_visibility = False
			

			"""
			Child-Method 5
				This sets the flipper between two parameters
			"""
			#parameter 5
			def FlipIndex(self):
				global flipper_visibility
				if flipper_visibility == True:
					flipper_index = int(input('Enter the flipper index(0/1): '))
					#reads index of Flipper from user
					if flipper_index != 0 or flipper_index != 1:
						print('Invalid index\n')
						exit()
					print('Flipper index set to: {}\n'.format(flipper_index))			
			
			"""
			Child-Method 6
				This reads the type of media file to display
			"""
			def MediaType(self):
				#parameter 6
				global card_type
				if card_type != 0 or card_type != 1 or card_type != 11 or card_type != 12:
					i = 0 	#to display count of ENUM listing
					for media in media_type_t:
						print('{}'.format(i), media)
						i += 1
					media_type = int(input('Enter ENUM index (0-2)\nSelect Media type: '))
					#reads the media type from user through ENUM index
					print('Media type set to: ')
					print(media_type_t(media_type))

					#parameter 7
					#all paths are hardcoded now as recommended
					if media_type == 0:
						media_path = "directory0/directory1/directory4/QR_file.ext"
						print('\nMedia Path set to: {}\n'.format(media_path))
					elif media_type == 1:
						media_path = "directory0/directory1/directory4/IMAGE_file.ext"
						print('\nMedia Path set to: {}\n'.format(media_path))
					elif media_type == 2:
						media_path = "directory0/directory1/directory4/GIF_file.ext"
						print('\nMedia Path set to: {}\n'.format(media_path))
					else:
						print('Invalid Media Type\n')
						exit()
				
				else:
					print('Card type does not support any media\n')
			
			
			"""
			Child-Method 7
				This reads the title of the card
			"""			
			def Title(self):
				#parameter 8
				#reads the title for the card selected
				global card_type
				global slot_index
				if card_type == 11 or card_type == 12:
					title = str(input('Enter the title of card {}: '.format(slot_index)))
					print('Title for Card {} set as: {}'.format(slot_index,title))
			
			
			"""
			Child-Method 8
				This relevant number of strings for the card
			"""			
			#parameter 8,9,10,11
			#Only strings relevant to the user selected cards are read.
			#Other strings are ignored
			#cards 1 and 2 expect no string
			def String(self):
				global card_type
				if card_type == 3 or card_type == 4 or card_type == 5 or card_type == 1 or card_type == 12:
				#cards 2, 3, 4 5 and 13 expect 3 strings
					print('Selected card expects 3 strings\n')
					string1 = str(input('Enter string 1: '))
					string2 = str(input('Enter string 2: '))
					string3 = str(input('Enter string 3: '))
					
					print('String 1: {}\nString 2: {}\nString 3: {}'.format(string1, string2, string3))

				elif card_type == 6 or card_type == 7 or card_type == 8 or card_type == 9 or card_type == 10 or card_type == 13:
				#cards 6, 7, 8, 9, 10, 11 expect 2 strings
					print ('Selected card expects 2 strings\n')
					string1 = str(input('Enter string 1: '))
					string2 = str(input('Enter string 2: '))

					print('String 1: {}\nString 2: {}\n'.format(string1, string2))
					
				elif card_type == 11:
					print('Selected card expects 4 strings\n')
					string1 = str(input('Enter string 1: '))
					string2 = str(input('Enter string 2: '))
					string3 = str(input('Enter string 3: '))
					string4 = str(input('Enter string 4: '))
					
					print('String 1: {}\nString 2: {}\nString 3: {}\nString 4: {}'.format(string1, string2, string3, string4))
				
				else: 
					print('Selected card {} doesnot expect any strings\n'.format(card_type_t(card_type)))



#Main Function outside of Class Definitions

Screen = screen_ui_t() 					#creating an object of the class screen_ui_t
																#This class initialises all details relating to the Screen/Display
Screen.screen_type()						#method call for screen_type
Screen.station_info_t()					#method call to set serial number of station
Screen.HEADER_VIS()							#method call to show or hide header

Card = Screen.card_ui_t() 			#creating an object of child class card_ui_t
																#this class defines all paramters relating to the Card details
Card.Card_Type() 								#method call to set the type of the card
Card.BackGround_Color()					#method call to set the background color of the card (essential only for two cards)
Card.SlotIndex()								#method call to set the slot_index
Card.FlipperVisibility()				#method to show or hide flipper
Card.FlipIndex()								#method to set the index of the flipper
Card.MediaType()								#method to choose the media type to display on the card
Card.Title() 										#method to set the title of the card
Card.String() 									#method to set the strings to be displayed on each card
