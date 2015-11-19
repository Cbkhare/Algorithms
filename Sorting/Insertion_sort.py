class Solution:
    # @param A : list of integers
    # @return a list of integers
    def InsertionSort(self, A):
        for i in range(1,len(A)):
            s=A[i]
            gap = i #temp var
            while gap>0 and A[gap-1]>s:
                A[gap]= A[gap-1]
                A[gap-1]= s
                gap-=1
        return A
            
if __name__=='__main__':

    B =Solution()
    n = int(input())
    #s = tuple(map(int,input().split(' ')))
    for i in range(n):
        c = list(map(int,input().split(' ')))
        #sup.append(list(map(int,input().split(' '))))
        print (B.InsertionSort(c))


'''
Insertion Sort

7 4 3 1 5 6

Solution step wise:-

- 4 7 3 1 5 6
- 4 3 7 1 5 6
  3 4 7 1 5 6
- 3 4 1 7 5 6
  3 1 4 7 5 6
  1 3 4 7 5 6
- 1 3 4 5 7 6
- 1 3 4 5 6 7

Time complexity :- O(n^2)
'''
