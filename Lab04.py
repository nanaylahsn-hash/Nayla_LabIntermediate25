def updateText(secret_word, guessed_letters, guess):
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    if guess in secret_word:
        feedback = f"Congrats, '{guess}' is correct!"
    else:
        feedback = f"Sorry, '{guess}' is not in the word."

    return display_word, feedback


secret_word = "monaco"
guessed_letters = []

print("Hangman Game Start")

while True:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)

    if display_word == secret_word:
        print("Congratulations! You guessed the secret word!")
        break

    guess = input("Please input a letter: ").lower()

    if len(guess) != 1:
        print(" -> Please input only one letter!")
        continue

    if not guess.isalpha():
        print(" -> Input is not a valid alphabet!")
        continue

    if guess in guessed_letters:
        print(" -> You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    display_word, feedback = updateText(secret_word, guessed_letters, guess)

    print("Word:", display_word)
    print("Feedback:", feedback)