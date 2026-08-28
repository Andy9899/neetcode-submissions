class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenCount = {}
        for letter in s:
            if letter not in seenCount:
                seenCount[letter] = 1
            else:
                seenCount[letter] += 1
        seenCount2 = {}
        for letter in t:
            if letter not in seenCount2:
                seenCount2[letter] = 1
            else:
                seenCount2[letter] += 1
        if seenCount == seenCount2:
            return True
        else:
            return False
        