# brute force

from itertools import combinations_with_replacement

def change_options(input_money, coins):
  count = 0
  for i in range(1,input_money+1):
    for c in combinations_with_replacement(coins,i):
      if sum(c) == input_money:
        count += 1
  return count
  
print(change_options(5, [1, 2, 5, 10, 100]))


# recursion 
def change_options(input_money,coins):
  if input_money == 0:
    return 1
  elif input_money < 0:
    return 0
  else:
    total = 0
    for i in coins:
      if input_money - i < 0:
        break
      else:
        total += change_options(input_money-i)
  return total

# DP
#...