# this is the code for LCM of 2 numbers
a = float(input("Enter 1st number "))
b = float(input("Enter 2nd number "))
# the Logic starts from here
if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print("LCM is:",min1)
        break
    min1=min1+1
