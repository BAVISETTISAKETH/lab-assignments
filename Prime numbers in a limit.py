# this is the program for printing Prime numbers upto a limit
print ('''saketh
12191031307''')
lower  = int(input("enter the lower limit: "))
higher = int(input('enter the higher limit: '))
# Prime number logic starts here

for a in range(lower,higher):
    if a > 1:
        for i in range(2,a):
            if (a % i == 0):
                break
        else:
            print(a)
            
