class Solution:
    def isPalindrome(self, s: str) -> bool:
        outputString = ""
        for char in s:
            if char.isalnum():
                outputString += char.lower()
            
        print(outputString)
        left, right = 0, len(outputString)-1
        while left <= right:
            if outputString[left] != outputString[right]:
                return False
            left += 1
            right -= 1

        return True