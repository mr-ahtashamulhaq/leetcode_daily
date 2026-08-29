class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)):
            if nums[i] != 0 and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = len(nums)-1

            while j < k:
                currSum = nums[i] + nums[j] + nums[k]
                if abs(currSum - target) < abs(closestSum - target):
                    closestSum = currSum
                
                if currSum < target:
                    j+=1
                elif currSum > target:
                    k-=1
                else: # we have found exact target no need to check furthur
                    return currSum
        return closestSum
                
                