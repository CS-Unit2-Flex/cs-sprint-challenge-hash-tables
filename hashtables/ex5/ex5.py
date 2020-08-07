# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    paths_table = {}
    result = []

    for file in files:
        file_list = file.split('/')
        print(file_list)
        ending_path = file_list[-1]
        paths_table[ending_path] = file

    for query in queries:
        to_find = paths_table[query]
        if to_find in paths_table:
            result.append(paths_table[to_find])
        else:
            continue
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
