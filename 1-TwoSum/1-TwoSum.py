# Last updated: 12/26/2025, 6:37:29 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Keep track of original indices before sorting
        nums_with_indices = [(num, i) for i, num in enumerate(nums)]
        nums_with_indices.sort()  # Sort by the numbers
        
        left = 0
        right = len(nums_with_indices) - 1
        
        while left < right:
            element = nums_with_indices[left][0] + nums_with_indices[right][0]
            if element == target:
                return [nums_with_indices[left][1], nums_with_indices[right][1]]
            elif element < target:
                left += 1
            else:
                right -= 1
