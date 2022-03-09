square = int(input('Enter Integer: '))

for guess in range(abs(square) + 1):
    if guess**2 >= abs(square):
        break

if guess**2 != abs(square):
    print(f'{square} is not a perfect cube')
else:
    if square < 0:
        guess = -guess
    print(f'Square root of {square} is {guess}')