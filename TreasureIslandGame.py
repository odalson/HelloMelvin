# Welcome to Treasure Island: Your mission is to find the treasure.
# Type whatever choice you have made.
print("*** Welcome to Mel's Island located somewhere within Africa. ***\n "
      "You are expected to locate a treasure chest on the island. ")
enter = input("Would you like to go 'Left' or 'Right'? ")
en = enter.lower()
if en == "left":
    wat = input("You are standing close to the beach. Would you like to 'Swim' or 'Wait'? ")
    wat = wat.lower()
    if wat == "wait":
        boat = input("You just got a boat to get across. Would you like to 'Take' or 'Reject' the boat? ")
        boat = boat.lower()
        if boat == "reject":
            climb = input("Would you like to climb the coconut tree to search for any cave around? 'Yes' or 'No' ")
            climb = climb.lower()
            if climb == "yes":
                run = input("Would you like to run to the cave? 'Yes' or 'No' ")
                run = run.lower()
                if run == "yes":
                    print("You just located the treasure in the cave. Ye!\n You have won...")
                else:
                    print("You got so tired walking towards the cave.\n"
                          "This has made you weak and you have fainted along the way.\n"
                          "Sorry, you just lost the quest.\nGame Over!!!")
            else:
                print("You just got attacked by swarm of bees that have stung you to unconsciousness.\n"
                      "Sorry, you have lost the quest. Game Over!!!")
        else:
            print(
                "Your boat just got crushed by a big crocodile leaving you in the water to be killed by crocodiles.\n "
                "Game Over!!!")
    else:
        print("You were a good swimmer, but just got eaten by a crocodile. You have lost!!! ")
else:
    print("You just fell into a pit. You have lost!!!")





