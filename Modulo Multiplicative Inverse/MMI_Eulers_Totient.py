'''
According to Euler’s theorem, if a is coprime to m, that is,
gcd(a, m) = 1, then a^{φ(m)} = 1 (mod m),
where where φ(m) is Euler Totient Function. Therefore the modular
multiplicative inverse can be found directly:
a^{*-1} = a^{-1} (mod m).

since

   a^(φ(m)) = 1 (mod m)
=> a * a^(φ(m)-1) = 1 (mod m)
The problem here is finding φ(m). If we know φ(m),
then it is very similar to above method.

Now φ(m) = m*product of all prime factors of m i.e (1-1/p)

φ(m) = m*(1-1/p)
'''


def prime_fac(n):                       #Application of fermats primality test
    i=2                                 #Generating prime factors
    p_fac = [] 
    while n > 1:
        if i == 2 or pow(2,i-1)%i==1:    #only if num is prime or equals to 2
            if n%i==0:
                p_fac.append(i)
                while n % i ==0:
                    n /=i
        if i ==2:
            i +=1
        else:
            i +=2
        #print (i,n)
    return p_fac

def phi(m):

    primes  = prime_fac(m)
    ph = 1
    for pes in primes:
        ph *= (1-1/pes)

    return (ph*m)

    
def Eulers(a,mod):

    p = phi(mod)
    print (pow(a,p-1))

    
if __name__== '__main__':

    x,y = list(map(int,input().split()))
    
    Eulers(x,y)
    

'''
#In case data is passed as a parameter

from sys import argv
import re

file_name = argv[1]
fp = open(file_name,'r+')

contents = [int(line.strip('\n')) for line in fp]

#print (contents)
'''
