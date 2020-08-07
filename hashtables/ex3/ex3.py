def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    present_in_all_arrays = []
    num_of_arrays = len(arrays)

    table = {}
    def build_table(arrays):
        for array in arrays:
            for number in array:
                if number not in table:
                    table[number] = 1
                else:
                    table[number] += 1 # for some reason I couldn't use the default else (as in... just not indent it after the if. Interesting)

    build_table(arrays)
    
    for entry in table:
        # print(f"entry is: {entry}, entry value is: {table[entry]}")
        if table[entry] >= num_of_arrays:
            present_in_all_arrays.append(entry)
    print(present_in_all_arrays)
    return present_in_all_arrays


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
