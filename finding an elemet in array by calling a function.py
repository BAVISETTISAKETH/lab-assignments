# finding an elemet in array by calling a function
print('''Venkatesh
121910313056''')
n = int(input('Enter the numeber of elements: '))
a = []
print('Enter the elements of the array')
for i in range(0,n):
    i = int(input())
    a.append(i)
x = int(input('Enter the element you want to search: '))
def search(x):
    for i in a:
        if x == i:
            return a.index(i)

y = search(x)
print(f'The index where {x} was found = {y}')
