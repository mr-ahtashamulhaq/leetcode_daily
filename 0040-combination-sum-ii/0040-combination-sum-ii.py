class Solution:
    def backtracking(self,ind, total , subset,candidates,result):
        if total == 0:
            result.append(subset.copy())
            return
        
        if total < 0:
            return
        
        if ind >= len(candidates):
            return
        
        # Try each candidate from current index onwards
        for i in range(ind,len(candidates)):
            #if current element is same as previous skip it
            if i>ind and candidates[i] == candidates[i-1]:
                continue


            if candidates[i] > total:
                break

            subset.append(candidates[i])
            remaining_total = total - candidates[i]

            # Include current candidate
            self.backtracking(i+1,remaining_total, subset,candidates,result )
            # Backtrack: remove the candidate
            subset.pop()

        
    def combinationSum2(self, candidates: List[int], target: int):
        result = []
        candidates.sort()
        self.backtracking(0,target,[],candidates,result)
        return result