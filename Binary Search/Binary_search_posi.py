#Enter a space delimited list with only positive values

stack = list(map(int,input().split(' ')))
#print (stack)

s = int(input())

back,z = stack,0

#List Way
while len(back)>0:
    i = 0
    i = int(abs((len(back)-1)/2))  #since list is of 0 to len
    print (i,back)
    if back[i]==s:
        z=back[i]
        break
    elif back[i]>s:
        back = back[:i]
    else:
        back = back[i+1:]
if z==s:
    print ('Target Found')
else:
    print ('Not Found') 
        

#Indices Way
'''
lo,hi,z = 0, len(stack)-1 ,0
while lo <= hi:

    mid = lo + int(abs((lo-hi)/2))
    print (mid)
    if stack[mid] == s:
        z = mid
        break
    elif stack[mid] < s:
        lo = mid+1
    else:
        hi = mid -1
if z!=0:
    print ('Target Found')
else:
    print ('Not Found')
        
'''

#only for parameters
'''
from sys import argv
#from itertools import permutations
#from operator import itemgetter
#from re import search


file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]
#print (contents)

'''
