#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:43:14 2022

@author: sivnerof
"""

# House Hunting

# 1. Call the cost of your dream home total_cost.
# 2. Call the portion of the cost needed for a down payment portion_down_payment.
# For simplicity, assume that portion_down_payment = 0.25 (25%).
# 3. Call the amount that you have saved thus far current_savings. 
# You start with a current savings of $0.
# 4. Assume that you invest your current savings wisely, 
# with an annual return of r 
# (in other words, at the end of each month, you receive an additional 
# current_savings*r/12 funds to put into your savings – 
# the 12 is because r is an annual rate). 
# Assume that your investments earn a return of r = 0.04 (4%).
# 5. Assume your annual salary is annual_salary.
# 6. Assume you are going to dedicate a certain amount of your 
# salary each month to saving for the down payment. 
# Call that portion_saved. 
# This variable should be in decimal form 
# (i.e. 0.1 for 10%).
# 7. At the end of each month, your savings will be increased by 
# the return on your investment,
# plus a percentage of your monthly salary (annual salary / 12).
# Write a program to calculate how many months it will take you to save up 
# enough money for a down payment. 
# You will want your main variables to be floats, 
# so you should cast user inputs to floats.


total_cost = float(input('Cost of your dream home: '))
annual_salary = float(input('Annual Salary: '))
portion_saved = float(input('Portion To Be Saved: '))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

goal = portion_down_payment * total_cost

while current_savings < goal:
    current_savings +=  portion_saved * annual_salary + current_savings * r / 12
    print(current_savings)










