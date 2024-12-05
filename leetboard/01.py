# Create an empty result string

# Start from the last character of input string

# Iterate backwards through the string

# Add each character to the result string

# Return the result string

# mine  | |
#       v v

class Solution:
    def reverseString(self, s:str) -> str: 
        res = []

        i = len(s) - 1

        for char in range(s, len(s), -1):
            res.append(char[i])

        return res
    
# solution | |
#          v v
def reverseString(self, s: str) -> str: 
    # Create an empty list to store reversed characters
    res = []
    
    # Iterate backwards through the string's indices
    # range(len(s) - 1, -1, -1) means:
    # - Start at len(s) - 1 (last index)
    # - Go down to -1 (just before 0)
    # - Step by -1 (move backwards)
    for i in range(len(s) - 1, -1, -1):
        # Append each character at the current index to the result list
        res.append(s[i])
    
    # Convert the list of characters back to a string
    return ''.join(res)


# also we could do

def reverseString(self, s:str) -> str:
    return s[::-1]