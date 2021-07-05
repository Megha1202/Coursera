def computepay(h,r):
    if h>40:
       pay = rate1
    else:
        pay = rate2
    return pay
h = float(input("Enter Hours:"))
r = float(input("Enter Rate:"))
rate1 = 40 * r + (r * 1.5) * (h - 40)
rate2=h * r
pay = computepay(h,r)
print("Pay",pay)