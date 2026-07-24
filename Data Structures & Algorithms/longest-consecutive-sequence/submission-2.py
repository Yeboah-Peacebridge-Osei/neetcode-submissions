
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

            #avoid repeatitive work.
            if currentNum - 1 in elementStore and elementStore[currentNum - 1] > 0:
                consecutiveCount += elementStore[currentNum - 1]

            else:
                while currentNum - 1 in elementStore:
                    consecutiveCount += 1
                    currentNum = currentNum - 1
                elementStore[value] = consecutiveCount

            longestConsecutiveCount = max(longestConsecutiveCount, consecutiveCount)

        return longestConsecutiveCount

#partition solution into partitions and only focus on that part of the solution with 
#scenarios and everything to help you out
#problem has properties, what subject are the statement in the problem really describing and 
#what is it leaving out for you to fill out on your own?
        