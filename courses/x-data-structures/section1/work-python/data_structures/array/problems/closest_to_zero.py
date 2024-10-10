def closest_to_zero(nums):
    """
    Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.
    """
    # iterative algorithms because it's O(n) time complexity and O(1) space complexity
    closest = nums[0]
    for num in nums:
        # if distance is less than closest, set closest (abs)
        if abs(num) < abs(closest):
            closest = abs(num)
        else:
            pass
    return f"closest distance {closest}"

nums = [-4,-2,1,4,8]
print(closest_to_zero(nums))