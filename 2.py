n = int(input())
array1 = []
for i in range(0,n):
    a = float(input())
    array1.append(a)
array2 = []
for j in range(0,n):
    b = float(input())
    array2.append(b)

for i in range (0,n):
    for j in range(0,n):
        if (array1[i] == array2[j]):
            print(array1[i])
