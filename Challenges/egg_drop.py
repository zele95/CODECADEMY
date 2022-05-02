# # import math as m

# # def egg_drop(n):
# #   # Write your function here
# #   if n == 1:
# #     return 1
  
# #   if n%2 == 0:
# #     return 1 + egg_drop(n/2)
# #   else:
# #     return 1 + max(egg_drop(m.floor(n/2)),egg_drop(m.ceil(n/2)))
# # print(egg_drop(100))


# import math as m

# # global eggs
# eggs = 2
# def egg_drop(n):
#     # Write your function here
#     global eggs
#     if n == 0 or eggs == 0:
#         return 0
#     if n == 1:
#         return 1
#     if eggs == 1:
#         return n
#     if eggs > 1:
#         # doesnt brake
#         no_break = egg_drop(n-m.floor(n/2))
#     # eggs brakes
#         eggs -= 1
#         breaks = egg_drop(m.floor(n/2)-1)
#     return 1 + max(no_break,breaks)
    

import math as m
import sys

eggs = 2
def egg_drop(n,eggs):
  # Write your function here
  if n == 0 or n == 1:
    return n
  if eggs == 1:
    return n
  min = 100
  for x in range(1,n+1):
    res = max(egg_drop(x - 1,eggs - 1),
                  egg_drop(n-x,eggs))
    if (res < min):
        min = res
  return min+1
    
print(egg_drop(100,eggs))