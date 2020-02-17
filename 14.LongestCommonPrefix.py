#
# 14. Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#     Input: ["flower", "flow", "flight"]
#     Output: "fl"
#
# Example 2:
#     Input: ["dog", "racecar", "car"]
#     Output: ""
#
# Note:
#     All given inputs are in lowercase letters a-z.
#


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first = strs[0] if strs else ''

        for i, c in enumerate(first):
            for s in strs[1:]:
                if len(s) == i or s[i] != c:
                    return first[:i]
        return first
