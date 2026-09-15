# Last updated: 15/9/2026, 11:38:21 pm
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # edge case — empty input
        if not digits:
            return []

        # phone mapping
        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        result = []

        def backtrack(curr, index):
            # BASE CASE — processed all digits
            # current combination is complete
            if index == len(digits):
                result.append(curr)
                return

            # get all letters for current digit
            for letter in mapping[digits[index]]:
                # MAKE CHOICE + RECURSE
                # no pop needed — string + letter creates NEW string
                # old curr is untouched automatically
                backtrack(curr + letter, index + 1)

        # start with empty string, first digit
        backtrack("", 0)
        return result
