# Copying Array from another array
print('''Venkatesh
121910313056''')

n = int(input('enter the number of elements in the array: '))
print ('Enter the elements of the array')
a = []
b = []
for i in range(0,n):
    i =  int(input())
    a.append(i)
print(f'The original array = {a}')
# copying of the array from another array 
for i in range(0,n):
    i = a[i]
    b.append(i)

print(f'The copied array = {b}')
