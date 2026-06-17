class Solution:

    def encode(self, strs: List[str]) -> str:
        # combined = "-".join(strs)
        # print("Encoded:", combined)
        # return combined
        combined = ""
        for i in strs:
            combined += str(len(str(len(i)))) + str(len(i)) + i
        return combined

    def decode(self, s: str) -> List[str]:
        # print("Received:", s, len(s), type(s))
        # if not len(s):
        #     return []
        # strs = s.split("-")
        # print(strs)
        # return strs
        if not len(s):
            return []
        
        strs = []
        num_digits = int(s[0])
        word_len = int(s[1:1+num_digits])

        i = 1 + num_digits
        while True:
            j = i+word_len
            word = s[i:j]
            strs.append(word)
            if i+word_len > len(s) - 1:
                break
            num_digits = int(s[j])
            
            i = i+word_len+1+num_digits
            
            word_len = int(s[j+1:j+1+num_digits])
            
        
        return strs
