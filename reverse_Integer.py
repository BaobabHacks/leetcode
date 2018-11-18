class SolutionA:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        reversed_number = int(
                "".join(
                reversed(
                    str(
                        x * -1 if x < 0 else x
                    ).rstrip("0")
                )
            )
        )
        if reversed_number > ((2**31) -1):
            return 0

        return reversed_number if x > 0 else (reversed_number * -1)



class SolutionB:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)

        reversed_number = int(
                "".join(
                reversed(
                    str(
                       x
                    )
                )
            )
        )
        if reversed_number > (2**31 -1):
            return 0

        return reversed_number