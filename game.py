import random

def generate_word():
    word_list = ["chimp", "sweet", "stink", "noyou", "silly","rivka"]
    return random.choice(word_list)

def check_guess(secret, guess):
    feedback = ""
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            feedback += f"{guess[i].upper()} "
        elif guess[i] in secret:
            feedback += f"{guess[i].lower()} "
        else:
            feedback += "_ "
    return feedback.strip()

secret_word = generate_word()
print("Guess the 5-letter word!")
attempts = 0
while attempts < 6:
    guess = input("Enter your guess: ").strip().lower()
    if len(guess) != 5:
        print("Please enter a 5-letter word.")
        continue

    attempts += 1
    feedback = check_guess(secret_word, guess)
    print(feedback)
    if guess == secret_word:
        print("Congratulations, you've guessed the word!")
        break
else:
    print(f"Sorry, the word was {secret_word}.")
