'''
Fermats little theorm when extended can be applied to check if a
num is prime or not.

Fermat little theorm states that if there is any num p and an int a then,

a^(p-1)%p will always leave a reminder 1,If a and p are co-prime to each other

Application of the same is presente below.
'''

def gcd(a,p):
    c= p
    p = p% a

    if c==1:
        return p
    else:
        return gcd(c,p)


print ('Enter Num')
num = int(input())
if num%2==0:
    print(False)    
elif num ==2:
    print (True)
else:                        #since i am using a=2 there is no need to find
    if pow(2,num-1)%num==1:  #gcd to check if a,p are co-prime or not
        print (True)         #as in first part of If clause we are already checking 
    else:                    #If num % 2==0.
        print (False)        #If you still wish to use gcd with any other num or even 2
                             #remove first part of If clause and uncomment below code
                             #change 'a' accordingly
'''
elif gcd(a,p)==1:   #if num are co-prime    
    if pow(a,num-1)%num==1:
        print (True)
    else:
        print (False)
else:
    print ('Not possbile to check via this method')
'''
