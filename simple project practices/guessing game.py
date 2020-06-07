import random
print("do you want play the game? type yes or no")

def guess():
	while entryconfirm=="yes":
		answer=random.randint(1,100)
		try_number=int(input("guess a number between 1 and 100"))
		counter=1
		while try_number != answer:
			if try_number> answer:
				print("Your number is too large, try again!")
				counter = counter + 1

				try_number = int(input("guess a number between 1 and Entered Number"))

			elif try_number<answer:
				print("your number is too small, try again!")
				counter = counter + 1

				try_number = int(input("guess a number between Entered Number and 100"))
			if try_number==answer:
				print('you won the game')
			if counter==4:
				print("sorry you lost, you tried 3 times")
				break;
		break;
entryconfirm=input("")
guess()
entryconfirm=input("continue?")
if entryconfirm=="yes":
	guess()