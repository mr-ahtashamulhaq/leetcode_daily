class Solution:
    def memoization(self, ind, words, hashmap, dp) : 
        if ind >= len(words) :
            return 0

        if ind in dp :
            return dp[ind]

        result = 1 

        for j, ch in enumerate(words[ind]) :
            w = words[ind]

            predecessor = w[ : j] + w[ j+1 : ]
            if predecessor in hashmap :        
                result = max(result ,  1 + self.memoization(hashmap[predecessor], words, hashmap, dp) )

        dp[ind] = result
        return dp[ind]

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda w : - len(w) ) 

        hashmap = {}        

        for i, word in enumerate(words): 
            hashmap[word] = i
        
        ans = 1
        dp = {}         # will store key = index  & value = longest length till this index
        for j in range(len(words)) :
            ans = max(ans , self.memoization(j, words, hashmap, dp))
        return ans