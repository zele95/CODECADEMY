def unique_characters(string_in):
    #  determines if any given string has all unique characters 
    if string_in == '':
        return 'Error! String must not be empty.'
    return len(string_in) == len(set(string_in))
  
  #   test_str = []
  #   for i in string_in:
  #     if i not in test_str:
  #       test_str.append(i)
  #     else:
  #         return False
  # return True


print(unique_characters("apple"))
print(unique_characters(""))
