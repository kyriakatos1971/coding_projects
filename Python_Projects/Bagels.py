"""Bagels, by Al Sweigart al@inventwithpython.com
 2. A deductive logic game where you must guess a number based on clues.
 3. View this code at https://nostarch.com/big-book-small-python-projects
 4. A version of this game is featured in the book "Invent Your Own
 5. Computer Games with Python" https://nostarch.com/inventwithpython
 6. Tags: short, game, puzzle"""

from pickle import TRUE
import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def getSecretNum():
    numbers = list('0123456789')  #Create a list of digits
    random.shuffle(numbers)

    secretNum = ''

    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum



def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Correct!'
    clues=[]

    for i in range(len(guess)):
        if guess[i]==secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues)==0:
        return 'Bagels'
    else: 
        clues.sort()
        return ' '.join(clues)






 

def main():
     print('''Bagels, a deductive logic game.
              By Al Sweigart al@inventwithpython.com
               I am thinking of a {}-digit number with no repeated digits.
              Try to guess what it is. Here are some clues:
              When I say:    That means:
              Pico         One digit is correct but in the wrong position.
              Fermi        One digit is correct and in the right position.
              Bagels       No digit is correct.

              For example, if the secret number was 248 and your guess was 843, the
             clues would be Fermi Pico.'''.format(NUM_DIGITS))

     while True:
        secretNum = getSecretNum()
        print('I have though of a number')
        print('You have {} guesses to win.'.format(MAX_GUESSES))


        numGuesses  = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''

            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input ('>>')
        

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses +=1

            if guess == secretNum:
                 break

            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(' the correct answer was {}: '.format(secretNum))

        print('Do you want to play again? (y/n)')
        if not input('>>').lower().startswith('y'):
         break
    
print ('Thanks for playing!')




if __name__ == '__main__':
        main()



