class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)


Operators = set(['+', '-', '*', '/', '(', ')', '^']) 

Priority = {'+':1, '-':1, '*':2, '/':2, '^':3} 
 
def infixToPostfix(expression): 

    stack = Stack() 

    output = '' 

    for character in expression:

        if character not in Operators:  
            output += character

        elif character =='(': 
            stack.push('(')

        elif character ==')':
            while not stack.is_empty() and stack.peek()!= '(':
                output+=stack.pop()
            stack.pop()

        else: 
            while not stack.is_empty() and stack.peek()!='(' and Priority[character]<=Priority[stack.peek()]:
                output+=stack.pop()
            stack.push(character)
    while not stack.is_empty():

        output += stack.pop()
    return output

def infixToPrefix(expression):
    reversed_expression = expression[::-1]
    reversed_expression = reversed_expression.replace('(', '#').replace(')', '(').replace('#', ')')
    prefix = infixToPostfix(reversed_expression)
    return prefix[::-1]

def evaluate_postfix(expression):
    stack = Stack()
    for char in expression:
        if char not in Operators:
            stack.push(int(char))
        else:
            first = stack.pop()
            second = stack.pop()
            
            if char == "+":
                stack.push(second + first)
            elif char == "-":
                stack.push(second - first)
            elif char == "*":
                stack.push(second * first)
            elif char == "/":
                stack.push(second / first)
            elif char == "^":
                stack.push(second ** first)
    return stack.peek()



while True:
    infix_expression = input('Enter infix expression: ')
    postfix_expression = infixToPostfix(infix_expression)
    prefix_expression = infixToPrefix(infix_expression)
    print(f'Infix notation: {infix_expression}')
    print(f'Postfix notation: {postfix_expression}')
    print(f'Prefix notation: {prefix_expression}')
    result = evaluate_postfix(postfix_expression)
    print(f'Evaluation result: {result}')