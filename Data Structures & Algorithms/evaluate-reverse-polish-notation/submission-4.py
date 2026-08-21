class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens:
            if element == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            
            elif element == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)

            elif element == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)

            elif element == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))

            else:
                stack.append(int(element))
        return stack[-1]