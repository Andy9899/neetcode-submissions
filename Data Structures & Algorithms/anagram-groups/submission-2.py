from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## seen() to check for similar characters
        ## 2 for loops

        lists = []
        seenWords = []

        firstIndx = 1
        for index, i in enumerate(strs):
            counts = Counter(i)
            subList = [i]
            if i in seenWords: continue

            for j in range(firstIndx, len(strs)):
                currStr = strs[j]
                if index == j: continue
                currCounts = Counter(currStr)
                if counts == currCounts:
                    subList.append(currStr)
                    seenWords.append(currStr)

            lists.append(subList)
            firstIndx += 1
        return lists

        