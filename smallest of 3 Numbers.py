# this is the program for finding the smallest of 3 Numbers
#using Input() we are taking the input 
a = float(input("Enter the number "))
b = float(input("Enter another number "))
c = float(input("enter the third Number "))

# the Logic begins here
if (a<=b) and (a<=c):
    smallest = a
elif (b<=a)and (b<=c):
    smallest = b
else: smallest = c
print(smallest,"is the smallest number")
