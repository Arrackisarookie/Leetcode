#
# 165. Compare Version Numbers
#
# Compare two version numbers version1 and version2.
# if version1 > version2 return 1;
# else if version1 < version2 return -1;
# else return 0
#
# You may assume that the version strings are non-empty and contain only digits
# and the . character.
#
# The . character does not represent a decimal point and is used to separate
# number sequences.
#
# For instance, 2.5 is not 'two and a half' or 'half way to version three', it
# is the fifth second-level revision of the second first-level revision.
#
# You may assume the default revision number for each level of a version number
# to be 0. For example, version number 3.4 has a revision number of 3 and 4 for
# its first and second level revision number. Its third and fourth level
# revision number are both 0.
#
#
# Example 1:
#     Input: version1 = '0.1', version2 = '1.1'
#     Output: -1
#
# Example 2:
#     Input: version1 = '1.0.1', version2 = '1'
#     Output: 1
#
# Example 3:
#     Input: version1 = '7.5.2.4', version2 = '7.5.3'
#     Output: -1
#
# Example 4:
#     Input: version1 = '1.01', version2 = '1.001'
#     Output: 0
#
# Example 5:
#     Input: version1 = '1.0', version2 = '1.0.0'
#     Output: 0
#


class Solution(object):
    def compareVersion1(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        length = max(len(v1), len(v2))

        while len(v1) < length:
            v1.append('0')
        while len(v2) < length:
            v2.append('0')

        for i in range(length):
            diff = int(v1[i]) - int(v2[i])
            if diff > 0:
                return 1
            elif diff < 0:
                return -1

        return 0

    def compareVersion2(self, version1, version2):
        import itertools
        for v1, v2 in itertools.zip_longest(version1.split('.'), version2.split('.'), fillvalue=0):
            diff = int(v1) - int(v2)
            if diff != 0:
                return 1 if diff > 0 else -1

        return 0
