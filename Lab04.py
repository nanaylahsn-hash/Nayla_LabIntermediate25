wins = 0
losses = 0

word_list = ["monaco", "milan", "vienna", "geneva"]

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


print("🎮 Hangman Game Start")

while len(word_list) > 0:

    secret_word = word_list[0]
    word_list.remove(secret_word)

    guessed_letters = []

    print("\nNew Game Started!")

    while True:
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print("\nWord:", display_word)

        if display_word == secret_word:
            print("🎉 You win this round!")
            wins += 1
            break

        guess = input("Please input a letter: ").lower()

        if guess == "quit":
            print("\n🚪 You chose to quit.")
            print(f"Final Score → Wins: {wins}, Losses: {losses}")
            exit()

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
        print("Feedback:", feedback)

    print(f"Score → Wins: {wins}, Losses: {losses}")

    if len(word_list) == 0:
        print("\n🎮 No more words left!")
        break

    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again == "yes" or play_again == "y":
            break
        elif play_again == "no" or play_again == "n":
            print("\n🎯 Game Over")
            print(f"Final Score → Wins: {wins}, Losses: {losses}")
            exit()
        else:
            print(" -> Please answer yes or no!")

print("\n🎯 Game Over")
print(f"Final Score → Wins: {wins}, Losses: {losses}")
