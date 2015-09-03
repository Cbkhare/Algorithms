'Application of Modulo Multiplicative Inverse via Brute Force'

n, m = list(map(int,input().split()))
n_inv = 0
for i in range(1,m):

    if n*i %m==1:
        n_inv = i
        break
print (n_inv)



'''
Sample Input & Outputs

>>> 
3 7
5
>>> ================================ RESTART ================================
>>> 
8 9
8
>>> ================================ RESTART ================================
>>> 
100 121
23

'''
