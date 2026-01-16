secret_word = 'timeless'
guessed_letters = []
attempts = 6

while True:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Attempts left:", attempts)

    if display_word == secret_word:
        print("Congratulations! You guessed the secret word! 🎉")
        break

    if attempts == 0:
        print("Game Over! The word was:", secret_word)
        break

    user_input = input("Please input a letter: ").lower()

    if len(user_input) != 1:
        print(" -> Please input only one letter!")
        continue

    if not user_input.isalpha():
        print(" -> Input is not a valid alphabet!")
        continue

    if user_input not in guessed_letters:
        guessed_letters.append(user_input)

        if user_input in secret_word:
            print(" -> Correct letter!")
        else:
            print(" -> Wrong letter!")
            attempts -= 1
    else:
        print(" -> You already guessed that letter!")