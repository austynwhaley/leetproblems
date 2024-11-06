class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wrd_index, abr_index = 0, 0

        while wrd_index < len(word) and abr_index < len(abbr):
            if abbr[abr_index].isalpha():
                if word[wrd_index] != abbr[abr_index]:
                    return False
                
                wrd_index += 1
                abr_index += 1
                
            elif abbr[abr_index].isdigit():
                if abbr[abr_index] == 0:
                    return False
        
                num = 0
                while abr_index < len(abbr) and abbr[abr_index].isdigit():
                    num = num * 10 + int(abbr[abr_index])
                    abr_index += 1

                wrd_index += num
            else:
                return False
        
        return wrd_index == len(word) and abr_index == len(abbr)
    
solution = Solution()
word = "apple"
abbr = "a2e"

print(solution.validWordAbbreviation(word, abbr))
    