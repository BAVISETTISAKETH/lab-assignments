#Binary Search with User defined Function
def binary_Search(arr,s):
    arr.sort()
    low = 0
    high = len(arr)
    mid = (high + low)//2
    if s not in arr:
        print('Element not found')
    elif s == arr[mid]:
        print(f'Element found at index {mid}')
    elif s < arr[mid]:
        for i in range(low,mid):
            if s == arr[i]:
                print(f'element found at index {i}')
                break
    elif s > arr[mid]:
        for i in range(mid,high):
            if s == arr[i]:
                print(f'Element found at index {i}')
                break
    
    
#Inputting the array :

a = [12,-33, 66, 5841, -55, 3398, -998]
#Test case 1
print('Test Case : 1')
se = -33
binary_Search(arr = a,s = se)

#Test case 2
print('Test Case : 2')
p = 8944
binary_Search(arr = a,s = p)          
