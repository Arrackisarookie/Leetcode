#
# 771. Jewels and Stone
#
# You're given strings J representing the types of stones that are jewels, and
# S representing the stones you have.
#
# Each character in S is a type of stone you have. You want to know how many of
# the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are
# letters. Letters are case sensitive, so "a" is considered a different type of
# stone from "A".
#


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # sum((True, False, True)) = 2
        return sum(map(J.count, S))
        return sum(S.count(j) for j in J)
        return sum(i in J for i in S)   # i in J 返回 True 或 False


s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))
