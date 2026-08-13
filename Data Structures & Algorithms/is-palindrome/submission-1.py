import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        ptr_1 = 0
        ptr_2 = len(clean_s)-1

        for idx in range(int(len(clean_s)/2)):
            if clean_s[ptr_1] == clean_s[ptr_2]:
                ptr_1 += 1
                ptr_2 -= 1
            else:
                return False

        return True