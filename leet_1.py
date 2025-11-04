class Solution(object):
    # These class attributes are actually unused by the corrected method
    # nums = [2, 7, 11, 15]
    # target = 9
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        # It's good practice to handle cases where no solution is found
        return []

# To use the class and print the result:
sol = Solution()
# Pass the actual data as arguments to the method
print(sol.twoSum(nums=[2, 7, 11, 15], target=9) )
