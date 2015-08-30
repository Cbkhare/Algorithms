from math import floor


#Search largest possible value in the list greater or equal to given no.

#Enter a space delimited list with only positive values
print ('Enter Your list')
stack = list(map(int,input().split(' ')))
#print (stack)
print ('Enter num to be searched')
s = int(input())

back,lo,hi,mid= stack, 0,len(stack)-1,0
#List Way

pos = 0

while  lo < hi:

    mid = floor(lo + (hi-lo)/2)
    #print(lo,mid,hi)
    if stack[mid] == s:
        pos = mid
        break
    elif  stack[mid]< s:
        lo = mid +1
        pos = hi
    elif stack[mid] > s:
        hi = mid
        pos = hi

print (pos,stack[pos])

'''
We want to find the index of the target value, thus any index into the array
is a candidate solution. The search space S is the set of all candidate
solutions, thus an interval containing all indices.
Consider the predicate “Is A[x] greater than or equal to the target value?”.
If we were to find the first x for which the predicate says yes, we’d get
exactly what decided we were looking for in the previous paragraph.

The condition in the main theorem is satisfied because the array is sorted
in ascending order: if A[x] is greater than or equal to the target value,
all elements after it are surely also greater than or equal to the target
value.

If we take the sample sequence from before:
0 	5 	13 	19 	22 	41 	55 	68 	72 	81 	98

With the search space (indices):
1 	2 	3 	4 	5 	6 	7 	8 	9 	10 	11

And apply our predicate (with a target value of 55) to it we get:
no 	no 	no 	no 	no 	no 	yes 	yes 	yes 	yes 	yes

This is a series of no answers followed by a series of yes answers, as
we were expecting. Notice how index 7 (where the target value is located)
is the first for which the predicate yields yes, so this is what our binary
search will find.

Implementing the discrete algorithm
One important thing to remember before beginning to code is to settle on
what the two numbers you maintain (lower and upper bound) mean. A likely
answer is a closed interval which surely contains the first x for which
p(x) is true. All of your code should then be directed at maintaining this
invariant: it tells you how to properly move the bounds, which is where a bug
can easily find its way in your code, if you’re not careful.

Another thing you need to be careful with is how high to set the bounds.
By “high” I really mean “wide” since there are two bounds to worry about.
Every so often it happens that a coder concludes during coding that the bounds
he or she set are wide enough, only to find a counterexample during
intermission (when it’s too late). Unfortunately, little helpful advice can be
given here other than to always double- and triple-check your bounds! Also,
since execution time increases logarithmically with the bounds, you can always
set them higher, as long as it doesn’t break the evaluation of the predicate.
Keep your eye out for overflow errors all around, especially in calculating
the median.
'''
