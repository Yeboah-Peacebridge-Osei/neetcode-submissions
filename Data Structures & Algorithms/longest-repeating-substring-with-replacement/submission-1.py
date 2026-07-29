
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        maxfreq = 0
        result = 0
        left = 0
        for right in range(len(s)):
            charCount[s[right]] = 1 + charCount.get(s[right], 0)
            maxfreq = max(maxfreq, charCount[s[right]])

            while (right - left + 1) - maxfreq > k:
                charCount[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
        return result
            



        

        