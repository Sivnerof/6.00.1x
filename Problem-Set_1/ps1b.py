#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: sivnerof

See PDF in containing folder for problem set requirements
"""


annual_salary = float(input('Annual Salary: '))
portion_saved = float(input('Percentage To Be Saved As Decimal: '))
total_cost = float(input('Cost of your dream home: '))
semi_annual_raise = float(input('Semi annual raise, as decimal: '))

portion_down_payment = 0.25
current_savings = 0
return_on_investment = 0.04

goal = portion_down_payment * total_cost
month = 0


while current_savings < goal:
    month += 1
    if month % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise 
    current_savings +=  portion_saved * (annual_salary / 12) + current_savings * return_on_investment / 12

print(f'{month} months')