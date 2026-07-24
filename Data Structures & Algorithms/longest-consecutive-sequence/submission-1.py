
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #store elements in dictionary
        elementStore = dict()
        for element in nums:
            elementStore[element] = 0

        #iterate through input array
        longestConsecutiveCount = 0

        #calculate for consecutive sequence by counting backwards
        for value in nums:
            consecutiveCount = 1
            currentNum = value
            while currentNum - 1 in elementStore:
                consecutiveCount += 1
                currentNum = currentNum - 1
            longestConsecutiveCount = max(longestConsecutiveCount, consecutiveCount)


        return longestConsecutiveCount


        