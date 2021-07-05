hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter Rate:"))
rate2=h * rate
rate1 = 40 * rate + (rate * 1.5) * (h - 40)
if h > 40:
    pay = rate1
else:
    pay = rate2
print(pay)