# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:09:59 2016

@author: ericgrimson

19 % 2 = 1  <- lowest bit (bit which is furthest right)
19 // 2 = 9
9 % 2 = 1  <- second lowest
9 // 2 = 4
4 % 2 = 0  <- 3 lowest
4 // 2 = 2
2 % 2 = 0 <- 4 lowest 
2 // 2 = 1
1 % 2 = 1  <- 5 highest
1 // 2 = 0  
END
Now put them in order (54321) = 10011
"""

num = 19

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
if isNeg:
    result = '-' + result
print(result)
