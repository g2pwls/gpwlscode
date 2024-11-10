array = []

for i in range(10):
    a = int(input()) % 42
    if a not in array:
        array.append(a)
print(len(array))