def find_sum_of_three(nums, target):
    # Sort the nums input
    nums.sort()

    for i in range(len(nums) - 2):
        # Initialize the pointers
        low = i + 1
        high = len(nums) - 1

        # Traverse the list to find the triplet that equals the target
        while low < high:
            triplet = nums[i] + nums[low] + nums[high]

            if triplet == target:
                return True
            
            # If the sum of the triplet is less than the target, move the low pointer forward
            elif triplet < target:
                low += 1

            # If the sum of the triplet is greater than the target, move the high pointer backward
            else:
                high -= 1
    
    
    return False