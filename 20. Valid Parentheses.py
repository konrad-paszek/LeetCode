class Solution:
    def isValid(self, s: str) -> bool:
        open = ['(', '{', '[']
        closed = [')', '}', ']']
        stack = []
        if len(s) < 2:
            return False
        for bracket in s:
            if bracket in open:
                stack.append(closed[open.index(bracket)])
            else:
                if stack:
                    if stack.pop() != bracket:
                        return False
                else:
                    return False
        return not bool(stack) 