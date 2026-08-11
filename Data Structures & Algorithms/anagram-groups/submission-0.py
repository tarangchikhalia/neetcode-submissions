class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for st in strs:
            sorted_str = ''.join(sorted(st))
            output[sorted_str].append(st)
        
        return list(output.values())
