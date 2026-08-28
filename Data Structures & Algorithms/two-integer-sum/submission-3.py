class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    ##for loop for a number
    ##second for loop for every other number and checking 
        count = 0
        for k in range (0, len(nums)):
            count += 1
            for i in range (count, len(nums)):
                if nums[k] + nums[i] == target:
                    return [k, i]
            

        