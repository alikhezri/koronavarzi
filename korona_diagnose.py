KORONA_TEMPRETURE = 37.5

temp = int(input("Enter Your Body Tempreture: "))

def tab_sanj():
	if temp < KORONA_TEMPRETURE:
		print("You are in safe range")
	else:
		print("Danger! Visit a doctor")


if __name__ =' __main__':
	tab_sanj()
