def find_missing_nums(nums):
    missing = []

    for i in nums:
        position = abs(i) - 1
        if nums[position] > 0:
            nums[position] *= -1
                
    for i in range(len(nums)):
        if nums[i] > 0:
            missing.append(i + 1)
                
    return missing


