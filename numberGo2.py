import os
import random
import getpass

def checker(ZahlStr):
	Zahl = 0
	if ZahlStr.isdigit():
		Zahl = int(ZahlStr)
	else:
		return False

	if Zahl < 1:
		return False
	elif Zahl > 10:
		return False
	else:
		return True

def human1Input():
	secretInteger = 5
	while True:

		secretString = getpass.getpass('Bitte geben sie die geheime Zahl ein: \n')

		if checker(secretString) == False:
			print "Your input wasn't valid"

		else:
			secretInteger = int(secretString)
			return secretInteger

def human1Random():
	randomInteger = random.randint(1,10)
	return randomInteger

def human2Input():
	while True:
		secretString = raw_input('Bitte versuchen sie die geheime Zahl zu raten: \n')

		if checker(secretString) == False:
			print "Your input wasn't valid"

		else:
			secretInteger = int(secretString)
			return secretInteger

def compare(human1Integer,human2Integer):
	if human1Integer < human2Integer:
		print 'Your integer was too big'
		return False

	elif human1Integer > human2Integer:
		print 'Your integer was too low'
		return False

	elif human1Integer == human2Integer:
		print 'Your integer was correct'
		return True

limit = 3
scoreh1 = 0
scoreh2 = 0
running = True

human1Func = human1Random

print '0: random integer'
print '1: input integer'
choice = raw_input('Entscheide, wie die Zahlen erstellt werden sollen: ')
if choice == '0':
	human1Func = human1Random
elif choice == '1':
	human1Func = human1Input

os.system('clear')

while running == True:

	print 'Human 1 Score: ' + str(scoreh1)
	print 'Human 2 Score: ' + str(scoreh2)

	h1Input = human1Func()
	tryCounter = 0

	while tryCounter != limit:

		h2Input = human2Input()

		result = compare(h1Input, h2Input)

		if result == True:
			break

		else:
			tryCounter += 1


	if result == True:
		scoreh2 += 1

	elif result == False:
		scoreh1 += 1

	continueInput = raw_input('Press Enter to continue or q to exit: ')
	os.system('clear')

	if continueInput == 'q':
		running = False
