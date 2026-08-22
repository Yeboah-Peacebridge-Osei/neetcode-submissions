class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []
        for idx, value in enumerate(temperatures): #looking ahead
            while stack and value > stack[-1][1]: #top of stack
                currIdx, currTemp = stack.pop()
                results[currIdx] = idx - currIdx
            stack.append((idx, value))
        return results
        