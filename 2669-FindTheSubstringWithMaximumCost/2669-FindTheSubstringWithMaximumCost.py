# Last updated: 15/9/2026, 11:33:51 pm
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        

        # If char value is not given the cost is its index+1 from a= 1 to z = 26


        # and if s[i] is the charcters whose value is given its cost is that value .

        # return maximum cost among all substrings.

        # Substring continous in that char like apple -> app,ple, le, pple, not pale etc

        # How can we use hashmap in this.

        # What if we map the whole string in the hashmap with the chars having their key as their values.

        # Kadane automatically handles the substring part as it always follow the order.




        ##### Submarry:
        # 1. Create the dictionary with default values (a=1...z=26)
# 2. Update the dictionary with the special 'chars' and 'vals'
# 3. Initialize ans = 0, curr_sum = 0
# 4. For each character in string s:
    # a. Get value from dictionary
    # b. Add to curr_sum
    # c. If curr_sum < 0, reset to 0
    # d. ans = max(ans, curr_sum)
# 5. Return ans
        n = len(s)
        if n==0:
            return 0
        # 1. Create the dictionary with default values (a=1...z=26)
        alpha = {chr(ord('a')+ i): i+1 for i in range(26)}
        # Mapping the value according to charss
        for c,v in zip(chars,vals):
            alpha[c] = v

        curr_sum = 0
        ans = 0
        for i in s:
            value = alpha[i]
            curr_sum+=value
            if curr_sum < 0:
                curr_sum = 0
            ans = max(ans,curr_sum)
        return ans