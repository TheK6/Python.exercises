v1 = []

for i in range(10):
    num = int(input(f"Insert value {i+1} here: "))
    v1.append(num)

index = v1.index(max(v1))

print(v1)
print(max(v1))
print(index)
