import random
import time
import os
import sys

try:
    import pyttsx3
except ImportError:
    os.system("pip3 install pyttsx3")

# Initializing the pytts engine
engine = pyttsx3.init()

# Changing the voice of the TTS to a female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Changing the speed of the voice
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)

# Introduction to the game
os.system("cls")
one = "\n\nWelcome to Spelling Bee!"
for char in one:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
time.sleep(2)

two = "\n\nI made this because I got qualified for my school's Spelling Bee but it got cancelled due to COVID-19."
for char in two:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
time.sleep(3)

three = "\nand because I was bored..."
for char in three:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.005)
time.sleep(1)

os.system("cls")
four = "\n\nAnyways, prepare yourself for the spelling bee competition!"
for char in four:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
time.sleep(2)

os.system("cls")

print("""
Rules:
- Capitalization doesn't matter!
- The word will be repeated 3 times, before you are asked to spell it.
""")

time.sleep(5)

os.system("cls")


# The actual game
while True:
    wordsList = [
        "plaintiff",
        "posthumous",
        "controversy",
        "unsanitary",
        "precipitate",
        "belligerent",
        "serviceable",
        "scandalized",
        "unenforceable",
        "potpourri",
        "metamorphosis",
        "caricature"
    ]

    word = random.choice(wordsList)

    engine.say(word)
    engine.runAndWait()
    time.sleep(3)

    engine.say(word)
    engine.runAndWait()
    time.sleep(3)
    
    engine.say(word)
    engine.runAndWait()

    usersSpelling = input("\n\nEnter the spelling of the word: ")
    usersSpelling = usersSpelling.lower()

    if usersSpelling == word:
        print("\n\nYou guessed the word's spelling correctly!")
        time.sleep(2)
        os.system("cls")
    else:
        print("\n\nYou guessed the word's spelling incorrectly!")
        time.sleep(2)
        os.system("cls")
