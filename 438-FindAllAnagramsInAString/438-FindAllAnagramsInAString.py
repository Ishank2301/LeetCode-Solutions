# Last updated: 15/9/2026, 11:36:07 pm
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        n, m = len(s), len(p)
        if m>n:
            return []

        p_count = Counter(p)
        s_count = Counter()
        for i in range(n):
            # Add character to the right of the window
            s_count[s[i]]+=1

            # Remove char from the left once window size exceeds len(p);
            if i>=m:
                if s_count[s[i-m]] == 1:
                    del s_count[s[i-m]]
                else:
                    s_count[s[i-m]] -=1

            # Check if current window matches target frequency:
            if s_count == p_count:
                result.append(i-m+1)
        return result

