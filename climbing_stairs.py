class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def memoize(fun):
            memo = dict()
            def helper(x):
                if x not in memo:
                    memo[x] = fun(x)
                return memo[x]
            return helper

        def climb_stairs(
            stairs
        ):
            if stairs == 0:
                return 1
            solutions = 0
            if stairs >= 2:
                solutions += climb_stairs_memo(
                    stairs-2
                )
            return solutions + climb_stairs_memo(
                stairs-1
            )
            
        climb_stairs_memo = memoize(climb_stairs)
        for i in range(n):
            climb_stairs_memo(i)
        return climb_stairs_memo(n)
