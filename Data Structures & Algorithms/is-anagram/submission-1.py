class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = [0] * 26
        table_blank = [0] * 26
        for letter in s:
            table[ord(letter) - ord('a')] += 1
        for letter in t:
            table[ord(letter) - ord('a')] -= 1

        if table != table_blank:
            return False
        return True