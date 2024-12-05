# Function isPalindrome(input_string):
#     1. Convert string to lowercase
#     2. Remove all non-alphanumeric characters
#     3. Compare the string with its reverse
#     4. Return True if they are the same, False otherwise
import re

class Solution:
    def isPalindrome(self, s:str):
        s_lower = s.lower().re.sub('[^A-Za-z0-9 ]+', '', s)
        if s_lower == s_lower.reverse():
            return True
        
        return False
    
# Instantiate the class
sol = Solution()

# Test case
pally = "racecar"
print(sol.isPalindrome(pally))


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        s_lower = re.sub(r'[^A-Za-z0-9]+', '', s.lower())
        
        # Compare with its reverse
        return s_lower == s_lower[::-1]
    
# Instantiate the class
sol = Solution()

# Test cases
test_cases = [
    "racecar",
    "A man, a plan, a canal: Panama",
    "race a car",
    "hello"
]

for test in test_cases:
    print(f"'{test}' is palindrome: {sol.isPalindrome(test)}")

    