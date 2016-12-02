number = int(input("Enter a number: "))
count = number -1
def PRIME(number,count):
    if (number <= 1):
        print("Prime numbers can only be integers greater than 1")
        return
    elif number % count == 0 and number != 2: #checks if the remainder is 0
        print("Number is not prime")
        return
    elif count == 2 and number % count != 0 or number == 2: #checks if the remainder is not 0
        print("Number is prime")
        return
    PRIME(number, count-1)
PRIME(number,count)

'''
PRIME(number,count)
    IF number <= 1
        OUTPUT Prime numbers can only be integers greater than 1
        return
    ELSE IF number % count <- 0 and number != 2
        OUTPUT Number is not prime
        return
    ELSE IF
        count = 2 and number % count != 0 or number = 2
        OUTPUT Number is prime
        return
    PRIME(number, count-1)
'''
