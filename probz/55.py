class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip()
        print(s)
        words=s.split(' ')
        print(words)
        return len(words[-1])


solution = Solution()
s = "Hello World"

print(f"{solution.lengthOfLastWord(s)}")