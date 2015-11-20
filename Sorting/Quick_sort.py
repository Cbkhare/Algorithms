class Solution:
    # @param A : list of integers
    # @return a list of integers
    # @pivot here is the last element
    def Partition(self,A,st,en):
        B = A[st:en+1]
        pivot,i,c = B[-1],0,0
        while i< len(B):
            if c+i==len(B):   break
            if B[i]>pivot:
                B.append(B.pop(i))
                c+=1                #to check the counter to aavoid inf. loop 
            else:
                i+=1
        A =  (A[:st]+B+A[en+1:])
        return (A)
    
    def QuickSort(self, A,S,E):
        s = S
        e = E  
        piv = A[e]
        if (s < e):
            A = self.Partition(A,s,e)
            pIndex = A.index(piv)
            A = self.QuickSort(A,s,pIndex-1)
            A = self.QuickSort(A,pIndex+1,e)
        return A
         
            
if __name__=='__main__':

    B =Solution()
    n = int(input())
    #s = tuple(map(int,input().split(' ')))
    for j in range(n):
        c = list(map(int,input().split(' ')))
        #sup.append(list(map(int,input().split(' '))))
        print (B.QuickSort(c,0,len(c)-1))


'''
>>> 
1
2 6 5 9 8 4 3 1 7
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> ================================ RESTART ================================
>>> 
1
1 3 2 2 4
[1, 2, 2, 3, 4]
'''
