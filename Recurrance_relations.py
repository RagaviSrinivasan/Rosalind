# ------------------------------------------------------------------------------------------------------------------
# Rosalind problems:
# 5) Use dynamic programming to calculate the number of rabbit pairs after n months, provided each rabbit pair
#    reproduces after 1 month.
#    eg: there will be 19 pairs of rabbits after 5 months if each pair produces 3 rabbits at the end of each month
#-------------------------------------------------------------------------------------------------------------------

def recur_fibo(n, k):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return k
   else:
       return(recur_fibo(n-1,k) + recur_fibo(n-2, k))

print recur_fibo(2, 3)