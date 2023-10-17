import hangman
import random


def main():
    hangman_pics = hangman.HANGMANPICS
    words_bank = hangman.WORDBANK
    word = choose_word(words_bank)
    print(word)
    unresolved = list(unresolved_word(word))
    tries = 0
    while True:
        user_input = input("Please enter letter")
        result = game(word, unresolved, user_input)

        if result[1] == False:
            tries = tries + 1
            print("Your try: ", tries)
            print(*result[0])
            print(hangman_pics[tries])
        else:
            print(*result[0])
            print(hangman_pics[tries])

        if tries == 6:
            print("game over")
            break
        if check_result(unresolved) == True:
            break


def check_result(unresolved):
    if "_" not in unresolved:
        print("You won!")
        return True


def game(word, unresolved, user_input):
    for i, letter in enumerate(word):
        if letter == user_input:
            unresolved[i] = letter
    if user_input not in word:
        return unresolved, False
    else:
        return unresolved, True


def unresolved_word(word):
    unresolved_word = ""
    for _ in range(len(word)):
        unresolved_word = unresolved_word + "_"
    return unresolved_word


def choose_word(words_bank):
    word = random.choice(words_bank)
    return word


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()
