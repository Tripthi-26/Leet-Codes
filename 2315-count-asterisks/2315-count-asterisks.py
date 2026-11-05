class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        pair = 0

        for ch in s:
            if ch == '|':
                pair += 1
            elif ch == '*' and pair % 2 == 0:
                count += 1

        return count