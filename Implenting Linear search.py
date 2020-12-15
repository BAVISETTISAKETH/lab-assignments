#Implenting Linear search
print('''Venkatesh Bisoyi
121910313056''')
n = int(input('Enter the number elements you want to input: '))
a = []
print('Enter the elememts')
for i in range(n):
    a.append(int(input()))

x = int(input('Enter the element you want to search'))
c = 0

for i in a:
    if i == x :
        c += 1
        print(f'Element found ' )
        break
    else :
        c = 0
if x == 0
print('The element is not found ')
