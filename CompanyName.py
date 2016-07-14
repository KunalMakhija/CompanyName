#This is a fun program to come up with silly-ish ideas for a tech start up.
#It's based off a scene from the show Silicon Valley

import random

wordOne = ["Technology",
           "Clever",
           "Zen",
           "Square",
           "Circa",
           "Elevate",
           "Dream",
           "Chart",
           "Loco",
           "Quickly",
           "Insta",
           "Spark",
           "Clean",
           "Inside",
           "Change",]

wordTwo = [" Services",
           " Industries",
           " Machines",
           " Investing",
           " Media",
           " & Co.",
           "Hub",
           " Metrics"]


def name():
    confirm = input("Ready for your new company name? ").lower()
    if confirm == "yes":
        print ("Your new company's name is: " + (wordOne[random.randint(0, len(wordOne) - 1)]) + (wordTwo[random.randint(0, len(wordTwo) - 1)]))
    elif confirm != "yes":
        print ("Type yes or don't type anything at all! Jeez!")
    newName()
    

def newName():
    new = input("Want another name? ").lower()
    if new == "yes":
        name()
    elif new != "yes":
        quit()

name()
    
