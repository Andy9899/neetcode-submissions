class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        uniqueNums = []
        counts = {}

        nums = sorted(nums)

        for num in nums:
             if num not in uniqueNums: 
                uniqueNums.append(num)
                counts[num] = 1

        ##check how many times first number in uniqueNums appears
        ##move on to next
        ## repeat then compare findings using a hash

        y = 0
        i = 0
        while i < len(nums):
            num = nums[i]
            if y < len(uniqueNums):
                if num == uniqueNums[y]:
                    counts[num] += 1
                else:
                    y += 1
                    continue
            i += 1

        returnValues = []
        for i in range(k):
            mostFrequent = max(counts, key=counts.get)
            returnValues.append(mostFrequent)
            del counts[mostFrequent]
        return returnValues



        
        


        