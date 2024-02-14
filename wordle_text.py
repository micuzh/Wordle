# Name: Michael Zhu
# UTEID: mz9384
#
# On my honor, Michael Zhu, this programming assignment is my own work
# and I have not provided this code to any other student.

import random


def main():

    """ Plays a text based version of Wordle.
        1. Read in the words that can be choices for the secret word
        and all the valid words. The secret words are a subset of
        the valid words.
        2. Explain the rules to the player.
        3. Get the random seed from the player if they want one.
        4. Play rounds until the player wants to quit.
    """
    secret_words, all_words = get_words()
    welcome_and_instructions()

    replay = 'Y'

    while replay.upper() == 'Y':

        secret_word = (secret_words[random.randrange(len(secret_words))]).upper()
        unused_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'
                                , 'k', 'l', 'm', 'n', 'o', 'p', 'q','r'
                                , 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        progress = []
        tries = 0
        win = False
        
        while tries < 6:
            tries += 1
            revealed = '-----'

            guess = input('\nEnter your guess. A 5 letter word: ').upper()
            if guess not in all_words:
                print()
                print(guess, 'is not a valid word. Please try again.')
                tries -= 1
                continue

            freq = {}
            for letter in secret_word: #dict of occurences of letter, like a mapping to frequency
                freq[letter] = freq.get(letter, 0) + 1

            for i in range(0,5):
                if guess[i].lower() in unused_letters: #update letters list
                    unused_letters.remove(guess[i].lower())
                if guess[i] == secret_word[i]: #update revealed
                    revealed = revealed[:i] + 'G' + revealed[i + 1:]
                    freq[guess[i]] = freq.get(guess[i], 0) - 1

            for i in range(0,5):
                if guess[i] in secret_word and revealed[i] != 'G' and freq[guess[i]] > 0:
                    revealed = revealed[:i] + 'O' + revealed[i + 1:] #STRAP, POOOP
                    freq[guess[i]] = freq.get(guess[i], 0) - 1


            progress.append(revealed)
            progress.append(guess)

            print()
            for line in progress:
                print(line)
            print('\nUnused letters: ', end='')

            result = ' '.join(letter.upper() for letter in unused_letters)
            print(result)
            
            if revealed == 'GGGGG':
                win = True
                break

        commentary = ('Genius!', 'Magnificent!', 'Impressive!', 'Splendid!'
                        , 'Great!', 'Phew!')
        if win:
            print('\nYou win.', commentary[tries - 1])
        else:
            print('\nNot quite. The secret word was ', secret_word, '.',sep='')

        replay = input('\nDo you want to play again? Type Y for yes: ')



def welcome_and_instructions():
    """
    Print the instructions and set the initial seed for the random
    number generator based on user input.
    """
    print('Welcome to Wordle.')
    instructions = input('\nEnter y for instructions, anything else to skip: ')
    if instructions == 'y':
        print('\nYou have 6 chances to guess the secret 5 letter word.')
        print('Enter a valid 5 letter word.')
        print('Feedback is given for each letter.')
        print('G indicates the letter is in the word and in the correct spot.')
        print('O indicates the letter is in the word but not that spot.')
        print('- indicates the letter is not in the word.')
    set_seed = input(
        '\nEnter y to set the random seed, anything else to skip: ')
    if set_seed == 'y':
        random.seed(int(input('\nEnter number for initial seed: ')))


def get_words():
    """ Read the words from the dictionary files.
        We assume the two required files are in the current working directory.
        The file with the words that may be picked as the secret words is
        assumed to be names secret_words.txt. The file with the rest of the
        words that are valid user input but will not be picked as the secret
        word are assumed to be in a file named other_valid_words.txt.
        Returns a sorted tuple with the words that can be
        chosen as the secret word and a set with ALL the words,
        including both the ones that can be chosen as the secret word
        combined with other words that are valid user guesses.
    """
    temp_secret_words = []
    with open('secret_words.txt', 'r') as data_file:
        all_lines = data_file.readlines()
        for line in all_lines:
            temp_secret_words.append(line.strip().upper())
    temp_secret_words.sort()
    secret_words = tuple(temp_secret_words)
    all_words = set(secret_words)
    with open('other_valid_words.txt', 'r') as data_file:
        all_lines = data_file.readlines()
        for line in all_lines:
            all_words.add(line.strip().upper())
    return secret_words, all_words


if __name__ == '__main__':
    main()
