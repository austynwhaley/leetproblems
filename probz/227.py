class Solution:
    def calculate(self, s: str) -> int:
        # create a stack
        stack = []
        # create placeholder num and oper
        current_num = 0
        current_oper = "+"
        # parse the string seperate nums and and operaters
        for i, char in str:
            if char.isdigit():
                current_number = current_number * 10 + int(char)

            if char in "+-*/" or len(s) - 1:
                if current_oper


        
        return s
    

solution = Solution()
expression = "3+2*2"

print(solution.calculate(expression))