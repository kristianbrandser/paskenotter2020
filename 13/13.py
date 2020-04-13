import numpy as np


def isPalindrome(number):
    #ndigits = len(str(number))
    if (str(number) == (str(number)[::-1])):
        return True    
    else:
        return False

def addReverse(number):
    sum = number + int(str(number)[::-1])
    return sum

def isMeaningfulPaldinrome(number, nReversals):
    reversedsum = number
    
    for reversals in range (1,nReversals+1):
        reversedsum = addReverse(reversedsum)
        #print("Reversal: ", reversals)
        #print("Reversedsum: ", reversedsum)

        if ((reversals == nReversals) and (isPalindrome(reversedsum))):
            #print("Found meaningfulreversedsum: ", reversedsum)
            return True
    return False

#Om du legg saman eit tal med reversen av seg sjølv får du ein sum. 
#Av og til er summen eit palindrom. 
# Om den ikkje er det, kan vi gjenta prosessen igjen og igjen. 
# Til slutt endar vi opp med eit palindrom. 
# Dette gjeld for dei fleste tal, men vi veit ikkje om det gjeld for alle tal*.
#Kva er summen av alle tal fra og med 1 og til og med 10 000 000 som endar opp som 
# palindrom etter nøykatig 42 iterasjonar?


meaningfulNumbers = []

for number in range(1,10000000): #10000000
    if (isMeaningfulPaldinrome(number,42)):
        print("Found meaningfulnumber: ", number)
        meaningfulNumbers.append(number)
  
#Sum all meaningfulPalindromes found
np.savetxt("13/13.csv", meaningfulNumbers, fmt='%d', delimiter=',')
meaningfulSum = np.sum(meaningfulNumbers)
print("Svaret er: ", meaningfulSum)

#print(isPalindrome(101010414010101))
#print(isMeaningfulPaldinrome(42,1))
#print(isMeaningfulPaldinrome(64,3))

#print(isMeaningfulPaldinrome(10070,42))
#print(isMeaningfulPaldinrome(9998289,42))