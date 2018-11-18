class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                break
            if haystack[i:].startswith(needle):
                return i
        return -1
