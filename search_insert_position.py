class Solution:
    def searchInsert(self, nums, target):
        """
        e.g.
            [1,2,3] target=4
            return 4
            
            [1,2,3] target=2
            return 1

            [1,2,3] target=0
            return 0

        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # O(n)
        for i, value in enumerate(nums):
            if  target <= value:
                return i
        return i + 1


class SolutionB:
    def searchInsert(self, nums, target):
        """
        e.g.
            [1,2,3] target=4
            return 4
            
            [1,2,3] target=2
            return 1

            [1,2,3] target=0
            return 0

        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left != len(nums) and nums[left] < target:
            return left + 1
        return left
                
