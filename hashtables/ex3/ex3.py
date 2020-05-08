def intersection(arrays):

    min_arr = arrays[0]
    longest_length = 0
    for arr in arrays:
        if len(min_arr) > len(arr):
            min_arr = arr
        if len(arr) > longest_length:
            longest_length = len(arr)

    cache = {}
    for num in min_arr:
        cache[num] = 0

    for i in range(longest_length):
        for arr in arrays:
            if i < len(arr) and arr[i] in cache:
                cache[arr[i]] += 1
                
    result = []
    for k in cache.keys():
        if cache[k] == len(arrays):
            result.append(k)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
