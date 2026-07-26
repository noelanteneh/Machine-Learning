import random
from hangman_words import word_list
from hangman_art import stages,logo
lives = 6
game_over = False
while not game_over:

    chosen_word = random.choice(word_list)
    print(chosen_word)
    print(logo)

    placeholder = ""
    word_length = len(chosen_word)
    for position in range(word_length):
        placeholder += "_"
    print("Word to guess: " + placeholder)

    game_over = False
    correct_letters = []
    guesses_letters = []

    while not game_over:


        print(f"****************************{lives}/6 LIVES LEFT****************************")
        guess = input("Guess a letter: ").lower()
        if guess in guesses_letters:
            print("You already guessed this letter")
            lives += 1
        guesses_letters.append(guess)

        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + display)



        if guess not in chosen_word:
            print(f"the letter {guess} is not in the word")
            lives -= 1

            if lives == 0:
                game_over = True
                print(f"***********************YOU LOSE**********************")

                print(f"the correct word was {chosen_word}")

        if "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")


        print(stages[lives])
