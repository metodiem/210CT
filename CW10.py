sequence = [1,3,4,7,2,5,1,6,8,11,13,2,1]
a = []
b = []
for i in range(0,len(sequence)):       #loop in range of sequence
    if i == len(sequence)-1:           #If i has reached the last element append to a
        a.append(sequence[i])
    elif sequence[i] < sequence[i+1]:  #If the next element is higher append current element
        a.append(sequence[i])
    elif sequence[i] >= sequence[i+1]:
        a.append(sequence[i])
        if len(b) == 0:
            b.append(a[0::])
        elif len(b) != 0:
            if len(b) > len(a):
                a = []
            elif len(b) < len(a):
                b = []
                b.append(a[0::])
                a = []
print(b)
        
        
