def sieve_of_eratosthenes(limit):
  true_indices = [True for i in range(0,limit+1)] # [True]*(limit+1)
  # Write your code here
  for i in range(2,limit+1):
    if true_indices[i]:
      j = i*2
      while j <= limit:
        true_indices[j] = False
        j += i
  return [i for i in range(2,len(true_indices)) if true_indices[i]]


primes = sieve_of_eratosthenes(13)
print(primes) # should return [2, 3, 5, 7, 11, 13]



# import math library
import math
 
def sieve_of_eratosthenes_optimized(limit):
  # handle edge cases
  if (limit <= 1):
    return []
 
  # create the output list
  output = [True] * (limit+1)
 
  # mark 0 and 1 as non-prime
  output[0] = False
  output[1] = False
 
  # iterate up to the square root of the limit
  for i in range(2, math.floor(math.sqrt(limit))):
    if (output[i] == True):
      j = i ** 2    # initialize j to square of i
 
      # mark all multiples of i as non-prime
      while j <= limit:
        output[j] = False
        j += i
 
  # remove non-prime numbers
  output_with_indices = list(enumerate(output))
  trues = [index for (index,value) in output_with_indices if value == True]
  return trues
 
primes = sieve_of_eratosthenes(20)
print(primes) # return [2, 3, 5, 7, 11, 13, 17, 19]