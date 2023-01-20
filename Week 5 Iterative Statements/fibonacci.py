num = int(input("Please enter a positive integer greater than 1: "))
# num=4
nums = [1, 1]
if num > len(nums):
    for i in range(num-len(nums)):
        nums.append(nums[-1]+nums[-2])
for i in range(num):
    print(nums[i])
