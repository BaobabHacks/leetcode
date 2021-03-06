from collections import defaultdict


def shift_everything_over(
    nums1,
    nums2,
    last_index,
    index_of_nums1,
    times,
    index_of_nums2
):
    # nums1 = [1, 2, 3, 0, 0, 0] m = 3
    # nums2 = [2, 5, 6]          n = 3

    for i in range(
        len(nums1) - 1 - times,  # e.g. 4, 3 (5-1, 5-2)
        index_of_nums1 - 1,  # e.g. 1, 1 (2-1, 3-1-1)
        -1
    ):
        # First loop
        # i = e.g. 4, 3
        # index = e.g. 5, 4
        nums1[i + times] = nums1[i]

    # Insert the value
    for i in range(times):  # e.g. 0, [0, 1]
        nums1[index_of_nums1 + i] = nums2[index_of_nums2 + i]


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """ #            2  3     6
        # e.g.
        # nums1 = [1, 2, 3, 0, 0, 0] m = 3
        # nums2 = [2, 5, 6]          n = 3
        index_of_nums1 = 0
        where_to_insert = defaultdict(int)
        if len(nums2) > len(nums1):
            raise ValueError
        for num_from_l2 in nums2:
            while (
                nums1[index_of_nums1] <= num_from_l2
                and
                index_of_nums1 < m
            ):
                index_of_nums1 += 1
            where_to_insert[index_of_nums1] += 1
        # e.g.
        # where_to_insert = {2:1, 3: 2}
        last_index = m - 1
        index_of_nums2 = 0
        for index_of_nums1, times in where_to_insert.items():
            shift_everything_over(
                nums1,  # e.g. [1, 2, 3, 0, 0, 0], ???
                nums2,  # e.g. [2, 5, 6]
                last_index,  # e.g. 2, 3
                index_of_nums1=index_of_nums1 + index_of_nums2,  # e.g. 2, 4
                times=times,  # e.g. 1, 2
                index_of_nums2=index_of_nums2  # e.g. 0, 1
            )
            last_index += times
            index_of_nums2 += times
