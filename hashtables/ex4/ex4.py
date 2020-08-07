def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    table_of_nums = {}
    negatives_list = []
    result = []

    for number in a:
        if number < 0:
            negatives_list.append(number)
        else:
            table_of_nums[number] = 0
        
    for negative_number in negatives_list:
        number_to_look_for = 0 - negative_number
        if number_to_look_for in table_of_nums:
            table_of_nums[number_to_look_for] += 1

    for positive_number in table_of_nums:
        if table_of_nums[positive_number] >= 1:
            result.append(positive_number)

    print(result)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
