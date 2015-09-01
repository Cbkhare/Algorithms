import math

def lg(x):
    return float(math.log(x,2))

def time_cal(s,n):
    return (s*n*lg(n))
    
c = int(input())
time = float(input())


start = 1     #since min value of time is zero when n=1, check time_cal

end = math.pow(10,10)
t = end       #max value of n, will reduce it untills it gets max of min

while end-start > 1:
    mid = start + (end-start)/2
    ans = time_cal(c,mid)
    #print ((start),mid,end,ans)
    if (ans) == time :
        break
    elif ans < time:
        start= mid
    else:
        end = mid
print (round(start))

''' Problem Statement for SortEstimate
Problem Statement
    	You have implemented a sorting algorithm that requires exactly c*n*lg(n) nanoseconds to sort n integers. Here lg denotes the base-2 logarithm. Given time nanoseconds, return the largest double n such that c*n*lg(n) <= time.
 
Definition
    	
Class:	SortEstimate
Method:	howMany
Parameters:	int, int
Returns:	double
Method signature:	double howMany(int c, int time)
(be sure your method is public)
    
 
Notes
-	lg(n) = ln(n)/ln(2) where ln denotes the natural log.
-	Your return value must have a relative or absolute error less than 1e-9.
 
Constraints
-	c will be between 1 and 100 inclusive.
-	time will be between 1 and 2000000000 inclusive.
 
Examples
0)	
    	

1

8

Returns: 4.0

Given 8 nanoseconds we can sort 4 integers since

	1*4*lg(4) = 4*2 = 8

1)	
    	

2

16

Returns: 4.0

Now that c = 2 we need twice as many nanoseconds to sort 4 integers.
2)	
    	

37

12392342

Returns: 23104.999312341137

We can almost sort 23105 integers, but not quite.
3)	
    	

1

2000000000

Returns: 7.637495090348122E7

Largest possible return.
'''
