students = [i for i in range(1,31)]

for i in range(28):
    num = int(input())
    students.remove(num)
    
print(min(students))
print(max(students))