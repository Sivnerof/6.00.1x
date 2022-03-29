def square(x):
    return x * x

def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    return square(square(x))

result = fourthPower(int(input('Enter a number: ')))
print(result)