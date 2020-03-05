def numberOfPaths(v, n) : 
  m=1
  for i in range(n, (m + n - 1)): 
    m*= i 
    m //= (i - n + 1) 	
  return m%100000000
n,=v[int(i) for i in input().split()]
print(numberOfPaths(n,v)) 
