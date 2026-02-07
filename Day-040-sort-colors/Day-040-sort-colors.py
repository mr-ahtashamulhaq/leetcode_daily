class Solution(object):
    def sortColors(self, nums):

        i = 0 #Represent '0'
        k = 0 #Represent '1'
        j = len(nums)-1 #Represent '2'
        while k <= j:
            if nums[k] == 2:
                nums[k],nums[j] = nums[j],nums[k]
                j -=1
            
            elif nums[k] == 0:
                nums[k],nums[i] = nums[i],nums[k]
                i +=1
                k +=1
            
            else:
                k += 1
        return nums