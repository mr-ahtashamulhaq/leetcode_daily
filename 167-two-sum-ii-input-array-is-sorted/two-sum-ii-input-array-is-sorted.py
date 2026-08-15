class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) -1

        while i < j:
            sumRes = numbers[i] + numbers[j]
            if sumRes == target:
                return (i+1,j+1)
            if sumRes < target:
                i+=1
            if sumRes > target:
                j-=1
            
