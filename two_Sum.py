class SolutionA:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Option A:
        # Sort list, optimize a bit
        # nlogn sort time
        # n loop
        # Option B:
        # Easier, do n * n
        sorted_nums = (
            sorted(
                enumerate(nums),
                key=lambda tup: tup[1]  # sort by value
            )
        )
        left = 0
        right = len(sorted_nums) - 1
        while left < right:
            left_index, left_value = sorted_nums[left]
            right_index, right_value = sorted_nums[right]
            total = left_value + right_value
            if total == target:
                return (left_index, right_index)
            elif total > target:
                right -=1
            else:
                left += 1
        raise ValueError






from collections import defaultdict


class SolutionB:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = defaultdict(list)
        for i, n in enumerate(nums):
            mapping[n].append(i)
        for num in nums:
            remainder = target - num
            if remainder in mapping:
                if num != remainder:
                    return [mapping[num][0], mapping[remainder][0]]
                if len(mapping[num]) > 1:
                    return [mapping[num][0], mapping[num][1]]
        raise ValueError
