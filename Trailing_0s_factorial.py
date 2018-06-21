fac = int(input("Enter a number: "))
power = 1
zeroes = 0
calc = 1
while calc >= 1:
    calc = fac // 5**power #calculates the zeroes
    if calc < 1:
        continue
    zeroes += calc #stores the zeroes
    power += 1
print("The number of trailing 0s in the factorial of the number",fac,"are",zeroes)
