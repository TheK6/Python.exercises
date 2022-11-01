list1 = []

for i in range(6):
    num = int(input(f"Insert number {i+1} here: "))
    list1.append(num)

list1.reverse()
for i in list1:
    print(i)