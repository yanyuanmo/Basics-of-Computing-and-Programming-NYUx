def max_abs_val(nums):
    max_num = -float("inf")
    for num in nums:
        if abs(num) > max_num:
            max_num = abs(num)
    return max_num