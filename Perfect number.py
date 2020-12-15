#This is the program for Perfect number

a = int(input("Enter the number: "))
# the factors of the number are found
s= 0
for i in range(1,a):
    if (a % i==0):
        s = s + i
# the Logic for perfect number
if(a==s):
    print(a,'is a perfect number')
else:
    print(a,'is not a perfect number')
