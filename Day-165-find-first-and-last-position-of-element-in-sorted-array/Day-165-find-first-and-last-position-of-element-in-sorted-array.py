class Solution:
    def lower_bound(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1
        lowerbound = n 

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lowerbound = mid
                high = mid - 1
            else:
                low = mid + 1
        return lowerbound
    
    def upper_bound(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1
        upperbound = n 

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                upperbound = mid
                high = mid - 1
            else:
                low = mid + 1
        return upperbound
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lower_bound(nums, target)
        
        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]
        
        ub = self.upper_bound(nums, target)
        return [lb, ub - 1]