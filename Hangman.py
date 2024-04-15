import random

from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo
print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
letters_guessed = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    letters_guessed.append(guess)

    if guess in display:
        print(f"You have already guessed {guess}")
        letters_guessed.remove(guess)

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"You have {lives} lives left")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(f"Here are the letters you have guessed so far: {letters_guessed}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman_art import stages
    print(stages[lives])
