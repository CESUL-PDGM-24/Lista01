from random import choice


def draw_word() -> str:
    word_list = ['moises', 'cajado', 'mar', 'porta', 'monitor']
    return choice(word_list)


def handle_input() -> str:
    guess = input("Informe seu palpite: ")
    return guess.lower()


def is_single_letter(guess: str) -> bool:
    return len(guess) == 1


def validate_guess(guess: str, guess_word: list) -> bool:
    if not guess.isalpha():
        print("Você deve informar uma letra ou a palavra inteira!")
        return False

    if is_single_letter(guess) and guess in guess_word:
        print("Você já adivinhou esta letra!")
        return False

    return True


def show_error(errors: int) -> int:
    print("Palpite incorreto!")
    errors += 1
    return errors


def check_guess(guess: str, errors: int, selected_word: str, guess_word: list) -> (int, bool):
    found_word = False

    if is_single_letter(guess) and guess in selected_word:
        for i, letter in enumerate(selected_word):
            if guess == letter:
                guess_word[i] = letter

        found_word = "_" not in guess_word
    elif guess == selected_word:
        found_word = True
    else:
        errors = show_error(errors)

    return errors, found_word
