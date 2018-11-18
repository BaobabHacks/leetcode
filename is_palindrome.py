class SolutionA:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        elif x < 0 or str(x).endswith('0'):
            return False
        
        str_x = str(x)
        left = 0
        right = len(str(x)) - 1
        while left < right:
            if str_x[left] == str_x[right]:
                left += 1
                right -= 1
                continue
            return False
        return True


class SolutionB:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        elif x < 0 or str(x).endswith('0'):
            return False
        
        str_x = str(x)
        for first, last in zip(
            str_x,
            reversed(str_x)
        ):
            if first != last:
                return False
        return True
