class Solution:
    def isValid(self, s: str):
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)

            else:
                if len(stack) ==0:
                    return False
                popitem = stack.pop()
                if (popitem == "(" and char == ")"
                    or  popitem == "{" and char == "}"
                    or popitem == "[" and char == "]"):
                    continue
                else:
                    return False
        if len(stack) !=0:
            return False
        return True