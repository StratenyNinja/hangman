import os
import random
from words import THEMES, WORDS


HANGMAN = {
    0:
'''






''',
    1:
'''





  _________
''',
    2:
'''

 |
 |
 |
 |
 |_________
''',
    3:
'''
 __________
 |/
 |
 |
 |
 |_________
''',
    4:
'''
 __________
 |/      |
 |
 |
 |
 |_________
''',
    5:
'''
 __________
 |/      |
 |      ( )
 |
 |
 |_________
''',
    6:
'''
 __________
 |/      |
 |      ( )
 |       |
 |
 |_________
''',
    7:
'''
 __________
 |/      |
 |      ( )
 |      /|
 |
 |_________
''',
    8:
'''
 __________
 |/      |
 |      ( )
 |      /|\ 
 |
 |_________
''',
    9:
'''
 __________
 |/      |
 |      ( )
 |      /|\ 
 |      /
 |_________
''',
    10:
'''
 __________
 |/      |
 |      ( )
 |      /|\ 
 |      / \ 
 |_________
''',
}


def refresh_screen():
    os.system('cls')

def display_themes(themes):
    print('Choose a theme')
    for index, theme in enumerate(themes):
        if index % 5 == 0 and index > 0:
            print()
        print(f' {index+1}. {theme}', end='')
    print()

def display_hangman(wrong_guesses):
    print(HANGMAN[wrong_guesses])

def display_word(word, correct_letters):
    print(end=' ')
    for letter in word:
        if letter in correct_letters:
            print(letter.upper(), end='')
        elif letter == ' ':
            print(' ', end='')
        else:
            print('_', end='')
    print()

def display_available_letters(guessed_letters):
    print(end=' ')
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter in guessed_letters:
            print('_', end=' ')
        else:
            print(letter.upper(), end=' ')
    print()

def is_guessed(word, correct_letters):
    word = word.replace(' ', '')
    guessed_letters = [True for letter in word if letter in correct_letters]
    if guessed_letters.count(True) == len(word):
        return True
    else:
        return False

def find_theme(theme):
    try:
        index = int(theme)
        if index < len(THEMES):
            return index - 1
        else:
            return 'err'
    except ValueError:
        theme = theme.upper()
        if theme in THEMES:
            return THEMES.index(theme)
        else:
            return 'err'

def main():
    while True:
        guessed_letters = []
        correct_letters = []
        wrong_guesses = 0
        while True:
            display_themes(THEMES)
            theme = input()
            theme = find_theme(theme)
            refresh_screen()
            if theme == 'err':
                print('Theme does not exist.')
            else:
                word = random.choice(WORDS[theme])
                break
        while True:
            display_hangman(wrong_guesses)
            display_word(word, correct_letters)
            display_available_letters(guessed_letters)
            if is_guessed(word, correct_letters):
                print('YOU WON!')
                break
            elif wrong_guesses == 10:
                print('YOU LOST!')
                break
            else:
                guess = input('letter: ')
            if guess not in guessed_letters:
                guessed_letters.append(guess)
                if guess in word:
                    correct_letters.append(guess)
                else:
                    wrong_guesses += 1
            refresh_screen()

        print('The word was', word.upper())
        again = input('Do you want to play again? (Y/N): ')
        if again.lower() == 'n':
            break


if __name__ == '__main__':
    main()