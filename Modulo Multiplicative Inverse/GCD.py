def gcd(a,b):

    c = b
    b = a % b

    if b == 0:
        return c
    else:
        return gcd(c,b)


if __name__== '__main__':

    x,y = list(map(int,input().split()))

    ans = gcd(x,y)
    print (ans)
    



'''
#In case data is passed as a parameter

from sys import argv
import re

file_name = argv[1]
fp = open(file_name,'r+')

contents = [int(line.strip('\n')) for line in fp]

#print (contents)
'''
