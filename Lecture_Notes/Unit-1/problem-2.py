# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', 
# then your program should print:
    # Number of times bob occurs is: 2


s = 'azcbobobegghakl'
bob_count = 0

for x in range(len(s) - 2):
    if s[x] == 'b' and s[x + 1] == 'o' and s[x + 2] == 'b':
        bob_count+=1

print(f'Number of times bob occurs is: {bob_count}')