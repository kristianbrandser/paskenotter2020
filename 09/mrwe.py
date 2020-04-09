print(set([i for i in range(1,100000)]) - set(map(int,open("09/numbers.txt", "r").read().split(','))))

a = set([i for i in range(1,11)])
b = set(map(int,open("09/testnumbers.txt", "r").read().split(',')))

print ("a: ", a, "b: ", b)
print ("Diff: ", a-b)