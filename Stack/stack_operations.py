#Required stack_manipulation.py to run this script.

from stack_manipulation import *


def infix_to_postfix(infix_expression):
    """
    Objective: To convert infix expression into postfix expression.
    Input Parameter:
         expression: An infix expression
    Return: Postfix expression of expression
    """
    stack = Stack()
    postfix_express = ''
    operator_preced = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    for c in infix_expression:
        if c.isalnum():
            postfix_express += c
        elif c == '(':
            stack.push_ele(c)
        elif c == ')':
            top = stack.pop_ele()
            while top != '(':
                postfix_express += top
                top = stack.pop_ele()
        elif c in operator_preced:
            if stack.is_empty() or stack.peek() == '(':
                stack.push_ele(c)
            elif operator_preced[stack.peek()] < operator_preced[c]:
                stack.push_ele(c)
            else:
                while operator_preced[stack.peek()] >= operator_preced[c]:
                    postfix_express += stack.pop_ele()
                    if stack.is_empty() or stack.peek() == '(':
                        stack.push_ele(c)
                        break
    while not(stack.is_empty()):
        postfix_express += stack.pop_ele()
    return postfix_express


def postfix_express_evaluation(postfix_express):
    """
    Objective: To evaluate postfix expression.
    Input Parameter:
         postfix_express: An postfix expression whose value is to be calcuated.
    Return: Value of the postfix expression.
    """
    stack = Stack()
    for c in postfix_express:
        if c.isdigit():
            stack.push_ele(c)
            continue
        operand2 = stack.pop_ele()
        operand1 = stack.pop_ele()
        result = str(eval(operand1+c+operand2))
        stack.push_ele(result)
    return stack.pop_ele()


def main():
    infix_express = input("\nEnter any infix expression: ")
    postfix_express = infix_to_postfix(infix_express)
    value = postfix_express_evaluation(postfix_express)
    print(f'\nPostfix expression of {infix_express}-> {postfix_express}\n\t\t\tValue: {value}')


if __name__ == '__main__':
    main()








