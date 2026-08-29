class Solution:

    def encode(self, strs: List[str]) -> str:
        #length prefix strategy - a number followed by a #
        encoded_str = ""
        for string in strs:
            encoded_str += str(len(string))
            encoded_str += "#"
            encoded_str += string
        return encoded_str


    def decode(self, s: str) -> List[str]:
       res = []
       i = 0

       while i < len(s):
            # Read the length
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

        # Move past '#'
            j += 1

        # Read the string
            res.append(s[j:j + length])

        # Move to the next encoded string
            i = j + length

       return res
            
            


