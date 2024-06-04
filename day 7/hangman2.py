word_list = ["ardvark", "baboon", "camel"]
import random

chosen_word = random.choice(word_list)
print(f"psstt, the word is {chosen_word}")

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("wrong")
        