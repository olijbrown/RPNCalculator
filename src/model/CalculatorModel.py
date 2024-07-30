class CalculatorModel:
    def __init__(self):
        self.operators = {'+', '-', '*', '/'}
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def _tokenise(self, expression):
        tokens = []
        num = ''
        for char in expression:
            if char.isdigit() or char == '.':
                num += char
            elif char in self.operators or char in '()':
                if num:
                    tokens.append(num)
                    num = ''
                tokens.append(char)
            elif char.isspace():
                if num:
                    tokens.append(num)
                    num = ''
        if num:
            tokens.append(num)

        return tokens

    def infixToPostfix(self, expression):
        tokens = self._tokenise(expression)
        output = []
        operators = []

        for token in tokens:
            if token.isnumeric() or '.' in token:
                output.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()  # Remove the '(' from the stack
            elif token in self.operators:
                while (operators and operators[-1] in self.operators and
                       self.precedence[operators[-1]] >= self.precedence[token]):
                    output.append(operators.pop())
                operators.append(token)

        while operators:
            output.append(operators.pop())

        return output

    def RPNCalculator(self, expression):
        stack = []

        for token in expression:
            if token in self.operators:
                if len(stack) < 2:
                    raise IndexError("Insufficient values in the expression for the operation.")
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        raise ZeroDivisionError
                    stack.append(a / b)
            else:
                stack.append(float(token))

        if len(stack) != 1:
            raise ValueError

        return stack[0]
