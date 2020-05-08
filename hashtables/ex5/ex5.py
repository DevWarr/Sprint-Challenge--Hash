def finder(files, queries):

    # Create the cache for later lookup
    cache = {}
    for q in queries:
        cache[q] = True

    result = []
    for f in files:
        if f.split("/")[-1] in cache:
            result.append(f)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
