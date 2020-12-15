# Binary Search with user function and Dynamic input

#Defining the function binary_Search
def binary_Search(a,s):
    high = len(a)
    low = 0
    mid = (low+high)//2
    a.sort()
    if s not in a:
        print('Element  not found in the array!!')
    elif a[mid] == s:
        print(f'Element found at index {mid}')
    elif s < a[mid]:
        for i in range(low,mid):
            if a[i] == s:
                print(f'Element found at index {i}')
                break
    else:
        for i in range (mid, high):
            if a[i] == s:
                print(f'Element found at index {i}')
                break



#Taking the input from the user :

n = int(input('Enter the size of the array : '))
arr = []
print("Enter the elements of the array")
for i in range(n):
    x = int(input())
    arr.append(x)

#Asking the user for the element to search
se = int(input('Enter the element you want to search'))

#calling the function
binary_Search(arr,se)
