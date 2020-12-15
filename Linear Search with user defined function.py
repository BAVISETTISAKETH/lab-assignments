# Linear Search with user defined function

def linear_Search(b,x):
    c = 0
    for i in b:
        if i == x:
            c += 1
            break
        else :
            c = 0

        return c
    

n = int(input('enter the number of elements you want to input :' ))
print("Enter the elements of the array")
a = []
for i in range(n):
    a.append(int(input()))

x = int(input('Enter the element you want to search : '))
y = linear_Search(a,x)
if y == 1:
    print('Element found!!')
else :
    print("Element not found")
