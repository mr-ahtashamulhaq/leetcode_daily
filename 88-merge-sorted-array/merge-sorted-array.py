class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # if nums2 == [] or nums1 == []:
            
        i = len(nums1) - n -1
        j = n - 1
        ind = len(nums1) - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j] :
                print("i")
                nums1[ind] = nums1[i]
                i -=1
            elif nums1[i] < nums2[j] :
                print("j")
                nums1[ind] = nums2[j]
                j -=1
            ind -= 1
        
        while ind >= 0 and j >= 0:
            nums1[ind] = nums2[j]
            ind -=1 
            j-=1
