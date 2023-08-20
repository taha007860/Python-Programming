# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 
# hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
if hours > 40:
   pay = rate * 40
   new_rate = rate * 1.5
   new_pay = (hours - 40) * new_rate
   finalPay = pay + new_pay
else:
    finalPay = hours * rate   
print("Pay:", finalPay)
