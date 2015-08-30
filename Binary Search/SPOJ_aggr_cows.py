#MAXIMIZE THE MINIMUM DISTANCE

from math import floor

#Apply Binary search & get result

def placecow(stall,cow,dis):   #placing cow in the stall

    count = 1
    crnt = stall[0]
    for i in range(0,len(stall)):
        nxt = stall[i]
        if nxt-crnt>=dis:
            #print (crnt,nxt)
            count+=1
            if count == cow:
                return 1
            crnt = nxt
        #print (count)
    return 0
        
    


def bazinga(st,cw):     #applying binary search on distance
    st.sort()
    l = len(st)
    start = 0
    end = st[l-1]

    while end-start >1:

        mid = start + floor((end - start)/2)
        #print (start,mid,end)
        if placecow(st,cw,mid):
            start = mid
        else:
            end = mid
    print (start) 
        

'''

#Dynamic Programming: Results in only first 
        tup = ()
        tup += (bu[i],)
        j = i+1
        while j < l and len(tup)<cw:
            if abs(bu[i]-bu[j])>1:
                tup += (bu[j],)
            j+=1
        if len(tup)==cw:    #if tup has total cows as given
            jack.append(tup)
        i+=1
    final = []
    for tups in jack:
        #print (tups)
        diff = tups[1]-tups[0] 
        for x in range(1,len(tups)-1):
            if abs(tups[x]-tup[x+1]) < diff:
                diff = abs(tups[x]-tup[x+1])
        final.append(diff)
                       
    print (max(final),final,jack)
'''
            
        





if __name__== '__main__' :
    
    #Get num of test cases
    nc = int(input())

    for i in range(nc):

        #Get stalls and num of cows

        s,c = input().split(' ')
        stack = []
        #Get Stall Pos
        for j in range (int(s)):
            stack.append(int(input()))
        bazinga(stack,int(c))
        #print (stack,s,c)
                        
'''

AGGRCOW - Aggressive cows
no tags 

Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. The stalls are located along a straight line at positions x1,...,xN (0 <= xi <= 1,000,000,000).

His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, FJ want to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?
Input

t – the number of test cases, then t test cases follows.
* Line 1: Two space-separated integers: N and C
* Lines 2..N+1: Line i+1 contains an integer stall location, xi
Output

For each test case output one integer: the largest minimum distance.
Example

Input:

1
5 3
1
2
8
4
9

Output:

3

Output details:

FJ can put his 3 cows in the stalls at positions 1, 4 and 8,
resulting in a minimum distance of 3.

'''
