class Solution:

    def encode(self, strs: List[str]) -> str:
        #length prefix strategy
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string))
            encoded_string += "#"
            encoded_string += string
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
        j = 0

        while i < len(s):
            #iterate until you reach the #
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            start = j + 1
            end = start + length
            
            decoded_string.append(s[start:end])

            i = j + length + 1
            j = end

        return decoded_string

            
            
            


