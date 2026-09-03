class Solution:
    def reverseWords(self, s: str) -> str:
        # split() with no args automatically collapses runs of whitespace
        # and strips leading/trailing whitespace
        words = s.split()
        return ' '.join(reversed(words))