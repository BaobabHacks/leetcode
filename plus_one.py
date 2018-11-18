class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # The simple case, where we just increment the last digit
        # e.g. [7, 4] -> [7, 5]
        if digits[-1] != 9:
            last_digit = digits[-1]
            digits = digits[:-1]
            digits.append(last_digit + 1)
            return digits
        for i, digit in enumerate(reversed(digits)):
            if digit != 9:
                # Step 1:
                # e.g. [8, 9] -> [9, 9]
                digits[len(digits)-1-i] = digit + 1
                # Step 2:
                # Now [9, 9] -> [9, 0]
                for j in range(i):
                    digits[len(digits)-1-j] = 0
                return digits
        else:
            # They are all 9's
            # e.g. [9] -> [1,0]
            output = [1]
            for _ in digits:
                output.append(0)
            return output


class SolutionB:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        # Turn List[int] into a int
        for i, digit in enumerate(reversed(digits)):
            number += (10 ** i) * digit
        number += 1
        # Turn int into List[int]
        return [int(n) for n in str(number)]
