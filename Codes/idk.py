import random

#suits split so the lines arent super long
spades = ["Ace of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades"]
hearts = ["Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts"]
diamonds = ["Ace of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds"]
clubs = ["Ace of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs"]
plainDeck = spades + hearts + diamonds + clubs

playersHand = []

def getACard(doPrint, repeats):
    #We need to get a new card that is not in play everytime this runs
    usedCards = []
    int(repeats)
    for i in range(repeats):
        possibleCard = random.choice(plainDeck)
        while possibleCard in usedCards: #check if the card is in use, redo if it is
            possibleCard = random.choice(plainDeck)
        if possibleCard not in usedCards:
            playersHand.append(possibleCard)
            usedCards.append(possibleCard)
        else:
            print("Sorry, somethingwent wrong with the card " + possibleCard)
            quit()
    if doPrint == True:
        print("Your hand:")
        print(playersHand[0])
        print(playersHand[1])
print("")
getACard(True, 2)
print("")

