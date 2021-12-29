####3 digit combination safe
import random ###to shuffle the guess list

combination = []
guess = [1,1,1]
guess_list=[]
accuracy = None
show = None

def welcome():
	print("\n\n\n*****Welcome safecracker*****")
	print("In this program you will set a three digit combination lock")
	print("and the computer will guess the combination.")
	input("\nAre you ready? Press Enter to continue...")

def set_combo():
	global accuracy
	global combination
	while accuracy != 1 and accuracy != 5:
		print("\n\nHow precise would you like to test?")
		accuracy = int(input("Enter 1 or 5: "))
		print("\nNext we need to set the combination for the computer to guess.")
		input("Press Enter to continue...\n")

		if accuracy == 1:
			first_digit = int(input("First Digit:  Pick a number between 0 and 99  "))
			second_digit = int(input("Second Digit: Pick a number between 0 and 99  "))
			third_digit = int(input("Third Digit:  Pick a number between 0 and 99  "))
		elif accuracy == 5:
			first_digit = int(input("First Digit:  Pick a multiple of 5 between 0 and 95  "))
			second_digit = int(input("Second Digit: Pick a multiple of 5 between 0 and 95  "))
			third_digit = int(input("Third Digit:  Pick a multiple of 5 between 0 and 95  "))

		else:
			pass
	combination.append(first_digit)
	combination.append(second_digit)
	combination.append(third_digit)

def gen_guess_lst():
	for a in range(0,100, accuracy):
		guess[0] = a
		for b in range(0,100,accuracy):
			guess[1] = b 
			for c in range(0,100,accuracy):
				guess[2] = c 
				#print(f"guess{guess}")
				guess_list.append((a,b,c))
	print(f"{len(guess_list)} possible comboations")
	random.shuffle(guess_list)

def shows():
	global show
	userin = input("Do you want to the computer to show each guess? yes or no: ")
	if userin.lower() == 'yes' or userin.lower() == 'y':
		show = True
	elif userin.lower() == 'no' or userin.lower() == 'n':
		show = False

def bruteforce():
	global guess
	for i in range(1,len(guess_list)+1):
		if guess_list[i][0] == combination[0] and guess_list[i][1] == combination[1] and guess_list[i][2] == combination[2] :
			print("*********************************************************")
			print(f"Combination is {combination} and guess is {guess_list[i]}")
			print("*********************************************************")
			break
		else:
			if show == True:
				print(f"Attempt: {i} guess: {guess_list[i]}")
				pass
			else:
				pass
				

welcome()
set_combo()
gen_guess_lst()
shows()
bruteforce()


