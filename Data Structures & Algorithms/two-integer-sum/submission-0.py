class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_dict = {}

        for idx, num in enumerate(nums):
            
            temp_num = target - num
            if temp_num in hash_dict:
                return [hash_dict[temp_num], idx]
            else:
                hash_dict[num] = idx