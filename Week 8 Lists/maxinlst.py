def max_val(lst):
    max_val = float("-inf")
    for val in lst:
        if val > max_val:
            max_val = val
    return max_val
