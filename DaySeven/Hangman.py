#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
random_word = word_list[random.randint(0, len(word_list) - 1)]

#empty list
display = []

#each letter should be an underscore
for letter in random_word:
    display.append("_")

#print the underlines
print(display)

#end of game condition
end_of_game = False

#loop for game
while not end_of_game:

    #collect guess from the user
    guess = input("Guess a letter: ").lower()

    #loop for char checker
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win.")