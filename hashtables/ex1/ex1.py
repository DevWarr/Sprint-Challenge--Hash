def get_indices_of_item_weights(weights, length, limit):

    cache = {}

    for i in range(length):
        if limit - weights[i] in cache:
            return [i, cache[limit - weights[i]]]
        else:
            cache[weights[i]] = i

    return None
