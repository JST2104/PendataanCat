from os import system
from time import sleep
from datetime import datetime

def print_menu():
	system("cls")
	print("""
	Stock Paint Notes
	[1]. Add Paint
	[2]. Search Paint
	[3]. Update Paint
	[4]. Remove Paint
	[5]. Exit
		""")

def print_header(msg):
	system("cls")
	print(msg)

def not_empty(container):
	if len(container) != 0:
		return True
	else:
		return False

def verify_ans(char):
	if char.upper() == "Y":
		return True
	elif:
		return False

def print_data(id_contact=None, telp=True, hobi=True, all_data=False):
	if id_project != None and all_data == False:
		