# Algorithm: Longest Substring Without Repeating Characters
# Problem:
# Given a string s, find the length of the longest substring
#  that contains no repeating characters.

# Input:
# A string: s
# Output:
# An integer: The length of the longest substring.
# Example:
# Input: s = "abcabcbb"
# Output: 3 (The longest substring is "abc").

# Input: s = "bbbbb"
# Output: 1 (The longest substring is "b").

# Input: s = "pwwkew"
# Output: 3 (The longest substring is "wke").

# Constraints:
# The substring must be contiguous.
# You may assume s only contains ASCII characters.

# input: s = "toomanylettters"
# output: 8 (omanylet)

# this is a sliding window, we are gonna start with 2 points and a var to track
# the highest length so far if the letters arent the same then we increase the end and 
# update our counter. if they are the same we check of out counter is greater then the
# highest if so update if not continue. then retunr the highetst found


def length_of_longest_substring(s: str) -> int:

    highest = 0
    counter = 0

    left, right = 0, 1

    while s:
        if s[left] != s[right]:
            right += 1
            counter += 1
            if highest < counter:
                highest = counter
        else:
            left, right = right, right + 1 

    return highest
    
