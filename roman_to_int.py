class SolutionA:
    def romanToInt(self, roman):
        """
            roman(str)
            :rtype: int
        """
        total = 0
        for i, c in enumerate(roman):
            prev_char = ''
            if i > 0:
                prev_char = roman[i-1]

            special_case = handle_special_case(c, prev_char)
            if special_case:
                total += special_case
            else:
                total += symbol_to_value[c]

        return total

symbol_to_value = {
       'I': 1,
       'V': 5,
       'X': 10,
       'L': 50,
       'C': 100,
       'D': 500,
       'M': 1000
}

def handle_special_case(char, prev_char):
    if char in ('V', 'X') and prev_char == 'I':
        if char == 'V':
            return 4 - 1
        if char == 'X':
            return 9 - 1
    if char in ('L', 'C') and prev_char == 'X':
        if char == 'L':
            return 40 - 10
        if char == 'C':
            return 90 - 10
    if char in ('D', 'M') and prev_char == 'C':
        if char == 'D':
            return 400 - 100
        if char == 'M':
            return 900 - 100
    return 0


class SolutionB:
    def romanToInt(self, roman):
        """
            roman(str)
            :rtype: int
        """
        return sum(
            [
                symbol_to_value[char] - (2 * symbol_to_value[prev_char])
                if symbol_to_value[prev_char] < symbol_to_value[char]
                else symbol_to_value[char]
                for prev_char, char in zip(roman, roman[1:])
            ]
        ) + symbol_to_value[roman[0]]
