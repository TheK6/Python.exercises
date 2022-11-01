vector1 = [2, 3, 6, 7, 9, 11, 13, 16, 17, 19, 22]
even = []


for i in vector1:
    if i % 2 == 0:
        even.append(i)

print(sum(even))
print(len(even))