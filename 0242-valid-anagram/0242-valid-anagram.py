class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        characters = {}
        for i in s:
            characters[i] = 1 + characters.get(i, 0)

        for j in t:
            if j not in characters:
                return False
            characters[j] -= 1
            if characters[j] == 0:
                characters.pop(j)

        if len(characters) != 0:
            return False
        return True
