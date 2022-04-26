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
def change_optionsREC(input_money,coins):
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


print(change_optionsDP(5, [1, 2, 5, 10, 100]))
