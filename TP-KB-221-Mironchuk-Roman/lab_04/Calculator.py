def infix_to_postfix(expression):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif char in operators:
            while stack and operators.get(char, 0) <= operators.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

def evaluate_postfix(expression):
    stack = []
    for char in expression:
        if char.isalnum():
            stack.append(float(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)
            elif char == '^':
                stack.append(operand1 ** operand2)

    return stack[0]

def main():
    infix_expression = input("Введіть математичний вираз: ")
    postfix_expression = infix_to_postfix(infix_expression)
    print("ЗПН:", postfix_expression)
    
    result = evaluate_postfix(postfix_expression)
    print("Результат обчислення:", result)

if __name__ == "__main__":
    main()