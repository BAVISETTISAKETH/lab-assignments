# deleting the repeating elements in the array
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
print(f'The original array = {a}')
# Deleting the repeated elements by using "not in" 
for i in a:
    if i not in b:
        b.append(i)

print(f'Array without the repeated elements = {b}')
