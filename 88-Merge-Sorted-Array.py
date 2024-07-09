class Solution:
    def merge(self, nums1, m, nums2, n):
        \\\
        Do not return anything, modify nums1 in-place instead.
        \\\
        idx1 = m - 1
        idx2 = n - 1
        idx = m + n - 1
        
        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] > nums2[idx2]:
                nums1[idx] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[idx] = nums2[idx2]
                idx2 -= 1
            idx -= 1
        
        # If there are remaining elements in nums2, copy them to nums1
        while idx2 >= 0:
            nums1[idx] = nums2[idx2]
            idx2 -= 1
            idx -= 1