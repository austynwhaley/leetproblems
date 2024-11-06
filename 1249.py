class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opened = "("
        closed = ")"
        stack = []
        result = ""
        for char in s:
            if char not in [opened, closed]:
                result += char
            elif char == opened:
                stack.append(len(result))
                result += char
            elif char == closed:
                if stack:
                    stack.pop()
                    result += char

        for i in reversed(stack):
            result = result[:i] + result[i + 1:] 

        return result

input_str = "))(("
solution = Solution()

print(solution.minRemoveToMakeValid(input_str))