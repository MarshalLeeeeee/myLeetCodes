'''
165. Compare Version Numbers

Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:
Input: version1 = "0.1", version2 = "1.1"
Output: -1

Example 2:
Input: version1 = "1.0.1", version2 = "1"
Output: 1

Example 3:
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
'''

class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        vs1 = version1.split('.')
        vs2 = version2.split('.')
        len1, len2 = len(vs1), len(vs2)
        i = 0
        while i < len1 or i < len2:
            n1, n2 = int(vs1[i]) if i < len1 else 0, int(vs2[i]) if i < len2 else 0
            if n1 > n2: return 1
            elif n1 < n2: return -1
            i += 1
        return 0