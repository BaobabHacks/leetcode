open_to_close_mapping = {
    '{':'}',
    '(':')',
    '[':']',
}

class SolutionA:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        for c in s:
            if c in (
                '[',
                '{',
                '(',
            ):
                stack.append(c)
            if c in (
                ']',
                '}',
                ')',
            ):
                if not stack:
                    return False
                if c != open_to_close_mapping[stack[-1]]:
                    return False
                stack.pop()
        return len(stack) == 0