class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0

        for i, c in enumerate(s):
            l1 = self.extendCenter(s, i, i)
            l2 = self.extendCenter(s, i, i + 1)
            biglen = max(l1, l2)
            if biglen > end - start + 1:
                start = i - (biglen - 1) // 2
                end = i + biglen // 2
        return s[start:end+1]

    def extendCenter(self, s, left, right):
        length = len(s)
        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
