    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        used_letters = {}
        curr_sub = ""
        
        for i in range(len(s)):
            
            letter = s[i]
            
            if letter not in curr_sub:
                curr_sub += letter
                used_letters[letter] = i
                continue
            
            if len(curr_sub) > longest:
                longest = len(curr_sub)
                
            start = used_letters[letter]
            used_letters[letter] = i
            
            curr_sub = s[start+1:i+1]
            
        if len(curr_sub) > longest:
            longest = len(curr_sub)
            
        
        print(longest)
        return(longest)