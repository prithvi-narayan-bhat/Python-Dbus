from enum import Enum

from gi.repository import GLib
# importing the necessary libraries

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
class card_type_t(Enum):
	CARD_TYPE_W100_BLUE_SPALSH = 0
	CARD_TYPE_W100_GRAY_MEDIA = 1
	CARD_TYPE_W100_GRAY_STRING3 = 2
	CARD_TYPE_W100_GRAY_MEDIA_STRING3 = 3
	CARD_TYPE_W100_RED_MEDIA_STRING3 = 4
	CARD_TYPE_W100_USERCOLOR_MEDIA_STRING_3 = 5
	CARD_TYPE_W50_RED_MEDIA_STRING2 = 6
	CARD_TYPE_W50_AMBER_MEDIA_STRING2 = 7
	CARD_TYPE_W50_GRAY_MEDIA_STRING2 = 8
	CARD_TYPE_W50_GREEN_MEDIA_STRING2 = 9
	CARD_TYPE_W50_BLUE_MEDIA_STRING2 = 10
	CARD_TYPE_W50_USERCOLOR_MEDIA_STRING2 = 11
	CARD_TYPE_W50_GREEN_TITLE_STRING4 = 12
	CARD_TYPE_W50_GREEN_TITLE_STRING3 = 13





class screen_ui_t():	

		"""
		Object 1
			This reads the type of screen from the user
		"""
		def screen_type(self):
			choice = int(input('Enter a screen type (0=TYPE_S1/1=TYPE_S2): '))
			if choice == 0:
				print('Screen set to: {}\n'.format(screen_type_t.SCREEN_TYPE_S1))
			elif choice == 1:
				print('Screen set to: {}\n'.format(screen_type_t.SCREEN_TYPE_S2))
			else:
				print('Invalid input\n')



		

		"""
		Object 2
			This reads and sets the Station's Serial Address
		"""
		class station_info_t:
			serial = str(input('Enter Serial number of station: '))
			#reads Serial number of the station
			print('Serial address set as: {}\n'.format(serial))
			




		"""
		Object 3
			This sets or clears the header visiblity on the screen
		"""
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
		Object 4
			This reads Card parameters from the user and sets the same to each card
		"""
		class card_ui_t:


			#parameter 1
			i = 0 #to display count of ENUM listing
			for types in card_type_t:
				print('{}'.format(i), types)
				i += 1
			try:
				card_type = int(input('Enter ENUM index (0-13)\nSelect Card type: '))
				#reads card type from user
				#assigns through ENUM index
				print('Card type set to: ')
				print(card_type_t(card_type))
			except:
				print('Input value does not match any defined card types')
				exit()
				
			
			#parameter 2
			#this parameter is read only if the user chooses 
			#5 card_type_t.CARD_TYPE_W100_USERCOLOR_MEDIA_STRING_3 or 
			#11 card_type_t.CARD_TYPE_W50_USERCOLOR_MEDIA_STRING2
			if card_type == 5 or card_type == 11:
				card_bgcolor = int(input('\nEnter Background Color: '))
				#reads background color from user
				#assumed to be a integer value
				print('Background color set to: {}\n'.format(card_bgcolor))
			else:
				print('Background color set by default as per card formatting\n')


			#parameter 3
			slot_index = int(input('Enter the slot index (0=LEFT/1=RIGHT): '))
			print('Slot index set as: {}\n'.format(slot_index))
			


			#parameter 4
			choice = int(input('FLIPPER Visibility (0=HIDE/1=SHOW): '))
			#reads users choice to either show or hide flipper.
			#sets Bool value appropriately
			if choice == 0:
				flipper_visibility = False
				print('Flipper set to HIDE\n')
			elif choice == 1:
				flipper_visibility = True
				print('Flipper set to SHOW\n')
			else:
				print('Invalid choice\n')
				exit()
			


			#parameter 4
			flipper_index = int(input('Enter the flipper index: '))
			#reads index of Flipper from user
			print('Flipper index set to: {}\n'.format(flipper_index))
			



			#parameter 5
			i = 0	#to display count of ENUM listing
			for media in media_type_t:
				print('{}'.format(i), media)
				i += 1
			media_type = int(input('Enter ENUM index (0-2)\nSelect Media type: '))
			#reads the media type from user through ENUM index
			print('Media type set to: ')
			print(media_type_t(media_type))
			
			#parameter 6 hardcoded now as recommended
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
			
			
			#parameter 7
			#reads the title for the card selected 
			title = str(input('Enter the title of card {}: '.format(slot_index)))
			print('Title for Card {} set as: {}'.format(slot_index,title))
			
			
			
			#parameter 8,9,10,11
			#Only strings relevant to the user selected cards are read.
			#Other strings are ignored
			#cards 1 and 2 expect no string
			if card_type == 2 or card_type == 3 or card_type == 4 or card_type == 5 or card_type == 13:
			#cards 2, 3, 4 5 and 13 expect 3 strings
				print('Selected card {} expects 3 strings\n'.format(card_type_t(card_type)))
				string1 = str(input('Enter string 1: '))
				string2 = str(input('Enter string 2: '))
				string3 = str(input('Enter string 3: '))
				
				print('String 1: {}\nString 2: {}\nString 3: {}'.format(string1, string2, string3))

			elif card_type == 6 or card_type == 7 or card_type == 8 or card_type == 9 or card_type == 10 or card_type == 11:
			#cards 6, 7, 8, 9, 10, 11 expect 2 strings
				print ('Selected card {} expects 2 strings\n'.format(card_type_t(card_type)))
				string1 = str(input('Enter string 1: '))
				string2 = str(input('Enter string 2: '))

				print('String 1: {}\nString 2: {}\nString 3: {}'.format(string1, string2, string3))
				
			elif card_type == 12:
				print('Selected card {} expects 4 strings\n'.format(card_type_t(card_type)))
				string1 = str(input('Enter string 1: '))
				string2 = str(input('Enter string 2: '))
				string3 = str(input('Enter string 3: '))
				string4 = str(input('Enter string 4: '))
				
				print('String 1: {}\nString 2: {}\nString 3: {}\nString 4: {}'.format(string1, string2, string3, string4))
			
			else: 
				print('Selected card {} doesnot expect any strings\n'.format(card_type_t(card_type)))



Screen = screen_ui_t()
Screen.screen_type()
