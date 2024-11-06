class Solution:
    def calculate(self, s: str) -> int:
        # create a stack
        stack = []
        # create placeholder num and oper
        current_num = 0
        current_oper = "+"
        # parse the string seperate nums and and operaters
        for i, char in enumerate(s):
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            if char in "+-*/" or i == len(s) - 1:
                if current_oper == '+':
                    stack.append(current_num)
                elif current_oper == '-':
                    stack.append(-current_num)
                elif current_oper == '*':
                    stack.append(stack.pop() * current_num)
                elif current_oper == '/':
                    stack.append(int(stack.pop() / current_num))

                current_oper = char
                current_num = 0

        return sum(stack)
    

solution = Solution()
expression = "3+2*2"

print(solution.calculate(expression))