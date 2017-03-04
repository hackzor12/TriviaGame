import re

def CheckStr(i):
	#This function checks to see if the inupt is an integer
	try:
		val = str(i)
	except ValueError:
		#It returns an enumeration of 1 if the check fails
		return 1
	return 0

def CheckInput(s):
	#This function checks to see if the difficulty is easy, medium or hard
	possible_difficulty = ["easy","medium","hard"]
	for diff in possible_difficulty:
		if str(s) == diff:
			return 0
			#It returns an enumeration of 2 if the check fails
	return 2

def Validate(value, varType):
	#This function verifies that user input is valid
	#The purpose of VarType is to allow future validation cases for different types of user input
	enum = 0
	if varType == "difficulty":
		enum = CheckStr(value)
		if enum == 0:
			enum = CheckInput(value)
		return enum	

def GetDifficulty():
	#Enums contains the error output for different validation enumerations
	enum = 0 
	enums = [" Input Looks Good!"," Must be a string"," Value must be easy, medium or hard"]

	#Ask the user to input the number of questions they would like to answer
	difficulty = raw_input("Input the difficulty level as a string (easy,medium,hard):")
	enum = Validate(difficulty,"difficulty")
	#Make sure the input is valid
	while enum != 0:
		print "Please try again your input has following error:" + str(enums[enum])
		difficulty = raw_input("Input the number of levels you would like to play, it must be greater than 0 and less than "+str()+":")
		enum = Validate(difficulty,"difficulty")
	#Return the user input
	if difficulty == "easy":
		return 1
	elif difficulty == "medium":
		return 2
	else: 
		return 3
	
def main():
	#Variables containing the games questions, answers, and a variable to store the users answer
	questions = [["Level 1 Maths","2 + 2 = _", "3 x 4 = _","55 / 11 = _ ","662 + 4 = _"],["Level 2 Trivia","_ is the last name of the current president?","_ Texas is the live music capital of the world!","_ is the year the USA first when to the moon.","_ kilometers per second is the speed of light."],["Level 3 Movies","The Dude was the main character in  'The Big _'","The 1980's movie _ popularized the term: 'It's time to kick ass and chew bubble gum but I am all out of gum.","_ direceted Grindhouse/Planet Terror?","The Dude _!"]]
	answers = [["4","12","5","666"],["Trump","Austin","1969","299,792"],["Lebowski","They Live","Robert Rodriguez", "Abides"]]
	answer = ""
	#Get the Number of Rounds the user wants to play
	difficulty = GetDifficulty()
	#Iterate through the number of questions they want to answer
	for i in range(0,difficulty):
		print questions[i][0]
		for x in range(1,len(questions[i])):
			print questions[i][x]
			answer = str(raw_input("Answer the question using a valid string then press enter:"))
			#If they get it wrong keep pestering them until they get it right
			while (answer != answers[i][x-1]):
				answer = str(raw_input("You got it wrong try again!:"))
			print re.sub('[_*]',answers[i][x-1],questions[i][x])
	#Wow they won the game how neat.
	print "Wow you're a real winner!"
main()

