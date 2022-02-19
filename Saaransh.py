import os


print("\n\t\t\t\t\b\b\b-----!! Saaransh !!-----\n")


while True:
	print(""" 
	Option 01: Read About Sessions 
	Option 02: Learn Linux Commands
	Option 03: Bonus Command
	Option 04: Run some Linux commands
	Option 05: Exit
	""")

	choice = int(input("Enter Your Choice: "))

	if choice == 1:
		print("""
		Option-01: About Session-1
		Option-02: About Session-2		
		Option-03: About Session-3
		Option-04: About Session-4
		Option-05: About Session-5
		Option-06: About Session-6
		Option-07: About Session-7
		Option-08: About Session-8
		Option-09: About Session-9
		Option-10: About Session-10
		Option-11: About Session-11
		Option-12: About Session-12
		Option-13: About Session-13
		Option-14: About Session-14
		Option-0: Exit
		""")
		while True:		
			choice = int(input("Enter your choice: "))
			if choice  == 1:
				session=os.system("cat sessions/session-1")
				print("\n")
			elif choice  == 2:
				session=os.system("cat sessions/session-2")
				print("\n")
			elif choice  == 3:
				session=os.system("cat sessions/session-3")
				print("\n")
			elif choice  == 4:
				session=os.system("cat sessions/session-4")
				print("\n")
			elif choice  == 5:
				session=os.system("cat sessions/session-5")
				print("\n")
			elif choice  == 6:
				session=os.system("cat sessions/session-6")
				print("\n")
			elif choice  == 7:
				session=os.system("cat sessions/session-7")
				print("\n")
			elif choice  == 8:
				session=os.system("cat sessions/session-8")
				print("\n")
			elif choice  == 9:
				session=os.system("cat sessions/session-9")
				print("\n")
			elif choice  == 10:
				session=os.system("cat sessions/session-10")
				print("\n")
			elif choice  == 11:
				session=os.system("cat sessions/session-11")
				print("\n")
			elif choice  == 12:
				session=os.system("cat sessions/session-12")
				print("\n")
			elif choice  == 13:
				session=os.system("cat sessions/session-13")
				print("\n")
			elif choice  == 14:
				session=os.system("cat sessions/session-14")
				print("\n")
			elif choice  == 0:
				exit=os.system("exit")
				print("Exiting Your Sessions ...")
				break
			else :
				print(" Invalid Option ....\n Please Try Again!!\n")
	elif choice == 2:
		command = os.system("cat commands.txt")
	elif choice == 3:
		bonus_command = os.system("cat bonus_command.txt")
	elif choice == 4:
		while True:
			print("""Which command do you wanna run\nPlease Enter your option...\n
			Option-01: Show current date
			Option-02: show current month's Calender		
			Option-03: If you want continuously time
			Option-04: To check my IP
			Option-05: To open new Terminal
			Option-06: Open firefox
			Option-07: check user
			Option-08: Create File
			Option-09: Create Folder
			Option- 0: Exit
			""")
			choice = int(input("Enter your choice: "))
			if choice == 1:
				date = os.system("date")
				print(date)
			elif choice == 2:
				cal = os.system("cal")
				print(cal)
			elif choice == 3:
				ip = os.system("bash garuda")
				print(ip)
			elif choice == 4:
				ip = os.system("ifconfig")
				print(ip)
			elif choice == 5:
				terminal = os.system("gnome-terminal")
				print(terminal)
			elif choice == 6:
				browser = os.system("firefox")
				print(browser)
			elif choice == 7:
				user = os.system("whoami")
				print(user)
			elif choice == 8:
				create_file =os.system("gedit NewFile")
			elif choice == 9:
				create_folder =os.system("mkdir NewFolder")
			elif choice == 0:
				exit = os.system("exit")
				print(exit)
				print("Exiting Your Linux Commands ...")
				break	
			else :
				print(" Invalid Option ....\n Please Try Again!!\n")
	elif choice == 5:
		exit = os.system("exit")
		print("Exiting Your Entire Program ...")
		break
	
	else :
		print(" Invalid Option ....\n Please Try Again!!\n")
