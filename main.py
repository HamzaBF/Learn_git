class Solution:
    def isValid(self, s: str) -> bool:
        closed = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char not in closed:
                print(char)
                stack.append(char)
                print(stack)
                
            else:
                if not stack:
                    return False
                if stack[-1] != closed[char]:
                    return False
                print(stack)
                print(stack[-1])
                print(char)
                stack.pop()
        return False if stack else True

       
            


    


s = "({})[]"


S = Solution()

print(S.isValid(s))



