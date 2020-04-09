import numpy as np

Numbers = np.genfromtxt("09/numbers.txt", dtype=int, delimiter=',')
sNumbers = np.sum(Numbers)

sAllNumbers = ((Numbers.size+1)*(Numbers.size+2))/2 # 100000*100001/2
missingNumber = sAllNumbers - sNumbers
print("Tallet som mangler er:", missingNumber)

