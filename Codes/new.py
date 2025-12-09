import random

lowercaseLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercaseLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
punc = ['!','.',',','?']
bothLetters = uppercaseLetters + lowercaseLetters
space = " "
word = ""
words = []
def speak():
    wordLength = random.randint(2,20)
    sentenceLength = random.randint(7,1000)
    i = 0
    word = ""
    while i < wordLength:
        i += 1
        currentLetter = random.choice(bothLetters)
        word = word + currentLetter
    word = word + space
    print(word)
    print("Was that a real word? y, n, print, or sentence")
    yesOrNo = input("")
    if yesOrNo == "y":
        words.append(word)
    elif yesOrNo == "print":
        for eachWord in words:
            print(eachWord)
    elif yesOrNo == "sentence":
        i = 0
        sentence = ""
        while i < sentenceLength:
            i += 1
            currentWord = random.choice(words)
            sentence = sentence + currentWord
        puctuation = random.choice(punc)
        print(sentence + puctuation)
    print("")

x = 0
while x == x:
    speak()