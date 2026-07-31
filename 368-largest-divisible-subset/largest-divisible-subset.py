class Solution:

    # USING RECURSION
    def recursion(self, i, nums, cache):
        if i == len(nums):
            return []
        
        if i in cache : 
            return cache[i]
            
        res = []
        res.append(nums[i])

        for j in range(i + 1 , len(nums)) :

            if nums[j] % nums[i] ==0 :

                pick  = [nums[i]] + self.recursion(j , nums, cache)
                if len(res) < len(pick) :
                    res = pick

        cache[i] = res
        return cache[i]
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = {}
        result = []
        for i in range(len(nums)) :
            temp = self.recursion(i, nums, cache)
            if len(temp) > len(result):
                result = temp

        return result