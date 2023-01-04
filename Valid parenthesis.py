class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeparent = { ")" : "(", "]": "[", "}":"{"
        }
        for e in s:
            if e in closeparent:
                if stack and stack[-1] == closeparent[e]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(e)
        return stack ==[]
