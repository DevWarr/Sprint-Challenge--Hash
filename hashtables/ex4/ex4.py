def has_negatives(a):

    cache = {}
    for num in a:
        if num < 0:
            cache[num * -1] = True

    result = []
    for num in a:
        if num in cache:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
