import random

word_bank = [
    'uttarkhand', 'assam', 'karnataka', 'kerala', 
    'tamilnadu', 'maharashtra', 'madhya pradesh', 
    'odisha', 'jharkhand'
]

word = random.choice(word_bank)
guessedWord = ['_' if c != ' ' else ' ' for c in word]
attempts = 5

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))
    guess = input('Guess a letter: ').lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Ooo Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))

    if '_' not in guessedWord:
        print('\n Yay!! You guessed the word: ' + word)
        break

if attempts == 0 and '_' in guessedWord:
    print('\n uh oh You\'ve run out of attempts! The word was: ' + word)
