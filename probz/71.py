from collections import deque


class Solution:

    def simplifyPath(self, path: str) -> str:
        # Split the path by '/'
        path_arr = path.split('/')
        
        # Use a deque or a list to build the canonical path
        new_path = []

        for part in path_arr:
            if part == '' or part == '.':
                # Ignore empty parts or '.' (current directory)
                continue
            elif part == '..':
                # Go up one directory (pop the last valid part if it exists)
                if new_path:
                    new_path.pop()
            else:
                # Append valid directory names to the new path
                new_path.append(part)

        # Join the result with '/' and add the root '/'
        return '/' + '/'.join(new_path)



solution = Solution()
str = "/home/user/Documents/../Pictures"

print(f"{solution.simplifyPath(str)}")