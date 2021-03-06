'''
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''

class Solution:
    # O(log(min(m,n)))
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        inf = 1e20
        n1, n2 = len(nums1), len(nums2)
        # nums1 shorter or equal than nums2
        if n1 > n2:
            nums1, nums2, n1, n2 = nums2, nums1, n2, n1
        if(n1 == 0):
            return (nums2[n2 // 2] + nums2[(n2-1)//2]) / 2
        
        left, right, l = 0, n1-1, (n1+n2+1) // 2
        while(True):
            mid1 = (left + right) // 2
            mid2 = l - 2 - mid1
            left1 = nums1[mid1] if (mid1 != -1) else -inf
            right1 = nums1[mid1+1] if (mid1 != n1-1) else +inf
            left2 = nums2[mid2] if (mid2 != -1) else -inf
            right2 = nums2[mid2+1] if (mid2 != n2-1) else +inf
            if(left1 > right2):
                right = mid1 - 1
            elif(left2 > right1):
                left = mid1 + 1
            else:
                break

        if ((n1+n2)%2 == 0):
            return (max(left1,left2)+min(right1,right2)) / 2
        else:
            return (max(left1,left2))


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1,2],[3,4]))