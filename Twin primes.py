# Twin primes
print ('''Venkatesh Bisoy
121910313056''')
s = []           # Empty list
lower  = int(input("enter the lower limit: "))
higher = int(input('enter the higher limit: '))

# Taking all the prime numbers in an empty list

for a in range(lower,higher):
    if a > 1:
        for i in range(2,a):
            if (a % i == 0):
                break
        else:
            s.append(a)  # The primes numbers are appended into the empty list 


# We have got the list of prime numbers in that range
for i in range(0,len(s)):
    if ( i+1 < len(s)):
        if (s[i+1] - s [i] == 2):
            print ( s[i], ' and ', s[i+1])
