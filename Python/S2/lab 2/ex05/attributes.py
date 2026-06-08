n = int(input("give me a number: "))

if n == 42:
    print("number is 42")
if n >= 0:
    print("number is positive")
if n % 7 == 0:
    print("number is dividable through 7")
if n % 2 == 0:
    print("number is even")
if 18 <= n <= 65:
    print("number is between 18 and 65")
l = len(str(n))
m = n
product = 0
for i in range(l):
    product += m % 10
    m = m // 10
if product < 10:
    print("cross sum is smaller than 10")

if l > 5 and n % 10 == 3:
    print("number has more than 5 digits and ends on a 3")