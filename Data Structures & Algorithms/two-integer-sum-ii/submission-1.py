class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        ptr_1 = 0
        ptr_2 = len(numbers)-1

        while ptr_1 < len(numbers) and ptr_2 > -1:
            add = numbers[ptr_1] + numbers[ptr_2]
            if add == target:
                output = [ptr_1+1, ptr_2+1]
                break
            elif add > target:
                ptr_2 -= 1
            elif add < target:
                ptr_1 += 1
            if ptr_1 == ptr_2:
                break
        return output

        