DROP DATABASE IF EXISTS gameoflife;
CREATE DATABASE IF NOT EXISTS gameoflife;
USE gameoflife;

DROP USER 'dbuser7'@'localhost';
CREATE USER 'dbuser7'@'localhost' IDENTIFIED BY 'dbpass';
GRANT SELECT ON gameoflife.* TO 'dbuser7'@'localhost';
GRANT UPDATE ON gameoflife.* TO 'dbuser7'@'localhost';
FLUSH PRIVILEGES;

/* source C:/Users/Samuli/Documents/OPISKELU/Pelit/Game of Life/create.sql; */

CREATE TABLE IF NOT EXISTS rooms(
   roomX INT(11),
   roomY INT(11),
   exitNorth BOOLEAN,
   exitEast BOOLEAN,
   exitSouth BOOLEAN,
   exitWest BOOLEAN,
   PRIMARY KEY(roomX, roomY)
   );

CREATE TABLE IF NOT EXISTS items(
	itemID INT(11),
	itemX INT(11),
	itemY INT(11),
	itemName VARCHAR(20),
	held BOOLEAN,
	PRIMARY KEY(itemID)
	);
   
CREATE TABLE IF NOT EXISTS descriptions(
   descriptionID INT(11) AUTO_INCREMENT,
   roomX INT(11),
   roomY INT(11),
   description VARCHAR(2000),
   PRIMARY KEY(descriptionID),
   FOREIGN KEY(roomX, roomY) REFERENCES rooms(roomX, roomY)
   );

/* roomX,roomY,exitNorth,exitEast,exitSouth,exitWest*/
INSERT INTO rooms(roomX, roomY, exitNorth, exitEast, exitSouth, exitWest) VALUES
(0, 0, TRUE, FALSE, FALSE, FALSE), /*Game start*/
(0, 1, FALSE, FALSE, FALSE, FALSE), /* Mom */
(0, 2, TRUE, FALSE, FALSE, FALSE), /* Chapter II start */
(22, 0, TRUE, FALSE, FALSE, FALSE), /* Kindergarten start */
(22, 1, TRUE, FALSE, FALSE, FALSE), /* Kindergarten yard */
(22, 2, FALSE, TRUE, FALSE, TRUE), /* Kindergarten inside */
(23, 2, FALSE, FALSE, FALSE, FALSE), /* Kindergarten Fred */
(21, 2, FALSE, FALSE, FALSE, FALSE), /* Kindergarten Jack */


(134, 0, FALSE, TRUE, TRUE, TRUE), /* School lobby*/
(135, 0, FALSE, FALSE, FALSE, TRUE), /* School room Fred */
(133, 0, FALSE, TRUE, FALSE, FALSE), /* School Jack */
(134, -1, TRUE, FALSE, FALSE, FALSE), /* School April */
(134, 1, FALSE, FALSE, FALSE, FALSE), /* Teacher*/

(234, 0, FALSE, TRUE, TRUE, TRUE), /*School lobby(Jack path) */
(235, 0, FALSE, FALSE, FALSE, TRUE), /* School Fred */
(233, 0, FALSE, TRUE, FALSE, FALSE), /* School Jack */
(234, -1, TRUE, FALSE, FALSE, FALSE), /* School April*/
(234, 1, FALSE, FALSE, FALSE, FALSE), /* Teacher (Jack path) */


(144, 0, TRUE, FALSE, FALSE, FALSE), /* Baseball (Fred path) */
(144, 1, FALSE, FALSE, FALSE, TRUE), /* Baseball game */
(143, 1, TRUE, FALSE, FALSE, FALSE), /* Baseball April */
(143, 2, TRUE, FALSE, FALSE, FALSE), /* Baseball Fred */
(143, 3, FALSE, FALSE, FALSE, FALSE), /* Baseball pitch simulator */

(244, 0, FALSE, FALSE, FALSE, FALSE), /* Baseball (Jack path) */
(244, 1, FALSE, FALSE, FALSE, TRUE), /* Baseball game */
(243, 1, TRUE, FALSE, FALSE, FALSE), /* Baseball April */
(243, 2, TRUE, FALSE, FALSE, FALSE), /* Baseball Jack */
(243, 3, FALSE, FALSE, FALSE, FALSE), /* Baseball pitch simulator */


(155, -1, TRUE, FALSE, FALSE, FALSE), /* party street fred */
(155, 0, TRUE, TRUE, FALSE, TRUE), /*party lobby fred */
(156, 0, FALSE, FALSE, FALSE, TRUE), /* party punch fred) */
(155, 1, FALSE, FALSE, TRUE, FALSE),/* party red fred */
(154, 0, FALSE, TRUE, FALSE, FALSE),/* party bully fred */
(155, 2, FALSE, FALSE, FALSE, FALSE), /*party fight scene*/
(155, 3, TRUE, FALSE, FALSE, FALSE), /* red meet */
(155, 4, FALSE, FALSE, FALSE, FALSE), /* red hug */
(155, 5, FALSE, FALSE, FALSE, FALSE), /* red kiss */

(255, -1, TRUE, FALSE, FALSE, FALSE), /* party street jack */
(255, 0, TRUE, TRUE, FALSE, TRUE), /*party lobby jack */
(256, 0, FALSE, FALSE, FALSE, TRUE), /* party punch jack */
(255, 1, FALSE, FALSE, TRUE, FALSE),/* party red jack */
(254, 0, FALSE, TRUE, FALSE, FALSE),/* party fin jack */
(255, 2, FALSE, TRUE, FALSE, TRUE), /* party fight */
(254, 2, TRUE, FALSE, FALSE, FALSE), /* worst ending help fin */
(256, 2, TRUE, FALSE, FALSE, FALSE), /* not worst ending bully fin */
(254, 3, TRUE, FALSE, FALSE, FALSE), /* red meet worst */
(254, 4, FALSE, FALSE, FALSE, FALSE), /* red worst hug */
(254, 5, FALSE, FALSE, FALSE, FALSE), /* red worst kiss */
(256, 3, FALSE, FALSE, FALSE, FALSE), /* red meet not worst */

/*Kaveri FININ kanssa,tappeli tai ei,Paragon*/
(166, 0, FALSE, TRUE, FALSE, FALSE), /* work homeFIN */
(167, 0, FALSE, FALSE, FALSE, TRUE), /* work cityFIN */
(166, 1, TRUE, FALSE, FALSE, TRUE), /* work home after work FIN */
(166, 2, TRUE, FALSE, FALSE, FALSE), /* work home 2 */
(166, 3, FALSE, FALSE, FALSE, FALSE), /* work home 3 */



/*Kaveri ensin BULLYN kanssa, juhlissa vaihtoi puolta, Worst ending*/
(366, 0, FALSE, TRUE, FALSE, FALSE), /* work homeBULLYFIN */
(367, 0, FALSE, FALSE, FALSE, TRUE), /* work cityFIN */
(366, 1, TRUE, FALSE, FALSE, TRUE), /* work home after work FIN */

(266, 0, FALSE, TRUE, FALSE, FALSE), /* work homeBully ending */
(267, 0, FALSE, FALSE, FALSE, TRUE), /* work cityFIN */
(266, 1, TRUE, FALSE, FALSE, TRUE), /* work home after work FIN */
(266, 2, TRUE, FALSE, FALSE, FALSE), /* work home 2 */
(266, 3, FALSE, FALSE, FALSE, FALSE), /* work home 3 */


/*Closure-kappaleen 1. taulu ns. Paragon*/
(177, 0, FALSE, FALSE, FALSE, FALSE), /* closureFIN */
(177, 1, FALSE, FALSE, FALSE, FALSE), /* closure call bully */

/*Closure-kappaleen 2. taulu, worst ending*/
(277, 0, FALSE, FALSE, FALSE, FALSE), /* closureBULLYFIN */
(277, 1, FALSE, FALSE, FALSE, FALSE), /* closure call fin

/*Closure-kappaleen 3. taulu ns. Not worst ending*/
(377, 0, FALSE, FALSE, FALSE, FALSE); /* closureBULLY */



INSERT INTO items VALUES(0, 0, 1, "Teddybear", FALSE); /* Teddybear in chapt. I */
INSERT INTO items VALUES(1, 144, 0, "bat", FALSE); /* baseball bat, chapt.4 */

/*Ensimmäisen chapterin tekstit LUKU, ALIKULU, HUONEX, HUONEY*/
INSERT INTO descriptions (roomX, roomY, description) VALUES
(0, 0, "You are born in to a loving middle class family. You are in the bedroom. You see your mother ahead of you.\n She tells you to come to her."),
(0, 1, "Mom: What a good boy you are, oh yes you are.\nYou see your favourite teddy on the floor."),
(0, 2, "And that pretty much sums up your first years in this magnificent world. \nMove forward in your life."),
(22, 0, "It is your first day at the kindergarten! You look north and there lies the playground with other children there. In the west you see a school for bigger children. In the east you see a road leading to the big city with lots of tall buildings."),
(22, 1, "You arrive at the playground. You see a red-headed girl all alone by the swing. She's so cute. You also see a boy bullying another kid. \nA bell rings telling you to go inside. You see other kids hurrying inside ahead of you."),
(22, 2, "A big boy is making fun of another kid's clothing. The bully has cool Adidas jacket - unlike the other kid. He finds it really amusing. \nThe kindergartner comes just in time to break the two apart and invite all of you to the classroom. Inside you learn that the pretty girl's name was April. The kid in the Adidas jacket was called Jack and the kid he was bullying was Fred. \n      The next day you come to the kindergarten and see a crowd of children gathered in circle. You push your way through and see Jack bullying Fred. April tells the Jack to stop but he won't listen. Other kids are shunned of Jack's strength as he pushes Fred like a punching bag.\nYou must do something! Help Fred on your right or join Jack on your left and torment Fred together."),
(23, 2, "You: Don't mind about Jack, he's an idiot\nYou help Fred get up. \nJack: Oh, you want to learn some respect too, huh? \nJack beats you up but at least you made a very good friend that day. And a few bruises here and there. \n Days and seasons pass as you and Fred are bullied through the whole kindergarten..."),
(21, 2, "You: Yeah, let's show Fred who the bosses are! \nYou join Jack and together you show Fred who's the boss. \n Time and seasons come and go as you and Jack have good time bullying Fred..."),
(134, 0, "First day at school! Who would've thought that you, April, Jack and Fred end up in the same class?\nYou look at your right and see your friends face. He is just as nervous as you are.\nOn your left you see the face that has been laughing and mocking you as long as you can remember, Jack.\nOne good thing is that the red-headed girl sits behind you. She doesn't probably remember you from kindergarten but you remember her.\nThe teacher is busy starting up her computer so you have time to chat with your friends.\nWhen finished, try looking forward and waiting for the teacher to start the class."),
(135, 0, "Fred: Oh jeez, why does Jack have to be on the same class with us? \nYou:\n1.) Don't worry about him. He cannot harm us in class and we'll just avoid him during breaks.\n2.) We'll have to stand against him."),
(133, 0, "Jack: What you lookin' at bugger ball? You just wait until we have sports. I'll make toast out of you!\nYou:\n1.) Why do you have to be so mean? Can't we just be friends?\n2.)I'll show you who\'s the man!"),
(134, -1, "You turn around and see April. She looks at you, smiling cheerfully.\nApril: Hi!\nYou:\n1.) Hi April! I remember you from kindergarten. \n2.) Hey April, tomorrow you'll see how I make a homerun!"),
(134, 1, "Teacher: Hello class! Let's start today with...\n Years slowly pass and before you realise middle school is upon you."),
(234, 0, "First day at school! Who would've thought that you, April, Jack and Fred end up in the same class? \nYou look at your left and see your friend Jack. Confidence shines from you two. On your right you see Fred who has been your and Jack's target of torment. One good thing is that the red-headed girl sits right behind you. She definitely remembers you for you have been on the spotlight with Jack. The teacher is busy starting up her computer so you have time to chat with your friends.\n"),
(235, 0, "Fred: Please don't hurt me!\nYou: \n1.) Don't worry, I've got better things to do. \n2.) We'll see on the break. Hope you can run fast enough."),
(233,0, "Jack: Can't we just go outside. I hate being here with these losers!\nYou:\n1.) Don't worry, we have baseball tomorrow and the break starts soon\n2.) Hah, you're right, what a bunch of bugger balls!'"),
(234, -1, "You turn around and see April. She looks at you with a faint smile on her face.\nApril: Hello.\nYou:\n1.) 'Hi! I know you from kindergarten.\n2.) Hey! I'm the king of baseball!"),
(234, 1, "Teacher: \nHello class, so let's start today's lesson...'"),
(144, 0, "*PRIIP!*\nTeacher blows the whistle. Baseball game is about to start. \nSadly you don't get to choose whom you play with or against, but at least you have Fred in your team. Too bad Jack plays against you. \nApril is also playing on the other team.\nTeacher said that your team starts as the batters. \nYou pick an old wooden bat from the ground. Give it a few practise swings?"),
(144, 1, "There's a brief pause in the game. It seems that Fred is hitting next. Jack is giving him a hard look from the pitcher's hill and laughing.\nYou see April sitting alone on the left side of the field."),
(143, 1, "You see April sitting on the side tying her shoelaces. As you approach her, she brushes a few red curls from her face and looks at you, smiling merrily.\n April: What's up?\nYou: \n1.) Hi April! Fun game, huh? \n2.) Did you see me out there? I was on fire!"),
(143, 2, "You approach Fred and you see how much the bat is trembling on his hand. He's almost paralyzed with fear. \nYou: \n1.) Yeah! Go Fred! Keep your eyes on the ball! \n2.) Show them who's the man! Be just be the best!"),
(143, 3, "You're in the pitcher's hill! Pitch!"),
(244, 0, "*PRIIP!*\nTeacher blows the whistle. Baseball game is about to start. Sadly you don't get to choose whom you play with or against, but you have Jack in your team so it doesn't matter. You see Fred and April playing in the other team. Teacher said that your team starts as the batters. \nJack gave you a new and shiny wooden bat. Give it a few practise swings?"),
(244, 1, "The game pauses for a moment. It seems that Jack's the next one to go hit the ball. He is giving a hard look to Fred, who cowers in fear on the pitcher's hill.\nApril is sitting alone on the left side of the field."),
(243, 1, "You see April sitting on the side tying her shoelaces. As you approach her, she brushes a few red curls from her face and looks at you, raising her brows, as if asking a silent 'what you want'.\nYou: \n1.) Hi April! Fun game, huh? \n2.) Did you see me out there? I was on fire!"),
(243, 2, "As you approach Jack, you see he tries to bulge his muscles and look bigger. Confidence shines from him.\nYou: \n1.) Yeah! Go Jack! Keep your eyes on the ball!\n2.) Show them who's the man! Be the best!"),
(243, 3, "You're in the pitcher's hill! Pitch!"),

(155, -1, "Oh how the time flies! Only yesterday you were playing baseball with your friends and now you are in high school going to a party. Even though time has passed things haven't changed. Fred is still your best friend and together you stand Jack's torment. April has been throwing glances you quite a lot lately and she even comes to sit with you often in class. You wonder... Well maybe she'll be at the party. You arrive to the house with Fred. You see the front door ahead.\nFred: Well... I guess this is it."), /* party street fred */
(155, 0, "You open the door and enter the house. You're now in the lobby. On your left you see living room and you heard Jack's voice, who clearly is in there already hammered. On your right you see dining room. People are having a great time in there. A narrow corridor lies straight ahead and it seems to lead outside."), /*party lobby fred */
(156, 0, "You enter the dining room. On the table you see a bowl of punch. You shrugh and decide to try it. The punch tastes like lemon soda mixed with cough medicine. Yuck! \nNothing else catches your eye. Except that one guy talking with a houseplant."), /* party punch fred */
(155, 1,"You go through the corridor and end up outside. On the terrace you see April. She's just as beautiful as you remembered. She notices you and a bright smile covers her face.\nYou:\n1.)Hi April! Nice to see you here!\n2.)Hello there beautiful!"), /* party red fred */
(154, 0,"As you enter the living room Jack turns and finally notices you. He smirks and comes to you. \nJack: Look who it is! My favourite turd! \n You:\n1.) C'mon Jack. Take it easy man.\n2.) You, shut up, right now!"),/* party sanaharkka jacking kanssa fred */
(155, 2, "Jack: Who's the man? I am! Say my name!\nJack is throwing Fred around again. You probably should go and save Fred."),
(155, 3, "You leave the house with Fred. You hear Jack shouting insults to you but you don't care. Let him be the jerk he's grown to be.\nSoon Fred thanks you and leaves. It's a shame that the fight interrupted your chat with April.\n\nWhen you walk the street a high voice shouts your name and you see April running to you.\nApril: Don't you leave without saying goodbye. I think it was a brave thing you did – helped Fred and didn't start another fight.\nYou:\n1.) I hate that we had to leave. I would've wanted to stay with you\n2.) I would've wanted to stay but Jack is not worth the trouble."),
(155, 4, "April surprises you with a hearty hug filled with emotion. You hug each other and you feel her warm body against your own. \nWhen you let go your eyes meet. You realise that now would be the perfect moment to kiss!"),
(155, 5, "Perfect kiss!"),

(255, -1,"Oh how the time flies! Only yesterday you were playing baseball with your friends and now you are in high school going to a party. Even though time has passed things haven't changed. You're still Jack's sidekick. Together you have made Fred's life really miserable. As strange as it may seem, April has been hanging around the places where you and Jack usually hang out. \nMaybe she likes bad boys. Anyways, you hope she'll be at the party. \nYou arrive to the house with Jack. You stand there staring at the front door.\n Jack: This is the place allright! Let's get wasted!"), /* party street jack */
(255, 0,"You open the door and enter to the house. You're now in the lobby. On your left you see living room. \nFor your surprise, Fred is in there, drinking quite heavily. There's something different about him, probably it has something to do with the silly beard he is desperately trying to grow. He hasn't yet noticed you. \nOn your right you see the dining room. People are having a great time there. A narrow corridor lies straight ahead and you guess it leads outside."), /*party lobby jack */
(256, 0,"You enter the dining room filled with people. On the table you see a bowl of punch. Man, it looks so tasty. You try the punch and it tastes like lemon soda mixed with cough medicine. Yum!\nNothing else catches your attention. Except that one guy hitting it off with a potted plant."), /* party punch jack) */
(255, 1,"You go through the corridor and end up outside. On the terrace you see April. She's just as beautiful as you remembered. She notices you and smiles. \nYou:\n1.) Hi April! Nice to see you here!\n2.) Hello cutie pie!"), /* party red jack */
(254, 0,"As you enter the living room Fred notices you. He rises from the sofa and starts walking towards you with slightly wavering steps.\nFred: Hey, hey you! I know you, you piece of shit! *burp*\nYou: \n1.) Hey, take it easy dude, no need to get pushy.\n2.) You watch your mouth!"), /* party sanaharkka fredin kanssa jack */
(255, 2, "Fred: I've had enough of you and your bullying.\nFred's fury is volcanic. He is pushing Jack and shouting at him, but Jack finds his outburst mostly comical. \nWhat do you want to do? Help Fred on the left or go on the right side with Jack and show Fred who's the boss. Again."),
(254, 2, "You team up with Fred and together you manage to take Jack down. You leave the party together victorious but still there's tension between you two.\nFred: Listen, I appreciate that you helped me beat Jack but I still can't forgive you for what you two did to me.\nFred leaves and all there's left is the lonely road home ahead."),
(256, 2, "You hold Fred while Jack punches him like a sand bag. You can feel Jack's powerful punches through Fred as you hold him and you hear his screams as he begs Jack to stop. \nSoon the fight is over, if you can even call it a fight. You leave Fred squirming and crying on the floor.\nYou and Jack get thrown out from the party.\nJack: Oh well that was fun while it lasted... See ya buddy.\n Ahead, you see a long road home..."),
(254, 3, "As you walk home thinking of the night's events, you suddenly hear a high voice calling your name. You turn and see April running to you.\nApril: What was that?! First you tease Fred through all his childhood and then you help him take down Jack. Why?\nYou:	\n1.) I guess people change. I realized how wrong I had done and tried to make up for it.\n2.) I got tired of Jack bossing me around and decided to act."),
(254, 4, "April surprises you with a hug. \nAs you hug each other, you can feel April's warm body against your own. When you let go your eyes meet. You realise that now would be the perfect moment to kiss!"),
(254, 5, "Perfect kiss!"),
(256, 3, "When you walk home April appears suddenly.\nApril: Why do you have to be like that?! Fighting against weaker ones with Jack! Aren't you ashamed of yourself?!\nYou:	\n1.) If I hadn't interfered Jack would still be kicking his sorry ass!\n2.) Hey babe, he was asking for it. He should've known not to start a fight with us."),


/*Kaveri FININ kanssa,tappeli tai ei,Paragon*/
(166, 0, "Many years have passed since the events of high school. Things turned out quite all right for you. You started up a business with Fred and your relationship with your lovely April is going great. \nYou feel like nothing could break your happiness. Not even Monday mornings! \nWell, the bus just arrived to the busstop on your right. Time to go to work."),
(167, 0, "You arrive at the office and Fred is already there. He's working on a huge project and introduces it to you and asks you to contact a possible client. Maybe you should call that client and see what you can do."),
(166, 1, "It's Jack?! Why the hell is he in your home? Fast! You need to get closer!"),
(166, 2, "He's groping April. What the hell?! This can't be happening!\n You need to go there and find out what's happening right now! "),
(166, 3, "As you storm inside Jack let's go of April and turns to face you. Second later he realises who you are and his face is filled with smug grin.\nJack: What's up super turd?\nYou: \n1.) April, what's going on?\n2.) What the hell is going on here?!"),
/*Kaveri ensin BULLYN kanssa, juhlissa vaihtoi puolta, Worst ending*/
(266, 0, "Many years have passed since the events of high school. Your friendship with Jack ended when you decided to beat him with Fred. But Fred couldn't forgive you for all the things you and Jack had done to him, not that you were surprised. \nBut there's always a silver lining - you and April have been dating since and even though you two have been fighting sometimes you're still confident about your relationship. You even managed to get an internship in a big company.\nOh, the bus arrived on the bus stop to your right. Time to go to work."),
(267, 0, "You arrive at the office and you are asked to go to the manager's room. When you enter the room you see a familiar face – Fred!\nFred: Hello. No need to sit down, Ill cut straight to the chase. Judging by your performance during your internship I cannot hire you. I'm sorry.\nYou:n1.) Is this because of the things I have done to you?\n2.) You gotta be kidding me!"),
(266, 1, "It's Jack?! Why the hell is he in your home. You better go closer."),
(266, 2, "He's groping April. What the hell?!\nFast! Rush in!"),
(266, 3, "As you storm inside, Jack lets go of April and turns to face you. A second later he recognises you and, with a smug smirk on his face, says: Hey turd-buddy, I'm just testing your wife here. She's super hot!\nYou:\n1.) April, what's going on?\n2.) What the hell is going on here!?"),

(366, 0, "Many years have passed since the events of high school. You stayed friends with Jack through thick and thin. Fred ran away to college and April disappeared soon after. But life hasn't been so bad to you – with only Jack by your side you've never had anyone slowing you down. You've managed to get a job in a big company. You got wealth but no one to share it with. Well, it's time to go to work."),
(367, 0, "You arrive at the office and you are suddenly asked to go the manager's room. Could it be a promotion? When you enter the room you see a familiar face – Fred!.\nFred: “Hello. Long time no see eh? Time is money so I'll cut to the chase. Judging by your performance and teamwork skills, and as the new manager, I have no other choice but to fire you. Please empty your desk and leave. \nYou:\n1.) Is this because of the things I have done to you?\n2.) You gotta be kidding me!"),
(366, 1, "As you walk down the road you see Jack selling hot dogs at the same hot dog-stand as always. He loves his hot dogs. \nJack: What's up man? \nYou: I got fired today! By Fred! Can you believe it?!"),

/*Closure-kappaleen 1. taulu ns. Paragon*/
(177, 0, "You are feeling old. You and April have been living together for a long time now, and now that you are retired you have a lot of time for your grandchildren. \nYou haven't talked to Fred in a long time - maybe you should call him."), /* closureFIN */
(177, 1, "Maybe you should call Jack? For no reasons, but still give him a call"),
/*Closure-kappaleen 2. taulu, worst ending*/
(277, 0, "You are getting old. April has left you ages ago and you are left all alone with no friends. Fred has some fancy job in an international company and Jack is in jail. You sit on the couch. \nYou drift in to your thoughts about all the things you could have done better in your life. That\\'s the way all your days will be spend from this point forward."), /* closureBULLYFIN */
(277, 1, "Maybe you should call Fred. He hates you but you're feeling lonely"),
/*Closure-kappaleen 3. taulu ns. Not worst ending*/
(377, 0, "You are old and weak, merely a shadow of your former self. Even though Jack can be a dick sometimes, he is the only person you can call a friend. You haven\'t seen him in a long time. Maybe you should call him."); /* closureBULLY */


