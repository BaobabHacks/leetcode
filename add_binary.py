import math


def binary_to_int(binary):
    """
    :type binary: str

    :rtype: int
    """
    total = 0
    for i, bit in enumerate(
        reversed(
            binary
        )
    ):
        total += (2**i) * int(bit)
    return total


def int_to_binary_str(number):
    """
    :type number: int

    :rtype: str
    """
    # e.g. 5
    # 5 in binary is
    # 101
    # e.g. 2**x = 15 means x is 3.something
    length_of_bin = int(
        math.log(
            number,
            2
        )
    )
    result = ""
    # 3, 2, 1, 0
    for i in range(length_of_bin, -1, -1):
        power = 2**i
        # e.g. 15-8, 7-4, 3-2, 1-1
        if number >= power:
            number -= power
            result += '1'
        else:
            result += '0'
    return result


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        total = binary_to_int(a) + binary_to_int(b)
        if not total:
            return '0'
        return int_to_binary_str(total)


class SolutionB:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        total = int(a, 2) + int(b, 2)
        return bin(total)[2:]  # Skip the 0b prefix
