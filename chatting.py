import os

name = input("Type Your Name: ")
while True:
	print("""\n\n\aWhat do you wanna Show ...\n
			01: Show current date
			02: show current month's Calender		
			03: show continuously time
			04: check my IP
			05: open new Terminal
			06: open firefox
			07: check user
			08: open file explorer
			09: Speak 
			10: show background process
			11: check internet connection
			12: clear terminal
			13: exit to terminal 
			00: Exit to program
			""")
	
	user_input= input("What can i do for you :- ")
	
	if ("exit" in user_input) or ("E" in user_input):
		print("\aexiting ...")
		exit=os.system("exit")
		break

	elif (("run" in user_input) or ("show" in user_input)) and (("Date" in user_input) or ("date" in user_input)):
		date=os.system("date")
		print(date)

	elif (("open" in user_input) or ("show" in user_input)) and (("calender" in user_input) or ("Calender" in user_input)):
		cal=os.system("cal")
		print(cal)

	elif (("continuously" in user_input) or ("run" in user_input) or ("current" in user_input) or ("show" in user_input)) and (("time" in user_input)):
		garuda=os.system("bash garuda")
		print(garuda)

	elif (("run" in user_input) or ("open" in user_input) or ("show" in user_input)) and (("firefox" in user_input) or ("browser" in user_input)):
		browser=os.system("firefox")
		print(browser)

	elif ("check" in user_input) and ("user" in user_input):
		user=os.system("whoami")
		print(user)

	elif (("open" in user_input) or ("start" in user_input)) and (("terminal" in user_input) or ("command line" in user_input)):
		terminal=os.system("gnome-terminal")
		print(terminal)

	elif (("check" in user_input) or ("show" in user_input)) and (("ip" in user_input) or ("ip address" in user_input)):
		ip=os.system("ifconfig")
		print(ip)
	
	elif (("open" in user_input) or ("show" in user_input)) and (("file explorer" in user_input) or ("linux explorer" in user_input)):
		file_ex=os.system("nautilus")
		print(file_ex)
	
	elif ("speak" in user_input):
		print(name)
		#update_name=os.system("cat>your_name.sh")
		speak = os.system("bash your_name.sh")
		print(speak) 

	elif (("open" in user_input) or ("show" in user_input)) and (("background process" in user_input)):
		bg=os.system("top")
		print(bg)

	elif ("check" in user_input) and ("connection" in user_input):
		con=os.system("ping google.com")
		print(con)

	elif ("clear" in user_input) and ("terminal" in user_input):
		clear=os.system("clear")
		print(clear)

	elif ("exit" in user_input) and ("terminal" in user_input):
		exit=os.system("exit")
		print(exit)
		
	else:
		print("Wrong Input...")

print("Welcome Again !! ",name)
