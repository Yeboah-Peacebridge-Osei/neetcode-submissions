class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for idx in range(len(nums)-2):
            #outer pointer checking for dupplicates
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            left, right = idx + 1, len(nums)-1
            while left < right:
                threeSum = nums[idx] + nums[left] + nums[right]
                if threeSum == 0:
                    result.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    #left and right pointers checking for duplictes
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif threeSum < 0:
                    left += 1
                else:
                    right -= 1

        return result


                

                 


        