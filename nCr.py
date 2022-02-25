#nCr concept in mathematics

n, r = map(int,input().split())
z= n-r
fact_n = 1
fact_r = 1
fact_nr = 1
for i in range(2, n+1):
    fact_n = fact_n * i
for j in range(2, r+1):
    fact_r = fact_r * i
for k in range(2, z+1):
    fact_nr = fact_nr * i

nCr = (fact_n / ((fact_r)* fact_nr))
print(nCr)