class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = [] 
        hash_dict = defaultdict(int)

        for num in nums:
           hash_dict[num] = hash_dict.get(num,0) + 1

        arr = []
        for num, count in hash_dict.items():
           arr.append([count, num])
        arr.sort()

        while len(output) < k:
            output.append(arr.pop()[1])
        
        return output