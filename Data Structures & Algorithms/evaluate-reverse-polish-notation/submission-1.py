class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        stack = []

        def get_nums(stack):
            n2 = stack.pop()
            n1 = stack.pop()
            return int(n1), int(n2)

        for el in tokens:
            if el not in {'+', '-', '*', '/'}:
                stack.append(int(el))
            else:
                if el == '+':
                    n1, n2 = get_nums(stack)
                    stack.append(n1 + n2)
                elif el == '-':
                    n1, n2 = get_nums(stack)
                    stack.append(n1 - n2)
                elif el == '*':
                    n1, n2 = get_nums(stack)
                    stack.append(n1 * n2)
                elif el == '/':
                    n1, n2 = get_nums(stack)
                    stack.append(int(n1 / n2))
        
        return int(stack[-1])