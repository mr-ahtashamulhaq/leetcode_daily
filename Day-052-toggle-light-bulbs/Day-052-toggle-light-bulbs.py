class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        res = set()
        for i in range(len(bulbs)):
            if bulbs[i] not in res:
                res.add(bulbs[i])
            else:
                res.remove(bulbs[i])

        return sorted(list(res))