class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []  # stores all final permutations

        # nested function — no 'self' needed here
        # curr    = permutation being built so far
        # rem     = numbers still remaining to be picked
        def backtrack(curr, rem):

            # BASE CASE — no numbers left to pick
            # current permutation is complete
            if not rem:
                result.append(curr[:])  # append a COPY not a reference
                return

            # try every remaining number as the next pick
            for i in range(len(rem)):

                # MAKE CHOICE — add rem[i] to current permutation
                curr.append(rem[i])

                # RECURSE — go deeper with rem[i] removed from remaining
                # rem[:i] + rem[i+1:] = all elements except index i
                backtrack(curr, rem[:i] + rem[i+1:])

                # UNDO CHOICE — remove last added element (backtrack)
                # pop() not pop(i) — always undo the LAST added element
                curr.pop()

        # kick off the recursion with empty current and full nums
        # this must be OUTSIDE backtrack, not inside it
        backtrack([], nums)

        return result