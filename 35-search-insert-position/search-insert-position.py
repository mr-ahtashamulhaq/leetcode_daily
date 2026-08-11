class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lowerbound = n
        low = 0
        high = n-1

        while low<=high:
            mid = (low+high)//2
            
            if nums[mid] >= target:
                lowerbound = mid
                high = mid -1
            else:
                low = mid+1
        return lowerbound