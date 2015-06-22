## Counting bobs

y = [i for i in range(len(s)) if s.startswith('bob', i)]
print("Number of times bob occurs is: " + str(len(y)))
