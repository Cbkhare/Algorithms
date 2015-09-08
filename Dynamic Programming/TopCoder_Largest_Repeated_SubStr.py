#In case data is passed as a parameter
'''
from sys import argv
import re

file_name = argv[1]
fp = open(file_name,'r+')

contents = [line.strip('\n') for line in fp]

#print (contents)
'''

print('Enter no. of strings followed by strings with new line')
n = int(input())
contents = []    #if more than
for i in range(n):
    contents.append(input())

for item in contents:

    junk = list(item)

    i =2
    j =0

    stack = []
    s = 0 
    while (i-j)*2 <= len(item) and j < len(item):

        stat = i        
        #print (junk[j:i],j,i)
        stat_j = j
        while (stat+stat-stat_j) <= len(item):
            
            #print (junk[j:i],junk[stat:stat+stat-stat_j])
            
            if junk[j:i] == junk[stat:stat+stat-stat_j] and \
               len(junk[j:i])*[' '] != junk[j:i] :

                if len(junk[j:i]) > s: 
                    stack= junk[j:i] 
                    s = len(junk[j:i])
            stat +=1
            stat_j +=1 
            
        if (i-j)*2 >= len(item)-1:
            #print (j,i)
            j +=1
            i = j+2
            continue
        i += 1
        
    if stack != []:
        #print (stack)
        print (str(stack).replace(', ','').replace('[','').replace(']','').replace('\'','').replace(' ',''))
    else:
        print ('NONE')

    
'''

Input / Out put Example


Enter no. of strings followed by strings with new line
4
banana
bonyaobonya
maconmac
trask
an
bonya
mac
NONE

'''
