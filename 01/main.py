from functions import *


if __name__ == '__main__':
    errors = 0
    found_word = False

    selected_word = draw_word()
    guess_word = ["_" for _ in selected_word]

    while errors != 3 and not found_word:
        print(' '.join(guess_word))
        guess = handle_input()

        if not validate_guess(guess, guess_word):
            continue

        errors, found_word = check_guess(guess, errors, selected_word, guess_word)

    if found_word:
        print("Parabéns, você acertou!")
    else:
        print(f"Você foi enforcado! A palavra sorteada era: {selected_word}")
