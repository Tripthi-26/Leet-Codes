class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"

        mid = len(s) // 2

        first = sum(1 for ch in s[:mid] if ch in vowels)
        second = sum(1 for ch in s[mid:] if ch in vowels)

        return first == second