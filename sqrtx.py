import math


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))


class SolutionB:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        def sqroot(left, right, n):
            mid = (left + right) // 2
            mid_times_mid = mid * mid
            if mid_times_mid == n:
                return mid
            if mid_times_mid < n:
                # e.g. 50
                # 49 will be less, 64 will be greater, return mid
                if ((mid+1) * (mid+1)) > n:
                    return mid
                return sqroot(
                    left=mid + 1,
                    right=right,
                    n=n
                )
            # mid is too much
            return sqroot(
                left=left,
                right=mid - 1,
                n=n
            ) 
            
        if x in (0, 1):
            return x

        return sqroot(
            left=1,
            right=(x // 2),
            n=x
        )
