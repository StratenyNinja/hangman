import random


WORDS = ['dog', 'cat', 'hangman']

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


def display_hangman(wrong_guesses):
    print(HANGMAN[wrong_guesses])

def display_available_letters(guessed_letters):
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter in guessed_letters:
            print('_', end=' ')
        else:
            print(letter.upper(), end=' ')
    print()

def display_word(word, correct_letters):
    for letter in word:
        if ' ' in word:
            print(' ', end='')
        if letter in correct_letters:
            print(letter.upper(), end='')
        else:
            print('_', end='')
    print()


def main():
    while True:
        word = random.choice(WORDS)
        guessed_letters = []
        correct_letters = []
        wrong_guesses = 0
        while True:
            display_hangman(wrong_guesses)
            display_word(word, correct_letters)
            display_available_letters(guessed_letters)
            if len(correct_letters) == len(word):
                print('YOU WON!')
                break
            elif wrong_guesses == 10:
                display_hangman(wrong_guesses)
                print('YOU LOST!')
                print('The word was', word.upper())
                break
            else:
                guess = input('letter: ')
            if guess not in guessed_letters:
                guessed_letters.append(guess)
            if guess in word:
                correct_letters.append(guess)
            else:
                wrong_guesses += 1

        again = input('Do you want to play again? (Y/N): ')
        if again.lower() == 'n':
            break


if __name__ == '__main__':
    main()