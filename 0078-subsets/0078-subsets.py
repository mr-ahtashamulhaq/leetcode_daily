class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def solve(ind,subset):
            if ind >= len(nums):
                return result.append(subset.copy())

            subset.append(nums[ind])
            solve(ind+1,subset)
            subset.pop()
            solve(ind+1 , subset)

        solve(0,[])
        return result