#Binary Search

a = [56,477,88,74,-222,93,-66]
a.sort()

high = len(a)
low = 0
mid = (high + low)//2

#The element that we want to search is 88
x = 477
if x not in a:
    print("Element not found in the array")
    
elif a[mid] == x:
    print(f"Element found at index {mid}")

elif x < a[mid]:  
    for i in range(low, mid):
        if a[i]==x :
            print(f'Element found at index {i}')
            break

elif x > a[mid]:
    for i in range(mid, high):
        if a[i]==x :
            print(f'Element found at index {i}')
