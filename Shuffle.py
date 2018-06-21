from random import randint
x = [0,4,2,6,1,7,3]

def rand_array(x):
    for i in x:
        j = randint(0,i)            #generates a random integer
        x[j], x[i-1] = x[i-1], x[j] #swaps the indexes
    return x
print(rand_array(x))
