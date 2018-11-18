class SolutionA:
    def removeDuplicates(self, nums):
        """
        e.g.
            [1,1,2]
            ->
            [1,2]

        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        length = 1
        removes = 0
        nums_len = len(nums)
        while (
            length + removes < nums_len
        ):
            if nums[length - 1] == nums[length]:
                nums.remove(nums[length])
                removes += 1
            else:
                length += 1
        return len(nums)



class SolutionB:
    def removeDuplicates(self, nums):
        """
        e.g.
            [1,1,2]
            ->
            [1,2]

        :type nums: List[int]
        :rtype: int
        """
        # Must modify the input array in-place with O(1) extra memory!
        i = 1
        while i < len(nums):
            if nums[i - 1] == nums[i]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
