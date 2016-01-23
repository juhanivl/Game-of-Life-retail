#Game of Life Version 0.01 Last Edited: 30.9. 11:09

from tkinter import *
import mysql.connector
import random


gui = Tk()
gui.resizable(0,0)
gui.title("Game of Life")

intro = "Welcome to Game of Life! \nFeeling lost? Try clicking that Help-thingie up there. \nType start to begin your journey."

db = mysql.connector.connect(host="localhost", user="dbuser7", passwd="dbpass", db="gameoflife")
#***********************OBJECTS***************************
action="" #First word of the player input is stored here
target="" #Last word of the player input is stored here

#Create global variables
global playerX                  #Global variable to store player's X coordinate
global playerY                  #Global variable to store player's Y coordinate
global bounds                   #Global variable to store available movement options for each room, fetched  from database.
global swings
global bullyKicked
global fredCalled
#Assigning values for global variables
bounds = ""
playerX = 0
playerX = str(playerX)
playerY = -1
playerY = str(playerY)
swings = 0
bullyKicked = 0
fredCalled = 0

	#*******Menu*******
def Help():
	printText("Move around with these easy-to-use commands: FORWARD, BACK, RIGHT and LEFT \nTo take things in your own hands, simply type: PICK <OBJECT> \n Want to refresh your memory? You might want to LOOK AROUND.\nUse 1 or 2 to choose dialogues when needed.\n Keep your eyes peeled for special commands!")
def About():
	printText("Copyright Team Lucky Seven 2014. All rights reserved.")
def Quit():
	gui.quit()
	sys.exit()

	#******Game Objects*******
def controller(action, target):
	global playerX
	global playerY
	global bullyKicked
	global fredCalled
	cur = db.cursor()
	if "start" in action and playerX == "0" and playerY == "-1":
		printText("Game starting...")
		text.after(3000, welcomeScreen)
	elif "right" in action and playerX == "22" and playerY == "0":
		printText(END, "The city is a scary place. You don't want to go there.")
	elif "left" in action and playerX == "22" and playerY == "0":
		printText(END, "School is for big kids. You can't make yourself older even if you wanted to.")
	elif "1" in action or "2" in action:
		dialogueManager(playerX, playerY, action)
	elif playerX=="144" and playerY=="0":
		baseballSimulatorGood(action, target)
	elif playerX=="143" and playerY=="3":
		pitchSimulatorGood(action, target)
	elif playerX=="244" and playerY=="0":
		baseballSimulatorBad(action, target)
	elif playerX=="243" and playerY=="3":
		pitchSimulatorBad(action, target)
	elif playerX=="155" and playerY=="2" and "save" in action and "fred" in target:
		cur.execute("UPDATE descriptions SET description='Jack: Turds looking after each other. Isn’t that cute.\nFred looks like he´s about to do something stupid soon. You better just leave.' WHERE roomX=155 AND roomY=2")
		getDescription(playerX, playerY)
	elif playerX=="155" and playerY=="2" and "leave" in action: # Fin path leave
		playerY="3"
		getDescription(playerX, playerY)
	elif "kiss" in action and playerX=="254" and playerY=="4": #April kiss scene
		printText("Kiss who?")
	elif "kiss" in action and "april" in target and playerX=="254" and playerY=="4":
		cur.execute("UPDATE descriptions SET description='Perfect kiss!\nApril looks you deep in the eyes and blushes.\nApril: I really like your lips...\n\n\n(PRESS ENTER WHEN READY TO MOVE ON)' WHERE roomX=254 and roomY=4")
		getDescription(playerX, playerY)
	elif "enterwaspressed" in action and playerX=="254" and playerY=="4":
		goToChapter6Worst()
	elif "kiss" in action and playerX=="155" and playerY=="4":
		printText("Kiss who?")
	elif "kiss" in action and "april" and playerX=="155" and playerY=="4":
		cur.execute("UPDATE descriptions SET description='Perfect kiss!\nApril looks at you with her sparkling green eyes and blushes.\nApril: I really like your lips...\n You spend a long time with April before going home.\n\n\n(PRESS ENTER WHEN READY TO MOVE ON)' WHERE roomX=155 and roomY=4")
		getDescription(playerX, playerY)
	elif "enterwaspressed" in action and playerX=="155" and playerY=="4":
		goToChapter6Good()
	elif playerX=="167" and playerY=="0" and "call" in action and "client" in target: #Call client in Chapter6 (good)
		cur.execute("UPDATE descriptions SET description='You see your house in the distance. You can barely see April through a kitchen window and she’s with someone. Who could it be?' WHERE roomX=166 AND roomY=0")
		cur.execute("UPDATE descriptions SET description='You: “Hello this is Lucky Ltd. How well is your business´s database protected?\nMan on the phone: Well, now that you mentioned it…\nYou work at the office through all day and you mange to close the deal. You and Fred feel proud of your success. But enough is enough. Time to go home – April has been telling you not to stay late at work. Luckily the bus arrives on the stop just on your left.' WHERE roomX=167 AND roomY=0")
		cur.execute("UPDATE rooms SET exitWest=TRUE WHERE roomX=167 AND roomY=0")
		cur.execute("UPDATE rooms SET exitNorth=TRUE WHERE roomX=166 AND roomY=0")
		getDescription(playerX, playerY)
	elif playerX=="166" and playerY=="3" and "kick" in action and "jack" in target: #Kick Jack out
		cur.execute("UPDATE descriptions SET description='Hopefully that’s the last time you’ll see Jack and you get to live your life without him. At least you and April are happy and you got a true Friend – Fred.\n\n(PRESS ENTER TO MOVE ON)' WHERE roomX=166 AND roomY=3")
		getDescription(playerX, playerY)
		bullyKicked=1
	elif "enterwaspressed" in action and playerX=="166" and playerY=="3" and bullyKicked==1:
		goToChapter7Good()
	elif playerX=="266" and playerY=="3" and "kick" in action and "jack" in target:
		cur.execute("UPDATE descriptions SET description='You kick Jack out, but nothing is the same anymore. Everything is falling a part around you. Can you ever trust anyone again?\n\n(PRESS ENTER TO MOVE ON)' WHERE roomX=266 AND roomY=3")
		getDescription(playerX, playerY)
		bullyKicked=1
	elif "enterwaspressed" in action and playerX=="266" and playerY=="3" and bullyKicked==1:
		goToChapter7Worst()
	elif playerX=="367" and playerY=="0" and "left" in action:
		playerX="366"
		playerY="1"
		getDescription(playerX, playerY)
	elif "enterwaspressed" in action and playerX=="23" and playerY=="2":
		goToChapter3Good()
	elif "left" in action in action and playerX=="22" and playerY=="2":
		Movement(action)
	elif "enterwaspressed" in action and playerX=="21" and playerY=="2":
		goToChapter3Bad()
	elif "enterwaspressed" in action and playerX=="134" and playerY=="1":
		goToChapter4Good()
	elif "enterwaspressed" in action and playerX=="234" and playerY=="1":
		goToChapter4Bad()
	elif "call" in action and "fred" in target and playerX=="177" and playerY=="0": #Call Fred in Chapter7 (good)
		cur.execute("UPDATE descriptions SET description='Fred: Hello, my old friend! I was just thinking of you. We used to have so much fun back in times - I´m so thankful that you stood by me.\nYou: Of course old pal.\nFred: You were the only friend I had. I don´t know how I would have managed to live life alone with Jack chasing me all the time. But eventually all turned good and I am really happy with the life I have - kids, wife and so on. I haven´t seen Jack in years, though. I wonder if he still is such a badass, or maybe he has settled.\nHmmm... Maybe you should give Jack a call.' WHERE roomX=177 AND roomY=0")
		getDescription(playerX, playerY)
		fredCalled=1
	elif "call" in action and "jack" in target and playerX=="177" and playerY=="0" and fredCalled==1: #Call Jack in Chapter7 (good)
		cur.execute("UPDATE descriptions SET description='Jack: Hey is that really you? So nice to hear about you after such a long time! We used to have some real conflicts, haha. I was such a fool for making fun of you and Fred. And I´m so ashamed of the things I tried to do with April. I was really drunk at the time. I just realized it later, and I haven’t been man enough to apologize you…\nYou: I forgive you, though I’m not that sure about Fred.\nJack: Thank you, thank you so much. At least now I have some peace from my conscience.\nYou end the call after a while. You feel some pity for Jack. He had to spend his life all alone after all, and he really never got any decent job. You are happy you never got tangled in his messes by making friends with him. Some people are just really toxic for you...\n(PRESS ENTER WHEN READY TO MOVE ON)' WHERE roomX=177 AND roomY=0")
		getDescription(playerX, playerY)
		playerY="1"
	elif "call" in action and "jack" in target and playerX=="377" and playerY=="0": #Call Jack in Chapter7 (bad)
		cur.execute("UPDATE descriptions SET description='Jack: Hello, you ol´ bugger ball! I was just thinking of you. We used to have so much fun back in times - but you know, I´ve been regretting some of the stuff we did.\nThis makes you think too. How is Fred doing nowadays? Maybe you should call him.' WHERE roomX=377 AND roomY=0")
		getDescription(playerX, playerY)
		fredCalled=1
	elif "call" in action and "fred" in target and playerX=="377" and playerY=="0" and fredCalled==1: #Call Fred in Chapter7 (bad)
		cur.execute("UPDATE descriptions SET description='Fred:	Is that really you? So nice to hear about you after such a long time! We used to have some real conflicts, haha. I’m sorry I fired you but you had it coming. Thank you though for giving me some hard lessons in life, which helped me move forward!\nYou: I hope you can forgive me... Have you seen April since high school?\nFred: Oh, you haven’t heard yet? We´ve been married now for over a decade! I realized the love of my life had been right in front of my eyes for as long as I can remember. Sorry, I must go now. The kids are keeping us busy all the time! It was nice talking to you, bye! *Beeb*”\n(PRESS ENTER WHEN READY TO MOVE ON)' WHERE roomX=377 AND roomY=0")
		getDescription(playerX, playerY)
		playerY="1"
	elif "enterwaspressed" in action and playerX=="177" and playerY=="1": #Ending(good)
		Ending()
	elif "enterwaspressed" in action and playerX=="377" and playerY=="1": #Ending(bad)
		Ending()
	elif "enterwaspressed" in action and playerX=="277" and playerY=="0": #Ending(worst)
		Ending()
	elif "enterwaspressed" in action and playerX=="0" and playerY=="1": #goToChapter2
		goToChapter2()
	elif "bitch" in action:
		printText("This is not Breaking Bad and you are not Aaron Paul!")
	elif "quit" in action:
		printText("Nooooo! Please don't go yet! :( \nThere's even cake in the end! I promise! It's not a lie!\n\nBut if you really hate me so much, just select Quit from the File-menu...")
	else:
		inputManager(action, target)

def Parser(playerInput):                                   #Splits player input into words the program undestands, stored in action and target variables.
	playerInput = command.get()
	playerInput = playerInput.split()
	command.delete(0,END)
	
	if len(playerInput)<1:
		action = "enterwaspressed"
		controller(action, "")
	if len(playerInput)>=1:
		action = playerInput[0].lower()
		controller(action, "")
	else:
		action = ""
		
	if len(playerInput)>=2:
		action = playerInput[0].lower()
		target = playerInput[-1].lower()
		controller(action, target)
	else:
		target = ""
def printText(output):
	text.config(state=NORMAL)
	text.delete(1.0, END)
	text.insert(END, output)
	text.config(state=DISABLED)
def inputManager(action, target):               #Redirects the input to correct handler object.
	if "start" in action:
		printText("You already started the game dummy ;)")
	elif "forward" in action:
		Movement(action)
	elif "right" in action:
		Movement(action)
	elif "back" in action:
		Movement(action)
	elif "left" in action:
		Movement(action)
	elif "pick" in action:
		itemManagement(target)
	elif "look" in action and "around" in target:
		getDescription(playerX, playerY)
	elif "play" in action:
		specialEvents(action, target)
	elif "fuck" in action and "you" in target:
		printText("Well fuck you too!")
	elif "why" in action or "why?" in action:
		printText("Because reasons.")
	elif "go" in action:
		printText("PRO TIP: Use forward, left, etc. if you want to go/move/do something in that direction.")
	elif "enterwaspressed" in action:
		printText("PRO TIP: You must type the command in the input box before pressing enter.")
	else:
		printText("Umm... I didn't quite understand you.")

def Movement(action):                           #Handles player movement.
	global playerX
	global playerY
	global bounds
	getBounds(playerX, playerY)
	north = str(bounds[0][0])
	east = str(bounds[0][1])
	south = str(bounds[0][2])
	west = str(bounds[0][3])
	
	if "forward" in action:
		if "0" in north:
			printText("Why would you go there?")
		else:
			playerY = int(playerY)
			playerY = playerY+1
			playerY = str(playerY)
			getDescription(playerX, playerY)
	elif "right" in action:
		if "0" in east:
			printText("Why would you go there?")
		else:
			playerX = int(playerX)
			playerX = playerX+1
			playerX = str(playerX)
			getDescription(playerX, playerY)
	elif "back" in action:
		if "0" in south:
			printText("Why would you go there?")
		else:
			playerY = int(playerY)
			playerY = playerY-1
			playerY = str(playerY)
			getDescription(playerX, playerY)
	elif "left" in action:
		if "0" in west:
			printText("Why would you go there?")
		else:
			playerX = int(playerX)
			playerX = playerX-1
			playerX = str(playerX)
			getDescription(playerX, playerY)
	else:
		printText(END, "Umm... I didn't quite understand you.")
def itemManagement(target):
	cur = db.cursor()
	sql = "SELECT itemX, itemY, itemName, held FROM items WHERE itemX="+playerX+" AND itemY="+playerY
	cur.execute(sql)
	itemList = cur.fetchall()
	if len(itemList)>=1:
		itemX = itemList[0][0]
		itemY = itemList[0][1]
		itemName = itemList[0][2]
		itemHeld = itemList[0][3]
		print(itemX, itemY, itemName, itemHeld)
		if "teddy" in target or "teddybear" in target and itemHeld==0:
			cur.execute("UPDATE items SET held=TRUE WHERE itemID=0")
			cur.execute("UPDATE descriptions SET description='You see your mom looking at you with a loving smile on her face.\n Mom: Do you want to play with your teddy, honey?' WHERE roomX=0 AND roomY=1")
			printText("You pick up the teddy bear. Why don't you play with it for a while?")
		elif ("teddy" in target or "teddybear" in target) and itemHeld==1:
			printText("You try to pick up the teddy bear, but you soon realise that it's already in your hand.")
		else:
			printText("I only understood you as far as pick")
			
	else:
		printText("You don't see anything like it nearby to pick up")
def getDescription(playerX, playerY):      #Handles description fetching from database.
	cur = db.cursor()
	sql = "SELECT description FROM descriptions WHERE roomX="+playerX+" AND roomY="+playerY
	cur.execute(sql)
	description = cur.fetchall()
	printDescription(description[0][0])
	return description
def dialogueManager(playerX, playerY, action):
	cur = db.cursor()
	if "1" in action and playerX=="135" and playerY=="0": #Fin in classroom (Fin path)
	      cur.execute("UPDATE descriptions SET description='Fred: Yeah I guess you’re right. But I don’t like him at all.\nFred seems very nervous and you can almost see him tremble' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="135" and playerY=="0":
	      cur.execute("UPDATE descriptions SET description='Fred: I don´t know, he´s too big and probably just kick our asses even more' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="133" and playerY=="0": #Bully in classroom (Fin path)
	      cur.execute("UPDATE descriptions SET description='Jack: I have enough friends. What I don´t have a is a punching bag!' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="133" and playerY=="0":
	      cur.execute("UPDATE descriptions SET description='Jack: I heard we have baseball tomorrow. Hope you’re not a afraid of balls!' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="134" and playerY=="-1": #Red in classroom (Fin path)
		cur.execute("UPDATE descriptions SET description='April: I remember you! You were always with Fred and got beat up by Jack.\nThe teacher seem to be ready to start. Maybe you should turn forward and focus on the lesson.' WHERE roomX="+playerX+" AND roomY="+playerY)
		cur.execute("UPDATE rooms SET exitNorth=TRUE WHERE roomX=134 AND roomY=0")
		getDescription(playerX, playerY)
	elif "2" in action and playerX=="134" and playerY=="-1":
		cur.execute("UPDATE descriptions SET description='April: You wish. I bet I can throw further than you!' WHERE roomX="+playerX+" AND roomY="+playerY)
		cur.execute("UPDATE rooms SET exitNorth=TRUE WHERE roomX=134 AND roomY=0")
		getDescription(playerX, playerY)
	elif "1" in action and playerX=="235" and playerY=="0": #Fin in classroom (Bully path)
	      cur.execute("UPDATE descriptions SET description='Fred: Phew…' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="235" and playerY=="0":
	      cur.execute("UPDATE descriptions SET description='Fred: ...' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="233" and playerY=="0": #Bully in classroom (Bully path)
	      cur.execute("UPDATE descriptions SET description='Jack: We should have baseball everyday all the time if you ask me' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="233" and playerY=="0":
	      cur.execute("UPDATE descriptions SET description='Jack: Bugger balls? Haha! Good one!' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="234" and playerY=="-1": #Red in classroom (Bully path)
	      cur.execute("UPDATE descriptions SET description='April: Hi, I remember you. You always teased Fred with that jerk Jack!' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="234" and playerY=="-1":
	      cur.execute("UPDATE descriptions SET description='April: Don’t get cocky. I bet you can’t even throw a ball!' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="143" and playerY=="1": #Red in baseball field (Fin path)
	      cur.execute("UPDATE descriptions SET description='April: Yeah, I guess it’s alright.\nYou see Fred farther ahead. You should go cheer him.' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="143" and playerY=="1":
	      cur.execute("UPDATE descriptions SET description='April: Don’t make me laugh.\nYou see Fred farther ahead. You should go cheer him.' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="143" and playerY=="2": #Fred in baseball field (Fin path)
	      cur.execute("UPDATE descriptions SET description='Fred: I´ll try my best!\nYou remember it´s your turn to pitch! Maybe you should hurry forwards and continue playing.' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="143" and playerY=="2":
	      cur.execute("UPDATE descriptions SET description='Fred: O-o-okay. I´ll try.\nYou remember it´s your turn to pitch! Maybe you should hurry forwards and continue playing.' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="243" and playerY=="1": #Red in baseball field (Jack path)
	      cur.execute("UPDATE descriptions SET description='April: Yeah, I guess it’s alright.\nYou see Jack farther ahead. You should go cheer him.' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="243" and playerY=="1":
	      cur.execute("UPDATE descriptions SET description='April: Don’t make me laugh.\nYou see Jack farther ahead. You should go cheer him.' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="243" and playerY=="2": #Jack in baseball field (Jack path)
	      cur.execute("UPDATE descriptions SET description='Jack: I know I´m the best!\nYou remember it´s your turn to pitch! Maybe you should hurry forwards and continue playing.' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="243" and playerY=="2":
	      cur.execute("UPDATE descriptions SET description='Jack: I´m the man!\nYou remember it´s your turn to pitch! Maybe you should hurry forwards and continue playing.' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="154" and playerY=="0": #Bully in party (Fin path)
	      cur.execute("UPDATE descriptions SET description='Don’t tell me what to do. Scram or I might do something stupid' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="154" and playerY=="0":
	      cur.execute("UPDATE descriptions SET description='Jack: You got a dirty mouth there boy. Get out of my face!\nOkay, time to leave living room.' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="155" and playerY=="1": #Red in party (Fin path)
		cur.execute("UPDATE descriptions SET description='April: Oh, hi! I was afraid that you wouldn’t come at all.\n\nYour chat is interrupted by shout. Someone is fighting in the lobby!'  WHERE roomX="+playerX+" AND roomY="+playerY)
		cur.execute("UPDATE rooms SET exitNorth=TRUE WHERE roomX=155 AND roomY=1")
		getDescription(playerX, playerY)
	elif "2" in action and playerX=="155" and playerY=="1":
		cur.execute("UPDATE descriptions SET description='April: Well hello to you too handsome!\nApril winks at you. She looks so happy.\n\nYour chat is interrupted by shout. Someone is fighting in the yard, just ahead from the terrace!' WHERE roomX="+playerX+" AND roomY="+playerY)
		cur.execute("UPDATE descriptions SET description='Jack: Who´s the man? I am! Say my name!\nJack is throwing Fred around again. You should save Fred.' WHERE roomX=155 AND roomY=0")
		cur.execute("UPDATE rooms SET exitNorth=TRUE WHERE roomX=155 AND roomY=1")
		getDescription(playerX, playerY)
	elif "1" in action and playerX=="155" and playerY=="3": #Red in street after leave (Fin path)
		cur.execute("UPDATE descriptions SET description='April: I know, me too. You’re really a nice guy \n Hey come here...'  WHERE roomX="+playerX+" AND roomY="+playerY)
		cur.execute("UPDATE rooms SET exitNorth=TRUE WHERE roomX=155 AND roomY=2")
		getDescription(playerX, playerY)
	elif "2" in action and playerX=="155" and playerY=="3": 
		cur.execute("UPDATE descriptions SET description='April: I know he´s a jerk - unlike you! \n Hey come here...' WHERE roomX="+playerX+" AND roomY="+playerY)
		cur.execute("UPDATE rooms SET exitNorth=TRUE WHERE roomX=155 AND roomY=2")
		getDescription(playerX, playerY)
	elif "1" in action and playerX=="234" and playerY=="-1": #Red in street after leave (Fin path)
	      cur.execute("UPDATE descriptions SET description='April: I know, me too. You’re really nice guy. \nHey come here... \nApril leans towards you. Hug her?' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="234" and playerY=="-1":
	      cur.execute("UPDATE descriptions SET description='April: I know he’s a jerk - unlike you! \nHey come here... \nApril leans towards you. Hug her?' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="254" and playerY=="0": #Fin in party (bully path)
	      cur.execute("UPDATE descriptions SET description='Fred: Don´t tell me what to do or I might do something stupid!' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="254" and playerY=="0":
	      cur.execute("UPDATE descriptions SET description='Fred: You watch yourself you… you oaf!' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="255" and playerY=="1": #Red in party (Fin path)
		cur.execute("UPDATE descriptions SET description='April: Oh, hi. I was afraid that you wouldn’t come at all. But you could’ve come alone and not with Jack.\n\nYour chat is interrupted by shout. Someone is fighting in the yard in front of you!'  WHERE roomX="+playerX+" AND roomY="+playerY)
		cur.execute("UPDATE rooms SET exitNorth=TRUE WHERE roomX=255 AND roomY=1")
		getDescription(playerX, playerY)
	elif "2" in action and playerX=="255" and playerY=="1":
		cur.execute("UPDATE descriptions SET description='April: Well hello to you too. I see you’re still friends with Jack, why? He’s such a dork.\n\nYour chat is interrupted by shout. Someone is fighting in the yard in front of you!'  WHERE roomX="+playerX+" AND roomY="+playerY)
		cur.execute("UPDATE rooms SET exitNorth=TRUE WHERE roomX=255 AND roomY=1")
		getDescription(playerX, playerY)
	elif "1" in action and playerX=="256" and playerY=="3": #Red in street (not worst ending)
	      cur.execute("UPDATE descriptions SET description='April: Keep telling yourself that! Are you happy now?! I hate you so much!' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="256" and playerY=="3":
	      cur.execute("UPDATE descriptions SET description='April: What!? Babe!? He was just drunk and bitter because of everything you have done to him! I hate you! Don't ever again come near me!!!' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="254" and playerY=="3": #Red in street (worst ending)
	      cur.execute("UPDATE descriptions SET description='April: I'm glad you have changed. Hey... come here...' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="254" and playerY=="3":
	      cur.execute("UPDATE descriptions SET description='April: I'm glad you came to your senses. Hey... come here...' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="234" and playerY=="-1": #Red in street after leave (Fin path)
	      cur.execute("UPDATE descriptions SET description='April: I know, me too. You’re really nice guy. \nHey come here... \nApril leans towards you. Hug her?' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="234" and playerY=="-1":
	      cur.execute("UPDATE descriptions SET description='April: I know he’s a jerk - unlike you! \nHey come here... \nApril leans towards you. Hug her?' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="166" and playerY=="3": #Red at home (good ending)
		cur.execute("UPDATE descriptions SET description='April: Please, let me explain! Jack came in here drunk as a skunk. He was sputtering how sorry he was for everything he had done. I told him to leave but he tried to hug me. I pushed him away but he kept coming. You gotta believe me honey!' WHERE roomX="+playerX+" AND roomY="+playerY)
		getDescription(playerX, playerY)
	elif "2" in action and playerX=="166" and playerY=="3":
	      cur.execute("UPDATE descriptions SET description='April: It’s not what it seems. Let me explain! \nApril: Jack came in drunk as a skunk. He was sputtering how sorry he was for everything he had done. I told him to leave but he tried to hug me. I pushed him away but he kept coming. You gotta believe me honey!' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)	  
	elif "1" in action and playerX=="267" and playerY=="0": #Fin in the office (worst ending)
		cur.execute("UPDATE descriptions SET description='Fred: Believe me, this is totally professional. Please empty your desk.' WHERE roomX="+playerX+" AND roomY="+playerY)
		cur.execute("UPDATE descriptions SET description='You arrive at home. You see April through a kitchen window and she’s with someone. Who could it be? You need to get closer!' WHERE roomX=266 AND roomY=0")
		cur.execute("UPDATE rooms SET exitWest=TRUE WHERE roomX=267 AND roomY=0")
		cur.execute("UPDATE rooms SET exitNorth=TRUE WHERE roomX=266 AND roomY=0")
		getDescription(playerX, playerY)
	elif "2" in action and playerX=="267" and playerY=="0": #Fin in the office (worst ending)
		cur.execute("UPDATE descriptions SET description='Fred: Believe me, this is totally professional. Please empty your desk.' WHERE roomX="+playerX+" AND roomY="+playerY)
		cur.execute("UPDATE descriptions SET description='You arrive at home. You see April through a kitchen window and she’s with someone. Who could it be? Look closer.' WHERE roomX=266 AND roomY=0")
		cur.execute("UPDATE rooms SET exitWest=TRUE WHERE roomX=267 AND roomY=0")
		cur.execute("UPDATE rooms SET exitNorth=TRUE WHERE roomX=266 AND roomY=0")
		getDescription(playerX, playerY)
	elif "1" in action and playerX=="266" and playerY=="3": #Red at home (worst ending)
	      cur.execute("UPDATE descriptions SET description='April: Please, let me explain.' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="266" and playerY=="3":
	      cur.execute("UPDATE descriptions SET description='April: It’s not what it seems. Let me explain.' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="367" and playerY=="0": #Fin in the office (not worst ending)
		cur.execute("UPDATE descriptions SET description='Fred: Believe me, this is totally professional. Please empty your desk.' WHERE roomX="+playerX+" AND roomY="+playerY)
		getDescription(playerX, playerY)
	elif "2" in action and playerX=="367" and playerY=="0":
		cur.execute("UPDATE descriptions SET description='Fred: Believe me, this is totally professional. Please empty your desk.' WHERE roomX="+playerX+" AND roomY="+playerY)
		getDescription(playerX, playerY)
	elif "1" in action and playerX=="366" and playerY=="1": #Bully in the street (not worst ending)
	      cur.execute("UPDATE descriptions SET description='Jack: Hah, no surprise there. We treated him like trash!' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="366" and playerY=="1":
	      cur.execute("UPDATE descriptions SET description='Jack: Hah, no surprise there. We treated him like trash!' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="234" and playerY=="-1":
	      cur.execute("UPDATE descriptions SET description='April: I know he’s a jerk - unlike you! \nHey come here... \nApril leans towards you. Hug her?' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "1" in action and playerX=="234" and playerY=="-1": #Red in street after leave (Fin path)
	      cur.execute("UPDATE descriptions SET description='April: I know, me too. You’re really nice guy. \nHey come here... \nApril leans towards you. Hug her?' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	elif "2" in action and playerX=="234" and playerY=="-1":
	      cur.execute("UPDATE descriptions SET description='April: I know he’s a jerk - unlike you! \nHey come here... \nApril leans towards you. Hug her?' WHERE roomX="+playerX+" AND roomY="+playerY)
	      getDescription(playerX, playerY)
	else:
		printText("So, you decided to type a random number?")
def printDescription(description):
	printText(description)
#**************Chapter transitions*******************
def welcomeScreen():
	global playerX
	global playerY
	playerX = "0"
	playerY = "0"
	getDescription(playerX, playerY)
def goToChapter2():
	global playerX
	global playerY
	playerX = "22"
	playerY = "0"
	getDescription(playerX, playerY)
def goToChapter3Good():
	global playerX
	global playerY
	playerX = "134"
	playerY = "0"
	getDescription(playerX, playerY)
def goToChapter3Bad():
	global playerX
	global playerY
	playerX = "234"
	playerY = "0"
	getDescription(playerX, playerY)
def goToChapter4Good():
	global playerX
	global playerY
	playerX = "144"
	playerY = "0"
	getDescription(playerX, playerY)
def goToChapter4Bad():
	global playerX
	global playerY
	playerX = "244"
	playerY = "0"
	getDescription(playerX, playerY)
def goToChapter5Good():
	global playerX
	global playerY
	playerX = "155"
	playerY = "-1"
	getDescription(playerX, playerY)
def goToChapter5Bad():
	global playerX
	global playerY
	playerX = "255"
	playerY = "-1"
	getDescription(playerX, playerY)
def goToChapter6Good():
	global playerX
	global playerY
	playerX = "166"
	playerY = "0"
	getDescription(playerX, playerY)
def goToChapter6Bad():
	global playerX
	global playerY
	playerX = "266"
	playerY = "0"
	getDescription(playerX, playerY)
def goToChapter6Worst():
	global playerX
	global playerY
	playerX = "366"
	playerY = "0"
	getDescription(playerX, playerY)
def goToChapter7Good():
	global playerX
	global playerY
	playerX = "177"
	playerY = "0"
	getDescription(playerX, playerY)
def goToChapter7Bad():
	global playerX
	global playerY
	playerX = "277"
	playerY = "0"
	getDescription(playerX, playerY)
def goToChapter7Worst():
	global playerX
	global playerY
	playerX = "377"
	playerY = "0"
	getDescription(playerX, playerY)	
def baseballHit():
	global playerY
	playerY = int(playerY)
	playerY = playerY+1
	playerY = str(playerY)
	getDescription(playerX, playerY)
#***********ENDING****************************
def Ending():
	printText("Every single thing you do matters.")
	text.after(4000, endingPart1)
	text.after(8000, endingPart2)
	text.after(12000, endingPart3)
	text.after(15000, endingPart4)
def endingPart1():
	text.config(state=NORMAL)
	text.insert(END, "\nYou have been created in order to make a difference.")
	text.config(state=DISABLED)
def endingPart2():
	text.config(state=NORMAL)
	text.insert(END, "\nYou have been created as one of a kind.")
	text.config(state=DISABLED)
def endingPart3():
	text.config(state=NORMAL)
	text.insert(END, "\nYou have within you the power to change the world.\n             -The Butterfly Effect")
	text.config(state=DISABLED)
def endingPart4():
	text.config(state=NORMAL)
	text.insert(END, "\n\n\n                        THE END")
	text.config(state=DISABLED)
#*************************************************
def getBounds(playerX, playerY):        #Reads from database, where the player can move.
	global bounds
	cur = db.cursor()
	sql = "SELECT exitNorth, exitEast, exitSouth, exitWest FROM rooms WHERE roomX="+playerX+" AND roomY="+playerY
	cur.execute(sql)
	bounds = cur.fetchall()
	return bounds
def specialEvents(action, target):      #Handles all events the game engine can't natively process
	if "play" in action and ("teddybear" in target or "teddy" in target):
		cur = db.cursor()
		sql = "SELECT held FROM items WHERE itemID=0"
		cur.execute(sql)
		itemTeddy = cur.fetchall()
		itemTeddy = str(itemTeddy[0][0])
		if "1" in itemTeddy:
			printText("You bite the teddybear with your gums. It'super effective!\nYour mom smiles brightly to you. She look very happy.\nMom: Good boy!\n...and that pretty much sums up your first years in the magnificent world.\nYears pass as as play, grow and start to explore this world, one small step at a time.\n\n(Press ENTER to go to next chapter)")
		else:
			printText("You don't have a teddybear to play with")
	else:
		printText("I only understood you as far as 'play'")

def baseballSimulatorGood(action, target):
	global swings
	global playerY
	if "swing" in action:
		print(swings)
		if swings == 0:
			printText("The bat feels kind of heavy but you manage to swing it with decent speed and force. Maybe you should take time to practice more.")
			swings = swings+1
		elif swings == 1:
			printText("You’re getting good. Try again?")
			swings = swings+1
		elif swings == 2:
			printText("April sure is watching. So one more time?")
			swings = swings+1
		elif swings == 3:
			printText("Jack: “Quit fooling around I want to hit too someday!” \nJack is about pitch. Get ready. \nJack: “Keep your head up, you wimp!”\n\nCurve ball incoming - swing the bat!")
			swings = swings+1
		elif swings==4:
			hit = random.randint(1,3)
			if hit == 1:
				printText("The ball flies far away beyond anyone’s reach. This is your moment!")
				text.after(5000, baseballHit)
			else:
				printText("You don't hit the ball.")
				text.after(3000, baseballHit)
		elif swings > 4:
			pass
	else:
		printText("Focus on the game!")
def baseballSimulatorBad(action, target):
	global swings
	global playerY
	if "swing" in action:
		print(swings)
		if swings == 0:
			printText("The bat feels kind of heavy but you manage to swing it with decent speed and force. Maybe you should take time to practice more.")
			swings = swings+1
		elif swings == 1:
			printText("You’re getting good. Try again?")
			swings = swings+1
		elif swings == 2:
			printText("You see April watching. One more time, for her?")
			swings = swings+1
		elif swings == 3:
			 printText("Jack: Nice moves! Make sure you hit a homerun!\nFin is about pitch. Get ready.\nFin: Here goes nothing!\nFin throws a really easy pitch! Swing the bat!")
			 swings = swings+1
		elif swings==4:
			hit = random.randint(1,3)
			if hit == 1:
				printText("The ball flies far away beyond anyone’s reach. Homerun!")
				text.after(3000, baseballHit)
			else:
				printText("You don't hit the ball.\nJack: You hit like a girl!")
				text.after(3000, baseballHit)
	else:
		printText("Focus on the game!")
def pitchSimulatorGood(action, target):
	if "pitch" in action:
		bullyHit = random.randint(1,3)
		if bullyHit == 1:
			printText("Jack hit the ball! He's cheering for himself as he makes a homerun.")
			text.after(5000, goToChapter5Good)
		else:
			printText("Jack misses the ball. \nJack: Bollocks. What a load of crap.")
			text.after(5000, goToChapter5Good)
def pitchSimulatorBad(action, target):
	printText("You're in the pitcher's hill. Pitch!")
	if "pitch" in action:
		finHit = random.randint(1,3)
		if finHit == 1:
			printText("Fred hit the ball! \nIt doesn't fly very far, but Fred seems very happy.\nJack yells from the field: Is that all you got wimp!?")
			text.after(5000, goToChapter5Bad)
		else:
			printText("Fred misses the ball. \nJack is laughing. He points at Fred and yells: You couldn't even hit a wall if you wanted to")
			text.after(5000, goToChapter5Bad)

#**********************INTERFACE*************************
#Initialize menus
menu = Menu(gui)
gui.config(menu=menu)
#File menu
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Quit", command=Quit)
#Help menu
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help", command=Help)
helpmenu.add_separator()
helpmenu.add_command(label="About", command=About)
#Set up background
canvas = Canvas(gui, width=1024, height=531)
canvas.pack(side=TOP, fill=BOTH)
img = PhotoImage(file="ui-ylempi2.gif")
canvas.create_image(0,0, anchor=NW, image=img)
#Set up input field
ui2 = PhotoImage(file="ui-alempi2.gif")
canvas2 = Canvas(gui, width=1024, height=141)
canvas2.pack(fill=BOTH)
canvas2.create_image(0,0, anchor=NW, image=ui2)
#Input
command = Entry(canvas2, relief=FLAT, font=("Gabriola", 24))
command.place(x=130, y=50, width=240, height=40)
command.bind("<Return>", Parser)
#Text
text = Text(canvas, height=9, width=80, relief=FLAT, font=("Gabriola", 18), wrap=WORD, state=DISABLED)
text.place(x=50, y=80)
printText(intro)
#scroll = Scrollbar(text) #TODO Implement a working and stylish scrollbar
#scroll.place(x=200, y=200)
#scroll.config(command=text.yview)
#**********************MAIN LOOP***********************************
gui.mainloop()


