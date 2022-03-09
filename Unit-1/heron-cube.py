cube = int(input('Enter Integer: '))

for guess in range(abs(cube) + 1):
    if guess**3 >= abs(cube):
        break

if guess**3 != abs(cube):
    print(f'{cube} is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print(f'Cube root of {cube} is {guess}')