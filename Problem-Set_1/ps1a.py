#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:43:14 2022

@author: sivnerof

See PDF in containing folder for problem set requirements
"""


annual_salary = float(input('Annual Salary: '))
portion_saved = float(input('Percentage To Be Saved As Decimal: '))
total_cost = float(input('Cost of your dream home: '))

portion_down_payment = 0.25
current_savings = 0
return_on_investment = 0.04

goal = portion_down_payment * total_cost
month = 0


while current_savings < goal:
    month += 1
    current_savings +=  portion_saved * (annual_salary / 12) + current_savings * return_on_investment / 12

print(f'{month} months')










