KORONA_TEMPRETURE = 37.5

temp = int(input("Enter Your Body Tempreture: "))

def tab_sanj():
	try:
		if temp < KORONA_TEMPRETURE:
			print("You are in safe range.")
		else:
			print("Danger! Visit a docter.")
	except ValueError:
		print("Wrong value entered. Try again later.")


if __name__ ==' __main__':
	while:
		item = input("Select from items('tabsanj', 'exit'): ")
		if item == 'tabsanj':
			tab_sanj()
		elif item == 'exit':
			break
		else:
			print("Wrong item selected. Please enter a correct one!")
