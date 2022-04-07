# Write a function, stairmaster(n), that will compute the number of ways to
#  climb a flight of n steps, taking 1, 2, or 3 steps at a time.
# Take the example of climbing n = 4 steps. There are seven different ways
#  one can climb four stairs using 1, 2, or 3 steps at a time: [1,1,1,1] [2,1,1] [1,2,1] [1,1,2] [2,2] [1,3] [3,1].

## Recursive:

def stairmasterRec(n):
  if n == 0 or  n < 0:
    return 0
  elif n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  else:
    return  stairmasterRec(n - 1) + stairmasterRec(n - 2) + stairmasterRec(n - 3)

print(stairmasterRec(10))


def stairmastermemo(n,memo):
    if n in memo:
        return memo[n]
    else:
        if n == 0 or  n < 0:
            memo[n] = 0
        elif n == 1:
            memo[n] = 1 
        elif n == 2:
            memo[n] = 2
        elif n == 3:
            memo[n] = 4
        else:
            memo[n] = stairmastermemo(n - 1,memo) + stairmastermemo(n - 2,memo) + stairmastermemo(n - 3,memo)
        return memo[n]

print(stairmastermemo(10,{}))

# Dynamic programming:

def stairmasterDP(n):
    memo = {0:1,1:1,2:2,3:4}
    if n in memo:
        return memo[n]
    else:
        for i in range(4,n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[n]

print(stairmasterDP(10))

def stairmasterDPopt(n):
    memo = {0:1,1:1,2:2,3:4}
    if n in memo:
        return memo[n]
    else:
        for i in range(4,n+1):
            count = memo[3] + memo[2] + memo[1]
            memo[1] = memo[2]
            memo[2] = memo[3]
            memo[3] = count
    return memo[3]

print(stairmasterDPopt(10))


# # if stairmaster(0) should be 1 then:

def stairmaster0(n):
  if n == 0:
    return 1
  elif n < 0:
    return 0
  else:
    return  stairmaster0(n - 1) + stairmaster0(n - 2) + stairmaster0(n - 3)

print(stairmaster0(4))