# Last updated: 15/9/2026, 11:35:07 pm
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # Ok let's do this shii as i have done similar questions beforehand:
        # Well we need to shift the element to the right whenever we come across a zero and we have make its next element zero too:
        n = len(arr)
        i=0
        while i < n:
            if arr[i] == 0:
                arr.insert(i+1,0)
                arr.pop()
                i+=2
            else:
                i+=1
    


                # If i simply want the  zero to come froward how can i do that