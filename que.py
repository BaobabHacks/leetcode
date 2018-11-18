class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        queue = list()
        index_of_nums1 = 0
        index_of_nums2 = 0
        while (index_of_nums1 < (m + n)):
            we_still_need_to_queue = index_of_nums1 < m
            if (
                index_of_nums2 >= n
                and
                not queue
            ):
                return
            elif queue:
                # if we just need to append to 1 or pop queue
                if index_of_nums2 >= n:
                    if we_still_need_to_queue:
                        queue.append(nums1[index_of_nums1])
                    nums1[index_of_nums1] = queue.pop(0)
                    index_of_nums1 += 1
                elif queue[0] < nums2[index_of_nums2]:
                    min = queue.pop(0)
                    if we_still_need_to_queue:
                        queue.append(nums1[index_of_nums1])
                    nums1[index_of_nums1] = min
                    index_of_nums1 += 1
                else:
                    min = nums2[index_of_nums2]
                    if we_still_need_to_queue:
                        queue.append(nums1[index_of_nums1])
                    nums1[index_of_nums1] = min
                    index_of_nums1 += 1
                    index_of_nums2 += 1
            else:
                if(
                    nums1[index_of_nums1] < nums2[index_of_nums2]
                    and
                    we_still_need_to_queue
                ):
                    index_of_nums1 += 1
                else:
                    if we_still_need_to_queue:
                        queue.append(nums1[index_of_nums1])
                    nums1[index_of_nums1] = nums2[index_of_nums2]
                    index_of_nums1 += 1
                    index_of_nums2 += 1
