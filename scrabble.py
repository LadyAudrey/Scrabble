# Guessing word Game to replace MIT 600 scrabble game
import twl
import random

score = 0
letter = int(0)
done = ('done', 'Done', 'DONE')

alphabet = ["a", "a", "b", "c", "d", "e", "e", "f", "g",
            "h", "i", "i", "j", "k", "l", "m", "n", "o", "o",
            "p", "q", "r", "s", "t", "u", "u", "v", "w", "x", "y", "z", ]

# Assign point values to each letter
SCRABBLE_LETTER_VALUES = {}
for key in ["a", "e", "i", "l", "n", "o", "r", "s", "t", "u"]:
    SCRABBLE_LETTER_VALUES[key] = 1
for key in ["d", "g"]:
    SCRABBLE_LETTER_VALUES[key] = 2
for key in ["b", "c", "m", "p", ]:
    SCRABBLE_LETTER_VALUES[key] = 3
for key in ["f", "h", "v", "w", "y"]:
    SCRABBLE_LETTER_VALUES[key] = 4
for key in ["k"]:
    SCRABBLE_LETTER_VALUES[key] = 5
for key in ["j", "x"]:
    SCRABBLE_LETTER_VALUES[key] = 8
for key in ["q", "z"]:
    SCRABBLE_LETTER_VALUES[key] = 10

# Creating output/ input for hand and words
print("Let's play a Word Game")
hand = random.choices(alphabet, k=7)
print("Your random letters are " + (str(hand)))

while input != [done]:
    word = input("Enter a word, please. When you have no more words, type 'done'\n")

    invalid_letters = []
    for letter in word:
        if letter not in hand:
            invalid_letters.append(letter)

    if invalid_letters:
        print("Found invalid letters: ")
        for invalid_letter in invalid_letters:
            print(f"{invalid_letter} ", end="")
        print()
        continue

    if twl.check(word):
        print("Excellent, that is a valid word.")
    else:
        print("I'm sorry, but that is not a valid word. Would you like to guess again?")
        continue

    # Taking the input and scoring it
    # for len(letters):
    for letter in word:
        points = SCRABBLE_LETTER_VALUES[letter]
        print(f"Letter {letter} was worth {points} points")
        score = score + points
        if len(word) == 7:
            score = score + 50

    break

print(f"Score is: {score}")