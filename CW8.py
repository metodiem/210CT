vowels = ["a","e","i","o","u","A","E","I","O","U"]
s = "beautiful"
def VOWEL_DEL(s, vowels, i):
    if len(s) == i:
        print(s)
        return
    elif s[i] in vowels:           #checks if the char on position i is in the list
        s = s.replace(s[i],"")     #removes the character
        VOWEL_DEL(s,vowels,i)      #calls the function for the same value of i
    else:
        VOWEL_DEL(s,vowels,i+1)
VOWEL_DEL(s,vowels,0)

'''
VOWEL_DEL(s,vowels,i)
    IF lenght(s) = i
        return s
    ELSE IF s[i] in vowels
        remove s[i]
        VOWEL_DEL(s,vowels,i)
    ELSE
        VOWEL_DEL(s,vowels,i++)
'''
