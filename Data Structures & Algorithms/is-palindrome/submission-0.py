class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        n=""
        for ch in s:
            if ch.isalnum():
                n+=ch
        return n==n[::-1]

        