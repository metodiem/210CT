number = int(input("Enter a number: "))
def Perfect(number):
    prf_sqr = 0
    while prf_sqr < number:
        if prf_sqr**2 > number:
            prf_sqr -= 1 #goes to the previous value
            print("The highest perfect square which is less or equal to", number, "is", prf_sqr**2)
            break
        prf_sqr += 1
Perfect(number)

''' PSUEDOCODE
PERFECT(number)
    m<-0
    while m < number
        if m*m > number
            m <- m - 1
            OUTPUT m*m
            break
        m++
'''
