class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # ok so 1  Pointer at name and 1 pointer at typed.
        if len(name) > len(typed):
            return False
        if name[0]!= typed[0]:
            return False

        i,j = 1,1
        name_len, typed_len = len(name), len(typed)
        
        while j < typed_len:
            # Case A: Fresh character match between both strings
            if i < name_len and name[i] == typed[j]:
                i+=1
                j+=1
            elif typed[j-1] == typed[j]:
                j+=1
            else:
                return False
        return i == name_len
