sentence = "This is awesome"

def reverse_string(sentence):
    
    words = sentence.split()                        #splits the string into a list
    for i in range(1,(len(words)+2)//2):            #loops through half the list
        words[i-1],words[-i] = words[-i],words[i-1] #reverses the position of the indexes  
    reversed_sentence = " ".join(words)             #converts the list into a string
    return reversed_sentence

print(reverse_string(sentence))

'''
REVERSE_STRING(sentence)
    words = split sentence into an array
    for i<- 1 to (words.size()+2)//2
        reverse the position of i-1 and -i
    reversed_sentence = convert the array into a string
    RETURN reversed_sentence
'''
Big O notation: O(n)

