# Knapsack problem

# %% Brute force
from itertools import combinations
import numpy as np

def recursive_knapsack_brute(weight_cap, weights, values):
  max_value = 0
  values = np.array(values)
  for i in range(1,len(weights)+1):
    for comb in combinations(weights,i):
      if sum(comb) <= weight_cap:
        # value = sum(values[np.isin(weights,comb)])
        members = [True if weight in comb else False for weight in weights]
        value = sum([val for (val, bool) in zip(values, members) if bool])
 
        if value > max_value:
          max_value = value
  return max_value


# weight_cap = 10
# weights = [3, 6, 8]
# values = [50, 60, 100]
weight_cap = 50
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
print(recursive_knapsack_brute(weight_cap, weights, values))


# %% Recursive programming
def recursive_knapsack(weight_cap, weights, values, i):
  if weight_cap == 0 or i == 0:
    return 0
  elif weights[i - 1] > weight_cap:
    return recursive_knapsack(weight_cap, weights, values, i - 1)
  else:
    include_item = values[i - 1] + recursive_knapsack(weight_cap - weights[i - 1], weights, values, i - 1)
    exclude_item = recursive_knapsack(weight_cap, weights, values, i - 1)
    return max(include_item, exclude_item)

# with memoization
def recursive_knapsack_memo(weight_cap, weights, values, i, memo):
  if memo[i][weight_cap] != 0:
    return memo[i][weight_cap]

  if weight_cap == 0 or i == 0:
    return memo[i][weight_cap]
  elif weights[i - 1] > weight_cap:
    memo[i][weight_cap] =  recursive_knapsack_memo(weight_cap, weights, values, i - 1,memo)
    return memo[i][weight_cap]
  else:
    include_item = values[i - 1] + recursive_knapsack_memo(weight_cap - weights[i - 1], weights, values, i - 1,memo)
    exclude_item = recursive_knapsack_memo(weight_cap, weights, values, i - 1,memo)
    memo[i][weight_cap] =  max(include_item, exclude_item)
    return memo[i][weight_cap]

# weight_cap = 10
# weights = [3, 6, 8]
# values = [50, 60, 100]
weight_cap = 50
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
memo = [[0 for x in range(weight_cap + 1)] for x in range(len(values)+1)]

print(recursive_knapsack(weight_cap, weights, values,len(weights)))
print(recursive_knapsack_memo(weight_cap, weights, values,len(weights),memo))

# %% Recursive programming without the item index
def recursive_knapsackb(weight_cap, weights, values):
  if weight_cap == 0 or len(weights) == 0:
    return 0
  elif weights[-1] > weight_cap:
    return recursive_knapsackb(weight_cap, weights[:-1], values[:-1])
  else:
    include_item = values[-1] + recursive_knapsackb(weight_cap - weights[- 1], weights[:-1], values[:-1])
    exclude_item = recursive_knapsackb(weight_cap, weights[:-1], values[:-1])
    return max(include_item, exclude_item)


# weight_cap = 10
# weights = [3, 6, 8]
# values = [50, 60, 100]
weight_cap = 50
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
print(recursive_knapsackb(weight_cap, weights, values))

# %% Dynamic programming

def dynamic_knapsack(weight_cap, weights, values):
  rows = len(weights) + 1
  cols = weight_cap + 1
  # Set up 2D array
  matrix = [ [] for x in range(rows) ]

  # Iterate through every row
  for index in range(rows):
    # Initialize columns for this row
    matrix[index] = [ -1 for y in range(cols) ]

    # Iterate through every column
    for weight in range(cols):
      # Write your code here
      if index == 0 or weight == 0:
        matrix[index][weight] = 0
      # If weight at previous row is less than or equal to current weight
      elif weights[index - 1] <= weight:
        # Calculate item to include
        include_item = values[index - 1] + matrix[index - 1][weight - weights[index - 1]]

        # Calculate item to exclude
        exclude_item = matrix[index - 1][weight]

        # Calculate the value of current cell
        matrix[index][weight] = max(include_item, exclude_item)
      else:
        # Calculate the value of current cell
        matrix[index][weight] = matrix[index - 1][weight]
  # Return the value of the bottom right of matrix
  return matrix[rows-1][weight_cap]

# Use this to test your function:
# weight_cap = 10
# weights = [3, 6, 8]
# values = [50, 60, 100]
weight_cap = 50
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
print(dynamic_knapsack(weight_cap, weights, values))

