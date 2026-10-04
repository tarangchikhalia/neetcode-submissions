class Solution:
    def isValid(self, s: str) -> bool:
        checker = []

        for el in s:
            if el in ['[', '{', '(']:
                checker.append(el)
            if el == ']':
                if checker and checker[-1] == '[':
                    checker.pop()
                else:
                    return False
            if el == '}':
                if checker and checker[-1] == '{':
                    checker.pop()
                else:
                    return False
            if el == ')':
                if checker and checker[-1] == '(':
                    checker.pop()
                else:
                    return False
        if checker:
            return False
        return True