class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        sum_so_far = 0
        for i, n in enumerate(nums):
            sum_so_far += n
            if sum_so_far > max_sum:
                max_sum = sum_so_far
            if max_sum < n:
                max_sum = n
            if sum_so_far < n:
                sum_so_far = n
            
        return max_sum

class SolutionB:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        sum_so_far = 0
        for i, n in enumerate(nums):
            sum_so_far = max(sum_so_far + n, n)
            max_sum = max(max_sum, n, sum_so_far)
            
        return max_sum
