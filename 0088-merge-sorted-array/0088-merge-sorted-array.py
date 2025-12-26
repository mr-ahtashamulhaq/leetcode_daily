class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            for i in range(n):
                nums1[i] = nums2[i]
        else:
            tail1 = m-1
            tail2 = n-1
            curr = (m+n)-1
            while tail1 >= 0 and tail2 >=0 :

                if nums1[tail1] <= nums2[tail2]:
                    nums1[curr] = nums2[tail2]
                    tail2 -=1

                elif nums1[tail1] > nums2[tail2]:
                    nums1[curr] = nums1[tail1]
                    tail1 -=1

                curr-=1
        
            if tail2 >= 0:
                for i in range(tail2 , -1 , -1):
                    nums1[i] = nums2[i]