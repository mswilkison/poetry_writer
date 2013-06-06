import random
from Tkinter import *

def poemize():
    nouns = entryNoun.get().split(',')
    verbs = entryVerb.get().split(',')
    adjectives = entryAdjective.get().split(',')
    prepositions = entryPreposition.get().split(',')
    adverbs = entryAdverb.get().split(',')

    noun1 = random.choice(nouns)
    noun2 = random.choice(nouns)
    noun3 = random.choice(nouns)
    while noun2 == noun1:
        noun2 = random.choice(nouns)
    while noun3 == noun1 or noun3 == noun2:
        noun3 = random.choice(nouns)

    verb1 = random.choice(verbs)
    verb2 = random.choice(verbs)
    verb3 = random.choice(verbs)
    while verb2 == verb1:
        verb2 = random.choice(verbs)
    while verb3 == verb1 or verb3 == verb2:
        verb3 = random.choice(verbs)

    adjective1 = random.choice(adjectives)
    adjective2 = random.choice(adjectives)
    adjective3 = random.choice(adjectives)
    while adjective2 == adjective1:
        adjective2 = random.choice(adjectives)
    while adjective3 == adjective1 or adjective3 == adjective2:
        adjective3 = random.choice(adjectives)

    adverb = random.choice(adverbs)

    preposition1 = random.choice(prepositions)
    preposition2 = random.choice(prepositions)
    while preposition2 == preposition1:
        preposition2 = random.choice(prepositions)

    if adjective1[0] in ['a', 'e', 'i', 'o', 'u']:
        start = 'An'
    else:
        start = 'A'

    myPoem = "{start} {adjective1} {noun1} \n {start} {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2} \n {adverb}, the {noun1} {verb2} \n the {noun2} {verb3} {preposition2} a {adjective3} {noun3}".format(start=start, noun1=noun1, noun2=noun2, noun3=noun3, adjective1=adjective1, adjective2=adjective2, adjective3=adjective3, preposition1=preposition1, preposition2=preposition2, verb1=verb1, verb2=verb2, verb3=verb3, adverb=adverb)
    resultPoem.config(text=myPoem)

window = Tk()
frame = Frame()
frame.pack()

# label enter words into each list, separated by a ','
labelInstructions = Label(frame, text="Enter words into each list, separated by a ','.",
			  relief=RAISED)
labelInstructions.grid(row=1, column=2)

labelNoun = Label(frame, text="Nouns:")
labelNoun.grid(row=2, column=1, sticky=W)
entryNoun = Entry(frame)
entryNoun.grid(row=2, column=2, sticky=W)

labelVerb = Label(frame, text="Verbs:")
labelVerb.grid(row=3, column=1, sticky=W)
entryVerb = Entry(frame)
entryVerb.grid(row=3, column=2, sticky=W)

labelAdjective = Label(frame, text="Adjectives:")
labelAdjective.grid(row=4, column=1, sticky=W)
entryAdjective = Entry(frame)
entryAdjective.grid(row=4, column=2, sticky=W)

labelPreposition = Label(frame, text="Prepositions:")
labelPreposition.grid(row=5, column=1, sticky=W)
entryPreposition = Entry(frame)
entryPreposition.grid(row=5, column=2, sticky=W)

labelAdverb = Label(frame, text="Adverbs:")
labelAdverb.grid(row=6, column=1, sticky=W)
entryAdverb = Entry(frame)
entryAdverb.grid(row=6, column=2, sticky=W)

btnPoemize = Button(frame, text="Create Poem", command=poemize)
btnPoemize.grid(row=7, column=2, rowspan=2)

resultPoem = Label(frame)
resultPoem.grid(row=8, column=2, rowspan=2)

# split() to generate words lists
# grid layout w/ labels for nouns, verbs, adjectives, prepositions, and adverbs
# create your poem button centered at bottom, that generates and displays random poem on click in a label below button
# if not enough words supplied display an error message
# add Save your poem button centered below that as .txt with Save As dialog box; add default .txt extension and allow cancel

window.mainloop()




