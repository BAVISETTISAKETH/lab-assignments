# the code for finding the sum of digits in a number

x = int(input(' Enter the number: ' ))
x1 = x
n = 0
sum1 = 0
while (x1>0):
      n+= 1
      x1 = x1//10
x1 = x
# The sum of the digits is
while (x>0):
     rem = x%10
     sum1 = sum1 + rem
     x = x//10
x = x1
print ('The sum of the digits is', sum1)
# the code for amstrong number
sum2 = 0
while ( x1>0):
     rem =  x1%10
     sum2 = sum2 + rem**n
     x1 = x1//10
if ( x == sum2 ):
    print(x, 'is an Amstrong number')
else :
    print (x,' is not an Amstrong number')
