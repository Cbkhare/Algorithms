def find_zig_zag(sa):

    seq = list(sa)
    count = 1      #First element is by default added
    sign,prev_sign = 1,1
    if len(seq)==1: return 1
    for i in range(len(seq)-1):
        if seq[i+1]==seq[i]: continue
        
        sign = (seq[i+1]-seq[i])/abs(seq[i+1]-seq[i])

        if  i != 0:
            if sign != prev_sign:
                count += 1
                prev_sign  = sign
        else:
            prev_sign = sign
            count += 1           #adding second element 
    return count        

        
if __name__== '__main__':

    seq_add = map(int,input().split())    #Space Demilitted
    m_size = find_zig_zag(seq_add) 
    print (m_size)    

'''
Problem Statement
    	

A sequence of numbers is called a zig-zag sequence if the differences between
successive numbers strictly alternate between positive and negative.
The first difference (if one exists) may be either positive or negative.
A sequence with fewer than two elements is trivially a zig-zag sequence.

For example, 1,7,4,9,2,5 is a zig-zag sequence because the differences
(6,-3,5,-7,3) are alternately positive and negative.
In contrast, 1,4,7,2,5 and 1,7,4,5,5 are not zig-zag sequences, the first
because its first two differences are positive and the second because its
last difference is zero.

Given a sequence of integers, sequence, return the length of the longest
subsequence of sequence that is a zig-zag sequence. A subsequence is obtained
by deleting some number of elements (possibly zero) from the original
sequence, leaving the remaining elements in their original order.
 
Definition
    	
Class:	ZigZag
Method:	longestZigZag
Parameters:	int[]
Returns:	int
Method signature:	int longestZigZag(int[] sequence)
(be sure your method is public)
    
 
Constraints
-	sequence contains between 1 and 50 elements, inclusive.
-	Each element of sequence is between 1 and 1000, inclusive.
 
Examples
0)	
    	

{ 1, 7, 4, 9, 2, 5 }

Returns: 6

The entire sequence is a zig-zag sequence.
1)	
    	

{ 1, 17, 5, 10, 13, 15, 10, 5, 16, 8 }

Returns: 7

There are several subsequences that achieve this length.
One is 1,17,10,13,10,16,8.
2)	
    	

{ 44 }

Returns: 1

3)	
    	

{ 1, 2, 3, 4, 5, 6, 7, 8, 9 }

Returns: 2

4)	
    	

{ 70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32 }

Returns: 8

5)	
    	

{ 374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 
600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 
67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 
477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 
249, 22, 176, 279, 23, 22, 617, 462, 459, 244 }

Returns: 36

'''
'''
#In case data is passed as a parameter

from sys import argv
import re

file_name = argv[1]
fp = open(file_name,'r+')

contents = [int(line.strip('\n')) for line in fp]

#print (contents)
'''
