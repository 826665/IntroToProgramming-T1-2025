def start_adventure():
    print("Your a C rank adventurer named Captian and you live in Hanakashi, your looking for a C rank Job.")
    print("1.Slay a Giant Snake.")
    print("2.Retrive Missing People.")
    print("3.Explore an large unknown area.")
    
    choice1 = input("> ")
    
    if choice1 == "1":
     Quest_Slay_Snake()
    elif choice1 == "2":
        Quest_Missing_PPL()
    elif choice1 == "3":
        Quest_Exploring()
    else:
        print("Not An Avalible Quest. Please Seletion From These Three")
   
  
    
   
       
def Quest_Slay_Snake():
   
   print("You Take You Dagger and a Small crossbow attach with a fire enchant on the back of your hand And Leave And Start Heading To The Forest.")        
   print("As you walk away father from the Town, You spot a group of Goblins.. And you deiced.")
   print("1. Attack the group of goblins")
   print("2. Sneak Around the group of goblins")
   choice2 = input("> ")
   if choice2 == "1":
    Attack()
   elif choice2 == "2":
    Sneak()
   else:
      print("Rethink Again?")
   

def Attack():
   
   
   print("You ambush the group of goblins and used your dagger at the first three leaving there fangs which you could sell later, which left only two left")
   print("One of the goblin was filled with anger and charged at you while the other trys to get away")
   print("You dodge the attack and slash the goblin three time before he died, but at the corner of your eye you see one running away. which leaves you with 2 more oppsites.")
   print("1.Use your flaming crossbow arrow.")
   print("2.Spare the goblin.")
   Quest_Slay1 = input("> ")
   if Quest_Slay1 == "1":
      Crossbow()
   elif Quest_Slay1 == "2":
      Spare()
      

    
    
def Crossbow():
   print("As you aim you bow as it Glows bright, as you release the sting, the arrow flys through the sir leaving specs of flame off the arrow")
   print("It strikes the goblin through the heart from behind and he falls over leaving a blue fang which was much more rare. You take the fang and head toward the sneak nest. ")
   Snake_Nest()

def Spare():
    print("You watch the goblin run away and you head to the snake nest..")
    Snake_Nest_Ambush()




def Sneak():
    print("You Quietly Sneak around the goblins and head to the snake nest.")
    Snake_Nest()



def Snake_Nest_Ambush():
    print("When You Arrived you spot the Giant Fanged, Venomous snake sleeping. You sneak closer to the snake")
    print("As strike from the head, The Snake Awakens and Shake his head rapidly until you fell off.")
    print("You stand back up looking at the snake, As the snake look back as if it was a stand off.. Only thing idea could pop up first was>")
    print("1. Run around and dodge the upcoming attack and use Earth Magic to trap the snake")
    Earth_Ambush()

def Earth_Ambush():
   print("As you ran around the snake you dodge every incoming attack and shoot big chucks of pellets at the snake to anger him, but as soon you create a structures over the snakes body, a 7 arrows come flying down at you.")
   print("As you look where the arrows came from, It was the goblin that you attack earlier but spared.")
   print("You create a wall guarding from the arrows, but what do you do?")
   print("1. Igrone the Goblins and Focus on the snake first.")
   print("2. Face the goblins first and then the snake.")
   print("3. Try to take both on at once.")

   Ambush = input("> ")
   if Ambush == "1":
      Attack_Snake()
   elif Ambush == "2":
      Attack_Goblins()
   elif Ambush == "3":
      Attack_Both()

def Attack_Snake():
   print("You charge in attacking the snake while creating earth walls blocking the arrows but the snake breaks out the stone and charges at you, as you placed you hand onto the ground creating earth spikes out the ground.")
   print("As get stabbed all over the body and suddenly stop moving and starting from his tail his body starts to disapear..")
   print("But you still had one more promble which was the goblins as you made a whole in a wall, you spot a huge goblin with a bone crown. But you had to fight them off some how..")
   print("1. Use your fire enchanted arrow and wind to spread the fire.")
   print("2. Use wind to blind all the goblins visions. as you use Rock Sprears to attack them")
   Attack = input("> ")
   if Attack == "1":
      Fire()
   elif Attack == "2":
      Rock_Spears()

def Fire():
   print("You break down the walls and quickly shoot you fire arrow at a goblin and setting the goblin on fire and then you use wind to increase the flames burning most of the other goblins besides the big one.")
   print("After the big goblin marches in your direction and then use his axe to an wipe surrounding trees.")
   print("You use thunder magic to boost your speed as you enchant your dagger with fire and suddely dash at the huge goblin")
   print("As the huge goblin turns around a dagger comes flying at him with fire power creating a huge slash on his stomach but wasn't enough.")
   print("The huge goblin kicks you and throws his blade at you.. and only leaving a mess..")
   print("YOU HAVE DIED. TRY A DIFFERENT OPTION NEXT TIME!")

def Rock_Spears():
   print("You fly into the air with wind but also creating big dust storm confusing the goblins. You create tons of rock sprears and preparing to launch an all out attack")
   print("As everything was ready. With all your force you launch all the rock spears into the dust storm killing the every almost every goblin and clearing the dust storm,but The Huge Goblin still stands..")
   print("As you hade one more big rock spear, you modified it with thunder and water magic.")
   print("You launch the last one right at the huge goblin, as the goblin tried to block, It broke his axe and strike him in the heart but also creating a large thunder strike down onto the Huge goblin and with the water, it splash a dead electric effect killing everything around the surrounding. ")
   print("You fall down from the sky and with a little wind you stop your fall but you are out cold.. you think I never thought I could perform something like that before.")
   print("THE END, THANK YOU FOR PLAYING!")

def Attack_Goblins():
   print("As you chosed to force on attention to the goblin, You Charged at the goblins and dodge the arrows then used thunder to increase your speed.")
   print("You strike the first 4 but there were too many then you thought and then you suddely spot a huge goblin with a bone crown.")
   print("Which leaves you with idea..")
   print("Crossbow enchanting magic inside the fire?")
   Magic_Enchant()

      

def Attack_Both():
   print("You look their the wall, then back at the snake.. now decided..")
   print("1. Self Destruct")
   print("2.Create a pit with elecrtic water.")
   choice4 = input("> ")
   if choice4 == "1":
      Self_Destruct
   elif choice4 == "2":
      electric_river()


def Self_Destruct():
   print("You think and think.. until you came up with one last plan.. Self Destruct>")
   print("You already know you will be completely drain after the final attack.. but it was the best you could do.>")
   print("As you create layers of rock around you as you focus and igrone everything around you and stat combining every magic you knew..>")
   print("You could hear the snake hissing and rushing and slamming against the layers of walls and the goblins shooting arrows and slashing there weapon at the rock walls.>")
   print("But, as your only half way from completing, they start breaking through the rock wall layers> ")
   print("You calmly keep focusing on the magic..>")
   print("The snake has broken all the layers on one side, but the goblins are almost inside as the snake lunges at you, but you compelete the magic and held it in for a bit longer and drop the rock layers and released all of the magic.>")
   print("Exploding everything in that forest leaving nothing but a big pit and with you laying there out cold from the explosion.>")
   print("People from Hanakashi came over to see the destruction. They spot your body and took you back to Hanakashi. When you woken up, you were in a tavern and walked out of your room and down stairs.>")
   print("They Question you what happen that day because you were out for 3 days.. and leaving you with a big fee for destorying the whole forest")
   print("THE END, THANK YOU FOR PLAYING!")

def electric_river():
   print("As you were thinking on how to do this, the snake breaks free and lunges at you and you jump dodging his attack into the air with wind magic.")
   print("As the idea finally came to find, the goblins tried to shoot you down, you move away from the arrows and started the plan..")
   print("You create a pit really deep as both the snake and goblins both fell but not enough to kill them, as you start the water magic the snap launchs it self back up at you and barely reaches you as you pour water with lighting slamming the snake back down to the ground.>")
   print("After the snake was paralyzed, the goblin once again shoot at you again and the huge goblin throws his axe at you. ")
   print("You send those back down at them and then pour wate with eletric all over them as they drowned in the water. You clear up the water up and collect there left overs.")
   print("You leave and head back to Hanakashi too relexed..>")
   print("THE END, THANK YOU FOR PLAYING!")

def Magic_Enchant():
   print("You run out and shoot the goblins with bows and change the arrow to a normal arrow and put  larage amount of water and lighting inside and shot at the floor by a goblins foot and hid.")
   print("It caused a thunder strike from the sky and cause a chain reaction with all the goblins that had a weapon with metal, besides the big goblins and the goblins with clubs")
   print("The goblins charged at you as you dodge there attack as you were open and forgotten the about the giant snake, the giant snake spots you and lunges you, you tried to dodge but didn't have enough time to move..")
   print("YOU ARE DEAD. TRY AGAIN")


def Snake_Nest():
    print("When You Arrived you spot the Giant Fanged, Venomous snake sleeping. You sneak closer to the snake")
    print("As strike from the head, The Snake Awakens and Shake his head rapidly until you fell off.")
    print("You stand back up looking at the snake, As the snake look back as if it was a stand off.. What do you do?")
    print("1. Run around and dodge the upcoming attack and use Earth Magic to trap the snake")
    print("2. Use Thuder Magic that strikes the snake from the head")
    print("3. Use Dark magic to create smoke and you hide underground and able to moce around")
    print("4. Use Wind magic and create a teal ball in your hand that Rapidly increases by your control")
    print("5. Combine Wind magic and Fire Magic")
    Quest_Slay2 = input("> ")
    if Quest_Slay2 == "1":
       Earth_Magic()
    elif Quest_Slay2 == "2":
       Thunder_Magic()
    elif Quest_Slay2 == "3":
       Dark_Magic()
    elif Quest_Slay2 == "4":
       Wind_Magic()
    elif Quest_Slay2 == "5":
       Combine_Magic()

def Earth_Magic():
   print("You around the snake and run over his tail twice and perform earth magic mid-air and trap his body in the ground with earth.")
   print("As you walk closer the snake breaks out of the earth magic and puts his tail into the ground but also does a lunge at you with his month but you quick make a earth wall dodging out the way.")
   print("As you dodge his attack his tail from out the ground and stabs you in the air.")
   print("YOU HAVE DIED. TRY A DIFFERNT SPELL NEXT TIME!")

def Thunder_Magic():
   print("As You used thunder magic the snake lunges at you but before he could reach you you finish the spell chant and strikes the snake in the head..")
   print("The Snake was paralyzed. You Jump in stabbing it all over the body and before the last attack the snake was unparalyzed and as he lunge at you, you use your fire enchanted crossbow to shot at it which killed it leaving a really big yellow electric fang.")
   print("You take the giant red fang head back to Hanakashi. When you arrived you turn everything thing for enough money for the next 3 months and you also Ranked up to B rank..")
   print("You take everything and head home and rest for the rest of the day..")
   print("THE END THANK YOU FOR PLAYING!")

def Dark_Magic():
   print("You yell Shamac creating a really big black smoke and your dark magic lets you travel undergroud leaving a small black trail.")
   print("As you underground you rapidly strike from everywhere of the snake body. The snake swings his tails clearing all the smoke and see lots of black trail all over the floor")
   print("The Snake jump up and does a really hard slam onto the ground, as you go flying up into the air and the snake jumps up at you trying to swallow you whole you use a little wind to force yourself to fly down faster and strike the snake with tons of speed on the head.")
   print("Using Dark magic inside your dagger and high speed you fly down striking the snake in the head and the dark magic numbing the body of the snake unable to move. The snake body disapear mind air as a Dark black fang drops. ")
   print("You slow yourself down from the air and grab the Dark fang and head back to Hanakashi.")
   print("As you arrived, You sell your items with the rare blue fang and you also Ranked up to B. You leave and the first thing you planned to do was eat.")
   print("THE END, THANK YOU FOR PLAYING!")


def Wind_Magic():
   print("You use wind to carry the surrounding sand and dirt to create a Domain blinding the snake so you could quick fly into the sky and slices of wind to hit the snake it landed both of them. ")
   print("The Snake jumps in that direction but you already moved away from that area and create a ball like the wind spins in every direction creating a ball that rapidly increase but drains you quickly")
   print("Outside of the domain you create lots of floating spinning ball, now that everything was ready you clear the sand and dirt striking all the float balls down at the snake at once leaving nothing but the snakes green floating fang and green tail.")
   print("You take the floating fang and green tail and quickly use wind magic to travel quicker but as look as you got close to Hanakashi you faint because wind drain lots of your energy making you land under a tree.")
   print("As you awaken only find the floating fang but the tail was nowhere found so you slowly walk back still with no energy with only the floaing fang.")
   print("THE END, THANK YOU FOR PLAYING!")

def Combine_Magic():
   print("As you kept running around and shooting the snake with flaming arrow, behind your body you were creating a new type of magic that is rare to master.")
   print("You use dark magic to clone yourself faking yourself and you hid underground waiting and creating other clone of yourself.")
   print("The snake swing his tail killing all the clone, you shoot youself out from underground and throw a spinning ball with the inside filled what looks like lava from the fire magic.")
   print("As the spinning ball lands it release tons of lava burnning the snake but the snake didn't give up and lunge at you but you couldn't move as you fell close to the snake mouth but then suddely thunder strike the snake killing it off..")
   print("Before you went out cold you saw a few other people running up to you then you blacked out.")
   print("As they brought you back to Hanakashi, you awaken in a bed next to you was a giant lava fang inside a jar. You stood up and walk outside your room. The people that found you was no where to be found..")
   print("As you took the giant lava fang outside the jar and went to sell it. The trader watch the people take you and knows who it is. You affor half of the money you gain to them and left and headed to go train combined magic more.")
   print("THE END, THANK YOU FOR PLAYING!")


def Quest_Missing_PPL():
   print("You take the quest to find missing people. It says there are three missing people and where they were last seem.")
   print("1. Ken, Large sword, Black hood and green clothing, last seen near the alley way by the tavern")
   print("2. Max, Bow, Black and gray clothing, last seen on the walls of Hanakashi.")
   print("3. Ethan, Light sword with sheild, black pants, light brown shirt, last seen exploring an cave.")
   Quest_Choice1 = input("> ")
   if Quest_Choice1 == "1":
      Ken()
   elif Quest_Choice1 == "2":
      Max()
   elif Quest_Choice1 == "3":
      Ethan()
   
def Ken():
   print("You sent off to seek the Tavern.")
   print("It was about a 15 minute walk to the tavern")
   print("The first thing you do is head inside asking for info about Ken")
   print("After searching for info, there was no luck")
   print("You search the inside of the tavern finding nothing, you walk outside and check around the tavern and find a sewer lid at the back of the tavern with some foor print with mud that hvaved dryed out.")
   print("You open the lid and jumped down..")
   print("The sewer smells like if someone puked, but you kept following the mud footp print until there was no more mud foot print because the sewer washed it away..")
   print("But you kept ,moving foward as you turn the corner there was a door. You walk over to the door and opened the door. The door lead down to even more stairs going deeper, as you kept walking down the stair with no light so you use fire magic to make light.")
   print("After you reach the bottom another door was in front of you, and process and open the door finding a dungeon but as much as you wanted to report this back, you were more worried about the person and headed in.")
   print("As you explore the unknown dungeon a lizard with sharp teeth and toxic acid and spited at you as you dodge and the acid started to dissolve the floor. You got up and swinged you dagger, the lizard jump back in the air as you shot your crossbow putting the lidzar on fire.")
   print("The lizard rolled on the floor as you jump and striked, killing the lizard and thought these lizards are easier then the one on land. You kept moving foward until you found three more lizards.. As you easily wiped them out.")
   print("At the end you find Large sword lying on the ground as you looked up and saw Ken's left over body.. with half of his stomach body dissolved, you take the body back up to surface used dark magic to travel thought the lizards and close that door off.")
   print("As you arrived back you hand over the body and inform that there a dungeon at the bottom of the sewers and head to the next missing person on your list which were still two missing people but you just went in order")
   



def Max():
   print("You head off to the walls surrunding Hanakashi and if anyone knew Max ot last seen him.. Only some people knew where he was last seen which was near the southern side of the wall as you head to the south side of the wall.")
   print("There was a tower which was where he was last standing and you search around looking for info but didn't find anthing so you headed down to look for more. As you walked down and started looking aroud the wall and after you gotta on the floor you step on a trap")
   print("You feel into a pit that put you inside a cell, but no one was around. You look around and saw a flag with symobl which you never seen before. You use dark magic to slip under the bars and explore around the place inside you rdark magic.")
   print("You find a room with a person inside with really tired eyes as they spot your black trail with dark magic, you suddely come out from the ground and question..")
   print("Captian - Are you Max?")
   print("??? - wHo ArE yOu? And how do you know my name?")
   print("Captian - Alright so you are Max")
   print("You the ropes off his hands and slowly drop him with his weak body. You hand him a piece of bread with Water")
   print("Captian - Its the only thing I brought, sorry.")
   print("You watch him eat away very quickly and he stood up and you gave him a sword off the wall and walked to the next door. You hid at behind the wall by the door as you could hear laugher and peak around the corner spoting 3 random people playing cards. What to do next?")
   print("1. Roll a small flaming ball into the room and explodes on a snap.")
   print("2. Use lighting magic and struck them all together")
   print("3. Rush in your dagger and Max with the sword behind.")
   Missing_choice1 = ("> ")
   if Missing_choice1 == "1":
      Flaming_Ball()
   elif Missing_choice1 == "2":
      Lighting_Bolt()
   elif Missing_choice1 == "3":
      Ambush_Attack()

def Flaming_Ball():
   print("You roll a big ball of fire into the middle of the ball as you hid behind the wall, The trail of fire got the three guys attention as they stood up, you snap your fingers as the ball lighten up and explodes slamming the three guys out.")
   print("Max and you tie the three guys up and went into the next room and open the door and saw two people with only the chest piece of a knight armor and charge in knocking one out as the other one charged at you as you slide kick him making him fall and knocking him out.")
   print("Max tied them both as you kept walking as you cleared most of them out, you find a door with light coming from the outside which was the next morning as you open the door, you were ambushed..")
   print("Decide..")
   print("1. Lighting chain")
   print("2. Water Magic")
   print("3. Fire magic")
   Missing_choice2 = ("> ")
   if Missing_choice2 == "1":
      Lighting_Chain()
   elif Missing_choice2 == "2":
      Water_Magic()
   elif Missing_choice2 == "3":
      Fire_Magic()

def Lighting_Chain():
   print("You create dark cloud above you, but the lighting couldn't strike the ceiling above you and you stand there helpless as every guard charages at you, stabbing you as you fell over helpless..")
   print("YOU HAVE DIED. TRY A DIFFERNT SPELL NEXT TIME!")

def Water_Magic():
   print("As you create a wall of water surrounding the guards and you dash out with max and managed to exit, as they search the tower for the two of you.")
   print("Obviously you couldn't leave then running around so you ambushed each one from the roof of the tower with a black cloak and tied them up and ended turning them all in.")
   print("You relax a bit before moving onto the next missing person. Ethan.")
def Fire_Magic():
   print("You use fire as a shield from them getting close to you, as you walked away from the senese with max, but one shoot an arrow at you stabing you in the back as you hid behind the tree, you couldn't heal so tried to think of plan.. before that they already strike you..")
   print("YOU HAVE DIED. TRY A DIFFERNT SPELL NEXT TIME!")

def Lighting_Bolt():
   print("You cast a lighting bolt, but there was a ceiling and above the ceiling was rock so the lighting bolt strike the room of the wall.. One pulls a bow and shoots..")
   ("YOU HAVE DIED. TRY A DIFFERNT SPELL NEXT TIME!")

def Ambush_Attack():
   print("You and Max Charged in and takedown two of them leaving only one, He pulls a bow and shoot at Max, You use wind to push max away making the arrow miss.")
   print("You flame the lasy person and headed as you open the door slowly and spot two guards and told max to sneakly takedown them from behind..")
   print("You open the door taking down as the second guard comes running at you, then Max strike from behind.")
   print("The next door has a small peep hole as 6 men stand outside the door. You Picked to blind them then use dark magic to trail away with Max.. as the plan worked. You and Max had escaped.")
   print("You head back to return max to a tavern to recover. Which left two people left..")
   print("1. Ken")
   print("2. Ethan")



def Ethan():
   print("Leave again and head toward the location of the cave where he was last seen. When you arrived, the cave seem to closed in as you slip thought with dark magic and continued..")
   print("As you walked deeper into the cave you spot something with a skull, It was a sheepman a d rank monster as you stiked it twice, and walked away going deeper.")
   print("The Monster got tougher but you were able to make it down, you spot a light source in the distance and spell something really bad. You walk closer as you spot someone siting there, alive.")
   print("You walk forward with a greet, as the person got scared, as soon as he got close to the fire he could your face..")
   print("??? - A Human?")
   print("Captian - Are you the missing person, Ethan?")
   print("Ethan - Yeah That would be me.")
   print("He gave you a story about how he had taken a quest to explore this cave alone. A explosion went off and closed him off and he's been feeding on the monster meat and drinking the cave water.")
   print("Told him that you were gonna get him out of the cave. His face glowed with a smile as you started walking back.")
   print("You walked into a new type of enemy that had a tongue that was a rock, and swing it at you cuting your cheeck as the tounge was really sharp. As you threw down you touch the rock jump onto it and made a weird suffering noise..")
   print("What Do You Do Next?")
   print("1. Light the room with Fire then strike")
   print("2. Send a flying rock spear at it")
   Missing_Choice3 = input("> ")
   if Missing_Choice3 == "1":
      Light()
   elif Missing_Choice3 == "2":
      Spears()

def Light():
   print("You Light the room up with flames and the rock makes with weird noise again as you strike. the rock it did nothing. As you ran back you spot something in his month..")
   print("This time you strike with your on fire, The rock opened his month and a shiny crystal was in it. You stike it killing it off.. As you sweat, you hear lots more of those coming from behind makinf crying noises.")
   print("You take ethan and rush up, dodging every other monster you incountered. As you reach the top you fogoted about the closed rocks as you use dark magic taking both you and Ethan outside as you sigh, and fell over")
   print("Ethan took you back to the closest tavern, as you awaken Ethan was out cold too and it was already night. You turn in your quest and Told them Everyone was found.")
   print("The very next day Both Max and Ethan ask if they could join you advanture, as you accepted them both, the three of you head out for complete another quest..")
   print("GOOD ENDING, THANK YOU FOR PLAYING!")

def Spears():
   print("You launched rock spears at the rock and it deflected it and ate the spear instead and grew more, it used it tounge and broke the boulder you were behind as you there thinking, also striking you in the process..")
   print("YOU HAVE DIED. TRY A DIFFERNT SPELL NEXT TIME!")

def Quest_Exploring():
   print("You chose to explore as you quickly collected your items and head south to the new area.")
   print("When you arrived, you found three paths that were not on the map so you assumed that this is part of the unknow area, what path do you pick now?.")
   print("1. Forward")
   print("2. Left")
   print("3. Right")
   Exploring_choice1 = input("> ")
   if Exploring_choice1 == "1":
      Forward()
   elif Exploring_choice1 == "2":
      Left()
   elif Exploring_choice1 == "3":
      Right()

def Forward():
   print("You move forward.. You kept walking was something crosses your path.. It was a bear looking animal as it stared at you and kept walking. ")
   print("A new monster has walked by you but seemed unharmful, you continued down the path until you arrived at an abandoned village.")
   print("One building had a claw mark on the building. As you get appeared by what look like a skeleton with knight armor as it strike you.")
   print("You jump out of the way.")
   print("1. Fight the unknown Skeleton")
   print("2. Run away and hide.")
   Forward_choice =input("> ")
   if Forward_choice == "1":
      Strike()
   elif Forward_choice == "2":
      Run()

def Left():
   print("You took the Left as it leaded to a really big forest. As you kept walking forward you step into this trap which made you fill dowm a pit.")
   print("When you were at the bottom you easily flew out of the trap, landing your self back on the land.. You kept walking as you Jump over traps and wires until you reached the end.")
   print("It was just a big cliff that you couldn't climb because of the really big curver so you turned back and return with nothing really new besides the traps..")
   print("Another boring quest, you claim you reward and headed to bed.")
   print("Boring ending..")

def Right():
   print("You had a really strong feek with the right trail because it always right, right?")
   print("The right path lead you up a snowy mountain, you travel up as you spot a big white Scorpion coming your way what do you do?")
   print("1. Cast fire magic")
   print("2. Water Magic")
   Right_choice1 = input("> ")
   if Right_choice1 == "1":
      Fire_magic()
   elif Right_choice1 == "2":
      Water_magic()

def Fire_magic():
   print("You cast fire at the Scorpion, the scorpion was on fire as it burn away really easily.")
   print("You kept moving forward, nothing was much of a problem as you marched over the mountain and finding a new biome, which was the pont you turned back.")
   print("You arrived back with no problems and turn in your reward and relaxed..")

def Water_magic():
   print("You use water to freeze the scorpion and advantured ahead as the scorpion breaks free and marches with many more others and you clueless didn't know.")
   print("As you reach the top and turn around the scirpion cornered you as you were helpless.")
   print("Bad Ending.")

def Strike():
   print("You waited for another attack and dodge the attack from the air.. It broke really easily apart, the body was still moving as you step on his head. The body suddely stoped.")
   print("You walked around more and everything looked like if everything has frozen in time with food in plates and fridges opened. As you start marking this village down on the map.")
   print("You continued walking into a really big open field as you spot too many different kind of monsters on the field. How will you get rid of them?")
   print("1. Walk by to get there attention and strike each one with a clone")
   print("2. Leave them")
   Foward_choice2 = input("> ")
   if Foward_choice2 == "1":
      clones()
   elif Foward_choice2 == "2":
      Leave()

def clones():
   print("When you walked in the middle of the field, every monster looked you and start running which was something new to you. You use dark magic to clone yourself in the air")
   print("They strike from above as some died really easily, and some not so easy, as you buff your self to strike the other and placing some dark magic inside as they numb to death.")
   print("Planned word! As you mark down this big field on your map as well. But at the end of the path lead to another really deep forest, you could feel the uneasy as you stood there and turn back for now.")
   print("You walked back and heard the sounds of bones as you looked over the hill to the village, there was tons of skeleton with knight armors.")
   print("What Next?")
   print("1. Cause lighting to village")
   print("2. Go around back to Hanakashi.")
   Foward_choice3 = input("> ")

   if Foward_choice3 == "1":
      Lighting()
   elif Foward_choice3 == "2":
      Go_around()

def Lighting():
   print("You strike the village with tons of lighting strikes, as it burn everything but was wiping the skeleton really quick.")
   print("Once everything was clear you head into the burning village and pick up bones that were still move because the heart of the skeleton has not been stab or crushed.")
   print("You brought the pieces of bones back to Hanakashi, until you turned around and spot the army marching towards the tower.")
   print("Now what?")
   print("1. Fight them off")
   print("2.Warn the tower that a large army of skeleton is marching toward the town.")
   Foward_choice4 = input("> ")
   if Foward_choice4 == "1":
      Defend()
   elif Foward_choice4 == "2":
      Warn()
   
def Defend():
   print("You turn around and charge into battle as you striked the skeletons, they kept getting back up")
   print("Until you remeber you need to crush the head, you turn around once more and flew into the air creating chucks of rock and sending them down at the skeletons.")
   print("Most skeletons has been crushed but the other where were still alive kept marching toward the town.")
   print("You spaced out for 10 mins and fell down")
   print("You got back up and the town was raided, as you wonder why you even spaced out.")
   print("Everyone has ran away or even died as other people just arrived back from a quest they finished.")
   print("You fall over once again and blacked out. When you woke up it was already night and you were surrounded other people by a camp fire.")
   print("You sit there thinkng how uselss you were..")
   print("BAD ENDING!!")

def Warn():
   print("You run back to the village and warn them about the army if skeleton coming this way as every panic and every soldier prepared for battle.")
   print("When the skeleton arrived, everyone charged into battle, including you as you knew the weak spot.")
   print("There were bones, bodys everywhere. But the town was saved and many people were grateful that you told them sooner they would of haved not won.")
   print("You walked into a tavern and fell over, you woken in a bed, as the bright night sky shined into your room.. as you snooze off once more..")
   print("GOOD ENDING! THANKS FOR PLAYING!")

def Go_around():
   print("You walk around the village carelessly, as one skeleton spots you.")
   print("The skeleton throws a wooden spear next to your foot. You look back the village as every skeleton marched to you.")
   print("As you dash into battle and cleaning everything body and crushing there skulls. As you took some body parts back to the village as a new monster type.")
   print("You were rewarded extra money for exploring and bring back a new type of monster back with you.. You walk up stairs and lied in bed..")
   print("Good ending? THANKS FOR PLAYING!")

def Leave():
   print("You left the monsters and headed back to the town. You used wind magic to fly over the village and the three paths.")
   print("When you arrived back and turned in your qust you were rewarded as you left to go eat somewhere.")
   print("Weeks you walk by and saw 7 bodys getting carried. You listen to the people saying they were wipe in the new field area..")
   print("You blamed youself for getting that clanned wipe because of how careless you were..")
   print("Bad Ending.")

def Run():
   print("You hid inside the house as the skeleton turn around and headed striaght for the house you were in.")
   print("You strike the skeleton and ran out. As the skeleton fall arm fell off and you ran back to the town.")
   print("This time not only one followed you but a whole army")
   print("Now what?")
   print("1. Defend them off")
   print("2.Warn")
   Foward_choice5 = ("> ")
   if Foward_choice5 == "1":
      Defend()
   elif Foward_choice5 == "2":
      Warn()

start_adventure()