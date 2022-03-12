# Please think of a number between 0 and 100!
# Is your secret number 50?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 75?
# Game over. Your secret number was: 83
# Sorry, I did not understand your input.

try:
    secret_number = int(input('Enter A Number Between 0-100 And I Will Guess It: '))
except:
    print('Must be an integer')

if secret_number > 99 or secret_number < 0:
    quit('Enter a valid integer BETWEEN 0-100 (100 not inclusive)')

high_point = 100
low_point = 0

while(True):
    guess = None
    mid_point = int((high_point + low_point) / 2)
    while(True):
        guess = input(f'Is your secret number {mid_point}? ')
        if guess == 'l' or guess == 'h' or guess =='c':
            break
        else:
            print('Sorry, I did not understand your input.')
    if guess == 'l':
        low_point = mid_point
    elif guess == 'h':
        high_point = mid_point
    elif guess == 'c':
        print(f'Game over. Your secret number was: {mid_point}')
        break
    print(f'high point = {high_point}')
    print(f'low point = {low_point}')
    print(f'mid point = {mid_point}')