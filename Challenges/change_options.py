# With recursion and DP, always choosing a path or not 
# choosing a path in the tree (dont iterate through different paths to search for combinations, permutations yes)

available_coins = [1,2,5,10,100]
input_money = 5

# %% Brute force

from itertools import combinations_with_replacement

def change_options(input_money, coins):
  count = 0
  for i in range(1,input_money+1):
    for c in combinations_with_replacement(coins,i):
      if sum(c) == input_money:
        count += 1
  return count
  
print(change_options(input_money, available_coins))

# %% Recursion with choosing

def change(input_money,coins,currentCoin):
  if currentCoin == 0:
    return 0
  if input_money == 0:
    return 1
  elif coins[currentCoin - 1] > input_money:
    return change(input_money, coins, currentCoin - 1)
  else:
    include_coin = change(input_money - coins[currentCoin - 1], coins, currentCoin)
    exclude_coin = change(input_money, coins, currentCoin-1)
    return include_coin + exclude_coin

print(change(input_money, available_coins,len(available_coins)))

# with choosing but without iterator
def change2(input_money,coins):
  if len(coins) == 0:
    return 0
  if input_money == 0:
    return 1
  elif coins[-1] > input_money:
    return change2(input_money, coins[:-1])
  else:
    include_coin = change2(input_money - coins[-1], coins)
    exclude_coin = change2(input_money, coins[:-1] )
    return include_coin + exclude_coin

print(change2(input_money, available_coins))


# %% DP
def change_optionsDP(input_money,coins):
  if input_money == 0:
    return 0
  else:
    rows = len(coins) + 1
    cols = input_money + 1
    # Set up 2D array
    matrix = [ [] for x in range(rows) ]

    # Iterate through every row
    for index in range(rows):
      # Initialize columns for this row
      matrix[index] = [ 0 for y in range(cols) ]

      # Iterate through every column
      for money in range(cols):
        # Write your code here
        if money == 0:
          matrix[index][money] = 1
        elif money != 0 and index == 0:
          matrix[index][money] = 0
        # If coin is bigger than the amount of money
        elif money-coins[index-1] < 0:
          # Calculate the value of current cell
          matrix[index][money] = matrix[index-1][money]
        else:
          # Calculate the value of current cell
          matrix[index][money] = matrix[index][money-coins[index-1]]+matrix[index-1][money]
    # Return the value of the bottom right of matrix
  return matrix[-1][-1]


print(change_optionsDP(input_money, available_coins))

# %% Recursion with iteration (NOT GOOD) (values have to be sorted 1111,1112,1115,1122,1125 ide prema većim brojevima)
def change_optionsREC(input_money,coins,currentCoin):
  if input_money == 0:
    return 1
  elif input_money < 0:
    return 0

  total = 0
  for coin in range(currentCoin,len(coins)):
    if input_money - coins[coin] < 0:
      break
    else:
      total += change_optionsREC(input_money-coins[coin],coins,coin)
  return total

print(change_optionsREC(input_money, available_coins,0))


# %% Recursion without iterator(currentCoin)
def change_optionsREC2(input_money,coins):
  if input_money == 0:
    return 1
  elif input_money < 0:
    return 0

  total = 0
  
  for coin in range(len(coins)):
    if input_money - coins[coin] < 0:
      break
    else:
      total += change_optionsREC2(input_money-coins[coin],coins[coin:])
  return total

  

# %% Recursion with memoization
def change_optionsREC_memo(input_money,coins,memo):
  if memo[len(coins)][input_money] != 0:
    return memo[len(coins)][input_money]
  if input_money == 0:
    memo[len(coins)][input_money] = 1
    return memo[len(coins)][input_money]
  elif input_money < 0 or len(coins) == 0:
    return 0

  total = 0
  for coin in range(len(coins)):
    if input_money - coins[coin] < 0:
      break
    else:
      total += change_optionsREC_memo(input_money-coins[coin],coins[coin:],memo)
  memo[len(coins)][input_money] = total
  return memo[len(coins)][input_money]

input_money = input_money
coins = available_coins
memo = [[0 for x in range(input_money + 1)] for x in range(len(coins)+1)]

print(change_optionsREC2(input_money, available_coins))
print(change_optionsREC_memo(input_money, coins,memo))



# %%
