try:
    secret_number = int(input('Please think of a number between 0 and 100! '))
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
        print(f'Is your secret number {mid_point}? ')
        print("Enter 'h' to indicate the guess is too high.", end='') 
        print("Enter 'l' to indicate the guess is too low.", end='') 
        print("Enter 'c' to indicate I guessed correctly.", end='')
        guess = input(' ')

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