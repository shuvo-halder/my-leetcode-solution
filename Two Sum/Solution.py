# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# solution


from typing import List, Tuple
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for num1_index, num1 in enumerate(nums):
            num2 = target - num1

            try:
                num2_index = result[num2]
            except KeyError:
                result[num1] = num1_index
            else:
                return tuple(sorted([num1_index, num2_index]))