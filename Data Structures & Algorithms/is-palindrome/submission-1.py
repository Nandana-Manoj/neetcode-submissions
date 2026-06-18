class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s if c.isalnum()]).lower()
        
        m = 0
        n = -1
        for i in range(0, len(s)//2):
            if s[m] == s[n]:
                m += 1
                n -= 1
            else:
                return False
        return True