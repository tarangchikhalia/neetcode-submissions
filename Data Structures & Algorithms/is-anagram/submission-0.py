class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_dict = {}

        for i in s:
            hash_dict[i] = hash_dict.get(i,0) + 1
        
        for i in t:
            if i in hash_dict:
                if hash_dict[i] == 0:
                    return False
                else:
                    hash_dict[i] = hash_dict[i] - 1
            else:
                return False
        
        return True
            