class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtracking(ind, total , subset):
            if total == target:
                result.append(subset.copy())
                return
            
            elif total > target:
                return
            
            if ind >= len(candidates):
                return

            subset.append(candidates[ind])
            sum = total + candidates[ind]
            backtracking(ind, sum , subset)
            
            subset.pop()
            sum = total
            backtracking(ind+1, sum, subset)
        
        backtracking(0,0,[])
        return result