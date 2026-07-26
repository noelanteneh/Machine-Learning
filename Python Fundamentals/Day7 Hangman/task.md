The Hangman project brings together many of the Python concepts learned so far. Instead of practicing each concept separately, this project combines them into a complete text-based game.

During this project, I practiced:

Variables to keep track of the game state.
Lists to store the secret word and the letters guessed so far.
Strings for comparing and displaying characters.
For loops to reveal correctly guessed letters.
While loops to keep the game running until the player wins or loses.
Conditional statements (if, elif, else) to check whether a guess is correct.
Functions to organize the code into reusable blocks.
Random module to choose a secret word from a list.
Importing modules by using helper files such as the word list and ASCII art.
Challenge

Build a text-based Hangman game where the player guesses one letter at a time.

Game Requirements
Randomly select a word from a predefined list.
Display blanks (_) for each letter in the word.
Ask the player to guess one letter each turn.
Reveal every occurrence of a correctly guessed letter.
Reduce the player's lives after an incorrect guess.
Prevent lives from decreasing when the player repeats a letter they have already guessed.
End the game when the player guesses the entire word or runs out of lives.
Display the appropriate Hangman stage after each incorrect guess.