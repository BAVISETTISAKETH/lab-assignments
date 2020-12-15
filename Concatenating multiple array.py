# This is the funnction for concatenating two arrays
print('''Venkatesh
121910313056''')
n = int(input('Enter the number of elements of 1st array: '))
print('Enter the elements of the 1st array:')
a = []
#Taking the elements of the 1st array
for i in range(0,n):
    i = int(input())
    a.append(i)

#Taking the elements of the 2nd array
m = int(input('The number of elements in 2nd array: '))
b = []
for i in range(0,m):
        i =  int(input())
        b.append(i)
# Concatenating array
for i in b:
    a.append(i)
print (f'The concatenated array is {a}')
