# Python TExt RPG
# Name here xD

import cmd
import wrap
import sys
import os
import time
import random

screen_width = 100

##### Player Setup #####
class Player:
	"""docstring for ClassName"""
	def __init__(self):
		self.name = ''
		self.job = ''
		self.hp = 0
		self.mp = 0
		self.status_effects = []
		self.location = 'b2'
		self.game_over = False
myPlayer = Player()

##### Title Screen	 #####
def title_screen_selections():
	option = input("> ")
	if option.lower() == ("play"):
		setup_game() # placeholder until written
	elif option.lower() == ("help"):
		help_menu()
	elif option.lower() == ("quit"):
		sys.exit()
	while option.lower() not in ['play', 'help', 'quit']:
		print("Plese Enter a valid command.")
		option = input("> ")
		if option.lower() == ("play"):
			setup_game() # placeholder until written
		elif option.lower() == ("help"):
			help_menu()
		elif option.lower() == ("quit"):
			sys.exit()

def title_screen():
	os.system('clear')
	print('##########################')
	print('# Welcome to the Text RPG!')
	print('##########################')
	print('          -Play-          ')
	print('          -help-          ')
	print('          -Quit-          ')
	print(' Copyright 2018 @Nasir.me ')
	title_screen_selections()

def help_menu():
	print('##########################')
	print('# Welcome to the Text RPG!')
	print('##########################')
	print('-Use up, down, left, right to move')
	print('-Type your commands to do them')
	print('- Use "look" to inspect something')
	print(' - Good luck and have fun!')
	print(' Copyright 2018 @Nasir.me ')
	title_screen_selections()




##### MAP #####


# a1 a2... # PLAYER STARTS AT b2 x
#-------------
#|  |  |  |  | a4
#-------------
#|  | x|  |  | b4 ...
#-------------
#|  |  |  |  | 
#-------------
#|  |  |  |  |
#-------------



ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False,'a1': False, 'a2': False,
	         		'b1': False, 'b2': False,'b1': False, 'b2': False,
	         		'c1': False, 'c2': False,'c1': False, 'c2': False,
	         		'd1': False, 'd2': False,'d1': False, 'd2': False,
	         		}

zonemap = {
	'a1': {
		 ZONENAME:'ATOWN',
		 DESCRIPTION:'description',
		 EXAMINATION:'examine',
		 SOLVED:False,
		 UP:'',
		 DOWN:'b1',
		 LEFT:'',
		 RIGHT: 'a2',
		},
	'a2': {
		 ZONENAME: 'city Entrance',
		 DESCRIPTION: 'description',
		 EXAMINATION: 'examine',
		 SOLVED: False,
		 UP: '',
		 DOWN:'b2',
		 LEFT:'a1',
		 RIGHT:'a3',
		},
	'a3': {
		 ZONENAME: 'Downtown',
		 DESCRIPTION: 'description',
		 EXAMINATION: 'examine',
		 SOLVED: False,
		 UP: '',
		 DOWN: 'b3',
		 LEFT: 'a2',
		 RIGHT: 'a4',	
		},
	'a4': {
		 ZONENAME:'FivePoints',
		 DESCRIPTION: 'description',
		 EXAMINATION: 'examine',
		 SOLVED: False,
		 UP: '',
		 DOWN:'b4',
		 LEFT: 'a3',
		 RIGHT:'',	
		},
	'b1': {
		 ZONENAME: '',
		 DESCRIPTION: 'description',
		 EXAMINATION: 'examine',
		 SOLVED: False,
		 UP: 'a1',
		 DOWN: 'c1',
		 LEFT: '',
		 RIGHT: 'b2',
		},
	'b2': {
		 ZONENAME: 'Home',
		 DESCRIPTION:'this is your home',
		 EXAMINATION: 'home is the same as always - nothing has change',
		 SOLVED: False,
		 UP: 'a2',
		 DOWN: 'c2',
		 LEFT:'b1',
		 RIGHT: 'b3',	
		},

	}

##### GAME INTERACTIVITY ######
def print_location():
	print('\n' + ('#' * (4 + len(myPlayer.location))))
	print('#' + myPlayer.location.upper() + '#')
	print('#' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
	print('\n' + ('#'* (4 + len(myPlayer.location))))
def prompt():
	print("\n" + "==============================")
	print("what would you like to do?")
	action = input("> ")
	acceptable_action = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
	while action.lower() not in acceptable_action:
		print('Unknown action, try again.\n')
		action = input("> ")
	if action.lower() == 'quit':
		sys.exit()
	elif action.lower() in ['move', 'go', 'travel', 'walk']:
		player_move(action.lower())
	elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
		player_examine(action.lower())
 #### HANDLE PLAYER #####
def player_move(myAction):
	ask = "where would you like to move to?\n"
	dest = input(ask)
	if dest in ['up', 'north']:
		destination = zonemap[myPlayer.location][UP]
		movement_handler(destination)
	elif dest in ['left', 'west']:
		destination = zonemap[myPlayer.location][LEFT]
		movement_handler(destination)
	elif dest in ['right', 'east']:
		destination = zonemap[myPlayer.location][RIGHT]
		movement_handler(destination)
	elif dest in ['south', 'down']:
		destination = zonemap[myPlayer.location][DOWN]
		movement_handler(destination)

def movement_handler(destination):
	print("\n" + "You have moved to the " + destination + ".")
	myPlayer.location = destination
	print_location()
	
def player_examine(action):
	if zonemap[myPlayer.location][SOLVED]:
		print("you have already exhausted this zone.")
	else:
		print("you can trigger pizzle here.")
##### GAME FUNTIONLITY #####


def main_game_loop():
	while myPlayer.game_over is False:
		prompt()
	# here handle if u have solved the game and beat it XD.etc

def setup_game():
	os.system('clear')
# PLAYER NAMING
	question1 = "Hello, what's your name\n"
	for character in question1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	player_name = input("> ")
	myPlayer.name = player_name

	question2 = "So, what's what role do you want to play?\n"
	question2added =  "(You can play as 'warrior', 'mage', 'healer')\n"
	for character in question2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in question2added:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)
	player_job = input("> ")
	valid_jobs = ['warrior', 'mage', 'healer']
	if player_job.lower() in valid_jobs:
		myPlayer.job = player_job
		print("You are now a" + player_job + "!\n")
		while player_job.lower() not in valid_jobs:
			player_job = input("> ")
			if player_job.lower() in valid_jobs:
				myPlayer.job = player_job
				print("You are now a "+ player_job + '!\n')

			##### PLAYER STATS #####  
	if myPlayer.job is 'warrior':
		self.hp = 150
		self.mp = 30
	elif myPlayer.job is 'mage':
		self.hp = 90
		self.mp = 120
	elif myPlayer.job is 'healer':
		self.hp = 90
		self.mp = 90


	### INTRO ###
	question3 = "Welcome, " + player_name + " the " + player_job + "\n"
	for character in question3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)

	speech1 = "Welcome to this fantesy world\n"
	speech2 = "I hope it greets you well\n"
	speech3 = "just make sure you don't get too lost...\n"
	speech4 = "heheheh...\n"
	for character in speech1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in speech2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.04)
	for character in speech3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.03)
	for character in speech4:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)

	os.system('clear')
	print('###################')
	print('# Lets start now! #')
	print('###################')
	main_game_loop()








title_screen()
