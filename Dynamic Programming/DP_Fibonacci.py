if __name__=='__main__':
    memo = {}
    n = int(input())
    def fibo(n):
        #print(n)
        if n in memo:    return memo[n]
        if n==0:
            f=0
        elif n==1:
            f=1
        else:
            f=fibo(n-1)+fibo(n-2)
        memo[n]=f
        return f
        
    print (fibo(n))
        
