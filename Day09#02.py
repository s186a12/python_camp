def isPrime(n):
  if n<=1:
    return False
  for i in range(2,n):
    if n%i==0:
      return False
    return True

def primes(n):
  l=[]
  for i in range(2,n):
    if isPrime(i):
      l.append(i)
  return l
   
n = int(input())       
print(isPrime(n),primes(n))
