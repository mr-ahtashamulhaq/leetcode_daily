class Solution:
    def threeSum(self, nums):
        key_dict = {}
        answer = []
        for i in range(len(nums)):
            for j in range(i+1 ,  len(nums)):
                remaining = -1 * (nums[i] + nums[j])
                if remaining in key_dict:
                    answer.append([nums[i] , nums[j] , remaining])
                else:
                
                    key_dict[i] = key_dict.get(i,0)


        return answer
        
obj = Solution()