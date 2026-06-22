class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = []
        indx = 0
        found = False

        for i in nums:
            indx2 = 0

            for j in nums:
                if indx == indx2: 
                    indx2 += 1
                    continue

                if i + j == target:
                    numbers.extend([indx, indx2])
                    return numbers
                indx2 += 1

            indx += 1
