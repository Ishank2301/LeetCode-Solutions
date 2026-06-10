class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split()
        return len(s[-1]) 


# Another nice way is that use two variables iterate in the string while checking if there is no space update count for letters or word if space reset count in end return the count

"""
     i = 0
     for ch in s:
        
        if ch!=" ":
            i+=1
            j = i
        else:
            i = 0 
        return j
        
"""