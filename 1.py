n = int(input())
array = []
for i in range(0,n):
    a = float(input())
    array.append(a)
max = 0
for i in range(1,n):
    if (array[i] >= array[max]):
        max = i
for i in range(max+1,n):
    array[i] = 0
print (array)
