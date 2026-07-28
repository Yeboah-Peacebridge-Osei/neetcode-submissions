class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        charCheck = set()
        left = 0
        for right in range(len(s)):
            while s[right] in charCheck:
                charCheck.remove(s[left])
                left += 1

            charCheck.add(s[right])
            result = max(result, right - left + 1)
        return result
        