
if __name__=='__main__':
    n,k = map(int,input().split(' '))
    dp = [[0 for i in range(n+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1
        dp[i][i]=1
        if i>1:
            for j in range(1,i):
                dp[i][j]=dp[i-1][j-1] + dp[i-1][j]
    print (dp)
    print (dp[n][k])

'''
Binomial Co-efficient
n    
 C  = n!/k!/(n-k)!
  k

  dp structure

  n   n-1   n-1
    =      +   
  k   k-1    k

'''
