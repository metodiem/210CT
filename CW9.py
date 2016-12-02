sequence = [2,3,8,16,20,22,23,25,28]
low = int(input("low: "))
high = int(input("high: "))
ending = len(sequence)-1
def bsearch(sequence,low,high,beginning,ending):
    mid = (ending + beginning) // 2                     #Find the middle value of the sequence
    if sequence[mid] >= low and sequence[mid] <= high:
        print("True")
        return
    elif beginning+1 == ending:      #If the lenght of the interval == 1 return False
        print("False")
        return
    elif sequence[mid] < low:        #Forget about the bottom half
        beginning = mid
        bsearch(sequence,low,high,beginning,ending)
    elif sequence[mid] > high:       #Forget about the top half  
        ending = mid
        bsearch(sequence,low,high,beginning,ending)

bsearch(sequence,low,high,beginning,ending)

#Big O notation: O(log n)
