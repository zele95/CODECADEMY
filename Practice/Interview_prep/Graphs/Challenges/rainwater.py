# O(n^2)
def naive_solution(heights):
  total_water = 0
  for i in range(1, len(heights) - 1):
    left_bound = 0
    right_bound = 0
    # We only want to look at the elements to the left of i, which are the elements at the lower indices
    for j in range(i+1):
      left_bound = max(left_bound, heights[j])
 
   # Likewise, we only want the elements to the right of i, which are the elements at the higher indices
    for j in range(i, len(heights)):
      right_bound = max(right_bound, heights[j])
 
    total_water += min(left_bound, right_bound) - heights[i]
 
  return total_water


# linear time O(n)
def efficient_solution(heights):
  total_water = 0
  left_pointer = 0
  right_pointer = len(heights) - 1
  left_bound = 0
  right_bound = 0

  # Write your code here
  while left_pointer < right_pointer:
    if heights[left_pointer] <= heights[right_pointer]:
      left_bound = max(left_bound,heights[left_pointer])
      total_water += left_bound - heights[left_pointer]
      left_pointer += 1
    else:
      right_bound = max(right_bound,heights[right_pointer])
      total_water += right_bound - heights[right_pointer]
      right_pointer -= 1
  return total_water


test_array = [4, 2, 1, 3, 0, 1, 2]
print(efficient_solution(test_array))
# Print 6
