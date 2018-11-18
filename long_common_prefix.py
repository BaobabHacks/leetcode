class SolutionA:
    def longestCommonPrefix(self, words):
        """
            words(list(str))
            :rtype: str
        """
        if not words:
            return ""
        if len(words) == 1:
            return words[0]

        return words[0][0:
            min(
                [
                    longestCommonPrefixTwoWords(
                        i, j   
                    ) if i and j else
                    0
                    for i, j in zip(words, words[1:])
                ]
            )
        ]

def longestCommonPrefixTwoWords(wordA, wordB):
    common = 0
    for i in range(0, min(
            len(wordA),
            len(wordB)
        )
    ):
        if wordA[i] != wordB[i]:
            break
        common += 1
    return common



class SolutionB:
    def longestCommonPrefix(self, words):
        """
            words(list(str))
            :rtype: str
        """
        if not words:
            return ""
        first_word = words[0]
        for i in range(len(first_word)):
            for word in words[1:]:
                if not word.startswith(first_word[0:i + 1]):
                    return first_word[0:i]
        return first_word


class SolutionC:
    def longestCommonPrefix(self, words):
        """
            words(list(str))
            :rtype: str
        """
        if not words:
            return ""
        first_word = words[0]
        for i in range(len(first_word)):
            for word in words[1:]:
                if i >= len(word) or first_word[i] != word[i]:
                    return first_word[:i]
        return first_word


class SolutionD:
    def longestCommonPrefix(self, words):
        """
            words(list(str))
            :rtype: str
        """
        if not words:
            return ""
        shortest_word = min(words, key=len)
        for i, ch in enumerate(shortest_word):
            for word in words:
                if word[i] != ch:
                    return shortest_word[:i]
        return shortest_word