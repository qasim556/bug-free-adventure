# version 0.1.7
# time spent: ~ 7.5 hours

import random
import time

'''
level = 1
xp = 0
nextlevel = 25
hp = 30
gold = 0

while xp >= nextlevel:
    level += 1
    xp = xp - nextlevel
    nextlevel = round(nextlevel * 1.5)
    hp = round(hp * 1.25)
    gold += round(level * 1.2)

print("level:", level)
print("Exp:", xp)
print("Exp till next level:", nextlevel - xp)
print("Hp:", hp)
print("Gold:", gold)
# simpler version of xp code
'''

char = {"level": 1,
        "xp": 0,
        "nextlevel": 25,
        "hp": 30,
        "gold": 0}
# dictionary holding key values for the character

attack = random.randint(4, 8)
# players attack ranges from 4 to 8 damage
block = random.randint(1, 15)
# players block chance is 1 in 15


def level(char):  # function for running while loop
    while char["xp"] >= char["nextlevel"]:
        char["level"] += 1
        # increases level by 1
        char["nextlevel"] = round(char["nextlevel"] * 1.5)
        # adds 1.5 times more xp count for next level
        char["hp"] += round(char["level"] * 1.25)
        # adds 1.25 times more hp
        char["gold"] += round(char["level"] * 2.4)
        # gives player 1.2 times the level amount of gold
# occurs every time there is a level up


def stats():  # function for displaying stats
    print(name, "'s STATS")
    print("------")
    print("Level:", char["level"])
    print("Exp:", char["xp"])
    print("Exp till next level:", char["nextlevel"] - char["xp"])
    print("Total hp:", char["hp"])
    print("Gold:", char["gold"])
    print("------")


name = input("Please enter your characters name: ")

print("\nWelcome,", name, "you have a whole new world ahead of you\n")

time.sleep(2)
# wait time for reader
print("You have arrived to a small town and are being questioned by an innkeeper outside as they don't recognize you\n")
time.sleep(2)
input("'Where do you come from young one?'\n")

print("'Never heard of that place, but why are you here?'\n")
answer1 = input("a)Ran away from home\nb)Just for fun oldie\n")
if answer1.lower() == "a":
    print("'Well then, i guess we'll let you stay the night but you'll have to pay up next night!'\n")
    time.sleep(2)

elif answer1.lower() == "b":
    print("'Listen here bafoon, you're gonna end up dying here with that attitude and no knowledge'\n")
    time.sleep(2)
    print("'Since i'm a nice guy ill let you stay for free tonight but want to see some gold next time!'\n")
    time.sleep(2)

print("You head to your inn and go to bed\n")
time.sleep(2)
print("Suddenly, you hear noises outside, what do you do?\n")
answer2 = input("a)Go back to sleep\nb)Go investigate since you brought a knife with you from fleeing your old town\n")
if answer2.lower() == "a":
    print("You get back into bed hoping everything goes well\n")
    time.sleep(2)
    print("Lucky for you it does!\n")
    time.sleep(2)

elif answer2.lower() == "b":
    print("You go outside to investigate and hear a scream\n")
    time.sleep(2)
    print("You see a large creature trying to tear a woman apart\n")
    time.sleep(2)
    print("Sweat drips from your face in fear, quivering with a small knife, but what will you do?\n")
    answer3 = input("a)Run back to bed\nb)Try take that beast down like a true champ\n")
    if answer3.lower() == "a":
        print("Smart, you're not fully equipped to take it on right now\n")
        time.sleep(2)
        print("You let a woman die but got a decent night's rest, surprisingly\n")
        time.sleep(2)

    elif answer3.lower() == "b":
        print("You ready your knife and go in for the attack\n")
        time.sleep(2)
        print("You jump high and mighty and stab the creature in the back causing it to scream\n")
        time.sleep(3)
        print("The sun starts to rise and it runs away into the distant forest\n")
        time.sleep(3)
        print("'OMG thank you, you saved my life'\n")
        time.sleep(2)
        print("'You seem new here, take this!'\n")
        time.sleep(2)
        print("She gives you + 20 gold\n")
        char["gold"] += 20
        # adds 20 gold to player's gold count
        time.sleep(2)
        stats()
        # prints all current player stats

print("You wake up\n")
time.sleep(2)
print("You head outside and ask a town member how to make quick money as you have none\n")
time.sleep(3)
print("'The quickest way is the most dangerous but can definitely be worth it'\n")
time.sleep(3)
print("'You need to kill different creatures that drop gold and XP for levelling which, can make you stronger'\n")
time.sleep(3)
print("'See that small field in the distance, go there to start with and find your own way after that'\n")
time.sleep(3)
print("'Go have fun but be careful, and remember you can go to the shop to upgrade your gear'\n")
time.sleep(3)
# big intro to the game and how it works, they will figure out more as they go along
# give them a map? teleportation?
print("You thank him then proceed to the field where there are small slimes\n")
time.sleep(3)


slimeAtk = 0
# slimes attack ranges from 1 to 4 damage / it gets declared later within its loop
slimeBlock = random.randint(1, 17)
# slime has a block chance of 1 in 17
slimeHp = 10
# slime hp
slimeGold = random.randint(3, 6)
# slime drops 3 to 6 gold when killed
slimeXp = random.randint(5, 8)
# slime drops 5 to 8 xp when killed


def hp():
    if slimeHp <= 0:
        print("Your HP:", char["hp"], "\nEnemy : Defeated")

    else:
        print("Your HP:", char["hp"], "\nEnemy HP:", slimeHp)
        time.sleep(2)
        # shows players hp and enemy hp


def death():
    print("You have died\n")
    # add restart option later


def victory():
    char["hp"] = 30
    # sets hp back to what it started as / more efficient way needed due to level ups
    char["xp"] = char["xp"] + slimeXp
    char["gold"] = char["gold"] + slimeGold
    # adds gold and xp to players stats
    print("You gained +", slimeXp, "xp and +", slimeGold, "gold\n")
    # prints the amount of gold and xp gained
    time.sleep(2)


print("A slime appears, do you wish to\n")
answer4 = input("\na)Attack\nb)There is no running this time!\n")
time.sleep(2)
if answer4.lower() == "a" or "b":
    print("The battle has begun")
    print("--------------------")
    while char["hp"] > 0 and slimeHp > 0:  # while the player and enemy are alive
        if slimeBlock == 1:
            print("Your attack was blocked!\n")
            time.sleep(1)
            if block == 1:
                print("You blocked the enemy's attack!\n")
                time.sleep(1)
            else:
                slimeAtk = random.randint(1, 4)
                char["hp"] -= slimeAtk
                print("The enemy dealt", slimeAtk, "damage!\n")
                time.sleep(1)
                hp()
                input("\nPress any key to continue \n")
                time.sleep(0.5)
        else:
            attack = random.randint(4, 8)
            slimeHp = slimeHp - attack
            print("You dealt", attack, "damage!\n")
            time.sleep(1)
            if block == 1:
                print("You blocked the enemy's attack!\n")
                time.sleep(1)
            else:
                slimeAtk = random.randint(1, 4)
                char["hp"] -= slimeAtk
                print("The enemy dealt", slimeAtk, "damage!\n")
                time.sleep(1)
                hp()
                input("\nPress any key to continue \n")
                time.sleep(0.5)
    if char["hp"] <= 0:
        death()
        # runs death function
    if slimeHp <= 0:
        print("\nYou won the battle!\n")
        time.sleep(2)
        victory()
        # runs victory function

'''
else:
    print("Please enter either 'a' or 'b'\n")
    time.sleep(2)
    # need to make it loop back to start of section to allow them to enter the option again
'''

level(char)
# runs function to check if there is a level up
stats()
# prints current stats and adds any stats on if found from level function


# GAME PLAN / TO-DO LIST:
# ------------
# battle feature - try to add multiple moves that you can do
# battle feature - add a 'flee' feature to exit the battle but you lose 2% of your gold
# ------------
# companion feature - allows you to be accompanied by an 'animal' or NPC
# companion feature - could be purchased from the shop with gold or unlocked through missions
# ------------
# home (spawn) - contains NPC's, shops and an inn 
# home (spawn) - inn only needed if time system involved / could include day time + night time enemies
# ------------
# battle zone 1 - low level slimes spawn
# battle zone 2 - mid level slimes spawn WITH low level rats
# battle zone 3 - high level slimes spawn WITH mid level rats
# battle zone 4 - high level slimes spawn WITH high level rats WITH low level rodents
# battle zone 5 - high level slimes spawn WITH high level rats WITH mid level rodents
# battle zone 5 - mini boss stage / boss spawns after defeating 5 different enemies / boss drops gear
# ------------
# bugs - line 185 : needs the 'else' to loop back to the start of the multiple choice
# bugs - if multiple choice is answered incorrectly it skips the scenario / add a reply telling them to re-enter choice
# ------------
