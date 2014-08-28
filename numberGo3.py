# coding: utf-8
import os
import random
import getpass

limit = 10
minimum = 1
maximum = 100

def checker(ZahlStr):
	Zahl = 0
	if ZahlStr.isdigit():
		Zahl = int(ZahlStr)
	else:
		return False

	if Zahl < minimum:
		return False
	elif Zahl > maximum:
		return False
	else:
		return True

def human1Input():
	secretInteger = 5
	while True:

		secretString = getpass.getpass('Bitte geben sie die geheime Zahl ein: ')

		if checker(secretString) == False:
			print "Your input wasn't valid"
			print ''
		else:
			secretInteger = int(secretString)
			return secretInteger

def human1Random():
	randomInteger = random.randint(minimum,maximum)
	return randomInteger

def human2Input():
	while True:
		secretString = raw_input('Bitte versuchen sie die geheime Zahl zu raten: ')

		if checker(secretString) == False:
			print "Your input wasn't valid"
			print ''
		else:
			secretInteger = int(secretString)
			return secretInteger

def compare(human1Integer,human2Integer):
	if human1Integer < human2Integer:
		print 'Your answer was too big'
		return False

	elif human1Integer > human2Integer:
		print 'Your answer was too low'
		return False

	elif human1Integer == human2Integer:
		print 'Your answer was correct'
		return True

def loadHighScore():
	f1 = open("highscore.csv","r")
	content = f1.read()
	f1.close()
	highScore = {}
	lines = content.split('\n')
	for line in lines:
		if line[0] != '#':
			tmpEntry = line.split(';')
			name = tmpEntry[0]
			wins = tmpEntry[1]
			games = tmpEntry[2]
			percentage = tmpEntry[3]
			rank = tmpEntry[4]
			highScore[name] = [wins,games,percentage,rank]
	return highScore

def saveHighScore(highScore):
	content = '#name;wins;games;percentage;rank'
	for user in highScore:
		values = highScore[user]
		wins = values[0]
		games = values[1]
		percentage = values[2]
		rank = values[3]
		tmpRow = '\n' + user + ';' + wins + ';' + games + ';' + percentage + ';' + rank
		content += tmpRow
	f1 = open('highscore.csv','w')
	f1.write(content)
	f1.close()

def editHighScore(highScore,name,wins,games,rank):
	tmpEntry = highScore[name]
	newEntry = [0,0,0,0]
	newEntry[0] = str(int(tmpEntry[0]) + int(wins))
	newEntry[1] = str(int(tmpEntry[1]) + int(games))
	tmpPercentage = int(float(newEntry[0])/float(newEntry[1]) * 100)
	newEntry[2] = str(tmpPercentage)
	newEntry[3] = str(rank)
	highScore[name] = newEntry
	return highScore

def createNewUser(highScore,name,wins,games,rank):
	tmpEntry = [0,0,0,0]
	tmpEntry[0] = str(wins)
	tmpEntry[1] = str(games)
	tmpPercentage = int(float(tmpEntry[0])/float(tmpEntry[1]) * 100)
	tmpEntry[2] = str(tmpPercentage)
	tmpEntry[3] = str(rank)
	highScore[name] = tmpEntry
	return highScore

def printHighScore(highScore):
	print 'Name:'.ljust(16) + '| ' + 'wins:'.ljust(5) + ' | ' + 'games:'.ljust(6) + ' | ' + 'percentage: '.ljust(12) + ' | ' + 'rank:'.ljust(5) + '|'
	for user in highScore:
		entry = highScore[user]
		print user.ljust(15) + ' | ' + entry[0].ljust(5) + ' | ' + entry[1].ljust(6) + ' | ' + entry[2].ljust(12) + ' | ' + entry[3].ljust(5) + '|'


scoreh1 = 0
scoreh2 = 0
running = True

human1Func = human1Random

print '1: 1 Player'
print '2: 2 Player'
choice = raw_input('Mit wie vielen Spielern möchtest du spielen: ')
if choice == '1':
	human1Func = human1Random
elif choice == '2':
	human1Func = human1Input

os.system('clear')

while running == True:

	if choice == '1':
		print 'KI Score: '.ljust(20) + str(scoreh1)
	elif choice == '2':
		print 'Human 1 Score: '.ljust(20) + str(scoreh1)

	print 'Human 2 Score: '.ljust(20) + str(scoreh2)
	print 'Limit:'.ljust(20) + str(limit)
	print 'Minimum:'.ljust(20) + str(minimum)
	print 'Maximum:'.ljust(20) + str(maximum)
	print 50*'-'
	print ''

	h1Input = human1Func()
	tryCounter = 0

	while tryCounter != limit:

		h2Input = human2Input()

		result = compare(h1Input, h2Input)

		if result == True:
			break

		else:
			tryCounter += 1
			print 'You now have ' + str(limit-tryCounter) + ' tries'

		print 50 * '-'
		print ''

	if result == True:
		scoreh2 += 1

	elif result == False:
		scoreh1 += 1
		print 'The right answer would be: ' + str(h1Input)
		print 50*'-'

	print ''
	continueInput = raw_input('Press Enter to continue or q to exit: ')
	os.system('clear')

	if continueInput == 'q':
		running = False

highScore = loadHighScore()

username = raw_input('Bitte geben sie ihren Namen ein: ')
print 50*'-'
wins = str(scoreh2)
games = str(scoreh1 + scoreh2)
rank = random.randint(0,100)

if username in highScore:
	highScore = editHighScore(highScore,username,wins,games,rank)
else:
	highScore = createNewUser(highScore,username,wins,games,rank)

saveHighScore(highScore)
printHighScore(highScore)