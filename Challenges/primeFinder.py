def prime_finder(n):
  # Write your code here
  lst = []
  for i in range(2,n+1):
    prime = True
    for j in range(2,i):
      if i % j == 0:
        prime = False
    if prime == True:
        lst.append(i)
  return lst


print(prime_finder(11))