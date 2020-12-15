# copying the elements of the array in reverse order
print('''Venkatesh
121910313056''')
n = int(input('enter the number of elements in the array: '))
print ('Enter the elements of the array')
a = []
b = []
#Taking the user input
for i in range(0,n):
    i =  int(input())
    a.append(i)
#Backward Iterating the for loop for copying the elements in reverse 
print(f'The original array = {a}')
for i in range(n-1,-1,-1):
    x = a[i]
    b.append(x)  
print(f'The copied array = {b}')
