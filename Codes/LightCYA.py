import random
import time
enemies = ["Goblin", "Slime", "Bandit"]
places = ["Thramdor", "Mysticana", "Oakstead", "Shadowspire", "Pyrophoria", "Luminasia"]
startYear = random.randint(2100, 3000)
startLocation = places[random.randint(0, 2)]
classes = ["Wizard", "Warrior", "Rouge"]
attackWords = ["Cast", "Slash", "Stab"]
classesNum = ["1", "2", "3"]

def say(sayWhat):
    print("")
    print(sayWhat)
    time.sleep(2)

promptTypes = ["e", "f", "t", "q"]
def prompt(promptType):
    if promptType == "encounter" or "e":
        print("1")
    elif promptType == "friendly" or "f":
        print("2")
    elif promptType == "trader" or "t":
        print("3")
    elif promptType == "quest" or "q":
        types = ["fetch" or "f", "attack" or "a", "escort" or "e"]
        print(str(questType = random.choice(types)))
    else:
        promptType = random.choice(promptTypes)
prompt("q")
prompt("f")
print()
print("Which class are you? (Put the number)")
print("1. Wizard")
print("2. Warrior")
print("3. Rogue")
rpgClassNum = input("")
classTries = 0
rpgClass = ""
while rpgClassNum not in classesNum:
    classTries = classTries + 1
    if classTries > 4:
        rpgClassNum = random.choices(classes)
        print("It seems like you need help, you are now a" + str(rpgClass))
        break
    else:
        print("Please pick 1, 2, or 3")
        rpgClassNum = input("")   
rpgClass = classes[classesNum.index(rpgClassNum)]
attackWord = attackWords[classes.index(rpgClass)]
rpgClass = str(rpgClass)
huntingEnemyType = random.choice(enemies)
huntingEnemyNum = 5
say("The year is " + str(startYear) + ", you are a " + rpgClass + " of " + startLocation + ".")
say("You have been tasked with going out and killing " + str(huntingEnemyNum) + " " + huntingEnemyType + "s")
say("You head out to the forest and explore a bit, when you see " + str(random.randint(2, huntingEnemyNum))+ " " + huntingEnemyType + "s.")

print("What do you do?")
print("1. Heads on attack")
print("2. Watch them to gain info")
print("3. Sneak attack them")
