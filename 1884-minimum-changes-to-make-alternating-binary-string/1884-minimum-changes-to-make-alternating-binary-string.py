#class Solution:
#    def minOperations(self, s: str) -> int:
 #       # We have to count the number of operation required this to be alternating:
  #      count_for_zero = 0
   #     for i in range(len(s)):
    #  # If index is even, expected character for '0'-started sequence is '
     #       if i%2 == 0:
      #          if s[i]!='0':
       #             count_for_zero+=1
        # If index is odd, expected character for '0'-started sequence is '1'
        #    else:
         #       if s[i]!='1':
          #          count_for_zero+=1
        #count_for_one = len(s)-count_for_zero
        #return min(count_for_zero, count_for_one)


class Solution:
    def minOperations(self, s: str) -> int:
        cnt = sum(c != '01'[i & 1] for i, c in enumerate(s))
        return min(cnt, len(s) - cnt)