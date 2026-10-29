n = int(input("Enter a number: "))
temp = n
total = 0
power = len(str(n))
while temp > 0:
    digit = temp % 10
    total = total + digit ** power
    temp = temp // 10
if n >= 0 and total == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong number")