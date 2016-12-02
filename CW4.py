from random import randint              (1)
x = [0,4,2,6,1,7,3]                     (1)

def rand_array(x):                      (1)
    for i in x:                         (n)
        j = randint(0,i)                (n)
        x[j], x[i-1] = x[i-1], x[j]     (n)
    return x                            (1) 
print(rand_array(x))                    (1)

Big O notation: O(n)

-------------------------------------------------------------------------------

fac = int(input("Enter a number: "))    (1)
power = 1                               (1)
zeroes = 0                              (1) 
calc = 1                                (1)
while calc >= 1:                        (n)
    calc = fac // 5**power              (n)
    if calc < 1:                        (n)
        continue                        (n?)
    zeroes += calc                      (n)
    power += 1                          (n)
print("The number of trailing 0s in the factorial of the number",fac,"are",zeroes)


Big O notation: O(n)
