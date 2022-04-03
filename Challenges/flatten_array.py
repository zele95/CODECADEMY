def flatten_array(arr):
# flatten an array into 1-dimension list
  new_list = []
  for i in arr:
    if type(i) == int:
      new_list.append(i)
    else:
      new_list = new_list + i
        
  return new_list
print(flatten_array([1, 2, [3, 4, 5], 6, [7, 8], 9]))
