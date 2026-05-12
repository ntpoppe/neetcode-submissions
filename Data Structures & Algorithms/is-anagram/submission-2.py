class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_map = {}
        for char in s:
            if char in string_map:
                string_map[char] += 1
            else:
                string_map[char] = 1

        for char in t:
            if char in string_map:
                string_map[char] -= 1
            else:
                return False

        for key in string_map:
            if string_map[key] > 0:
                return False

        return True
