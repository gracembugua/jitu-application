#Design a function that takes a list of integers as input. The function should
#return True if the list contains two consecutive threes (3 next to a 3) anywhere
#within the list

def consecutive(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

