#Performing several operations relating to arrays
print('''Venkatesh
121910313056''')
n = int(input('Enter the number of elements in the array: '))
a =[]
print('Enter the elements of the array:')
for i in range(0,n):
    i = int(input())
    a.append(i)
x = int(input('''Enter the respective numbers for perfroming the operations:
1. Copying the array
2. Removing the duplicates
3. Delete the k'th index
4. Search an item
5. Display contents : \n'''))
b =[]
if x == 1:
    #copying into another array
    b = a[:]
    print(b)
elif x == 2:
    #Removing the duplicates
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
elif x == 3:
    # Deleting the ith index using pop() function
    y = int(input('Enter the index you want to delete: '))
    a.pop(y)
    print(a)
elif x == 4:
    # Searching for an element
    y = int(input('Enter the element you want to search'))
    for i in a:
        if i == y:
            print(a.index(i))
elif x == 5 :
    print (a)

else:
    print('Enter the correct number dude....')
