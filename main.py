class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        for i in range(min([len(j) for j in strs])):
            letter = ''
            for j in strs:
                if letter == '':
                    letter = j[i]
                elif j[i] != letter:
                    return ''.join(prefix)
            else:
                prefix.append(letter)
        return ''.join(prefix)