def stats_finder(array):
    # finds a median and a lower mode of the array

    # mean
    mean = sum(array)/len(array)

    # find mode

    # count the values
    counts = {}
    for i in array:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    # # find the lower mode
    # mode = []
    # for key in counts:
    #     if counts[key] == max(counts.values()):
    #         mode.append(key)
    # mode.sort()
    sorted(array, key = array.count)
    mode = array[len(array)-1]

    return [mean, mode]

# test function
print(stats_finder([500, 400, 400, 375, 300, 350, 325, 300]))

# other solution

# def stats_finder2(array):
#   # Write your code here
#   return [sum(array,0)/len(array), max(set(array), key = array.count)]

# print(stats_finder2([500, 400, 400, 375, 300, 350, 325, 300]))