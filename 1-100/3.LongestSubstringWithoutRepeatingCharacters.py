class Solution:

    # 滑动窗口
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, maxlen = 0, 0
        last_seen = {}

        for i, c in enumerate(s):
            if c in last_seen and last_seen[c] >= start:
                start = last_seen[c] + 1
            else:
                maxlen = max(i - start + 1, maxlen)
            last_seen[c] = i
        return maxlen
