print("***** HANGMAN *****")
import random

word_list = ["banana", "papaya", "mangoe", "apple", "peach", "grape", "watermelon", 
    "cherry", "strawberry","pineapple", "kiwi", "avocado", "pomegranate", "coconut", "lemon", "lime", "orange", "apricot", "plum", "nectarine", "fig", "date"]
chosen_word = random.choice(word_list)

display = []
for letter in range(len(chosen_word)):
    display += "_"

end_of_game = False
lives = 6
stages = ["You have no remaining lives.", "You have 1 remaining lives.", "You have 2 remaining lives.",
          "You have 3 remaining lives.", "You have 4 lives.", "You have 5 lives.", "You have 6 lives."]
while not end_of_game:
    guess = input("Guess a letter:").lower()
    if guess in display:
        print(f"You have already gussed: {guess}.")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"You have guessed {guess}, which is not in the word. You lose a life.")
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Win!")