# define a function to tokenize the input expression
def tokenize(expression):
    # split the expression into a list of tokens
    tokens = expression.strip().split()

    # convert numbers from strings to floats
    for i, token in enumerate(tokens):
        if token.isdigit():
            tokens[i] = float(token)

    return tokens

# define the shunting-yard algorithm
def shunting_yard(tokens):
    queue = []
    stack = []

    operators = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    for token in tokens:
        # if it's a number add it to queue
        if type(token) == float:
            queue.append(token)

        # if it's an operator
        if token in operators:
            # while there is an operator at the top of the stack with greater precedence            
            if stack and stack[-1] in operators:
                current_operator = token
                last_operator_precedence = operators[stack[-1]]
                current_operator_precedence = operators[current_operator]

                while stack and (current_operator_precedence <= last_operator_precedence):
                    # pop the operator from the stack and add it to the queue
                    queue.append(stack.pop())

            # push the operator to the stack
            stack.append(token)

        # if it's a left parenthesis push it to the stack
        if token == '(':
            stack.append(token)

        # if it's a right parenthesis
        if token == ')':
            # pop the stack until you find the matching left parenthesis
            while stack and stack[-1] != '(':
                queue.append(stack.pop())

            # pop the left parenthesis from the stack but not to the queue
            stack and stack.pop()

    # pop the remaining operators from the stack and add them to the queue
    while stack:
        queue.append(stack.pop())

    return queue

def evaluate(queue):
    stack = []

    for token in queue:
        print(stack)

        if type(token) == float:
            stack.append(token)

        if token == '+':
            right = stack.pop()
            left = stack.pop()
            stack.append(left + right)

        if token == '-':
            right = stack.pop()
            left = stack.pop()
            stack.append(left - right)

        if token == '*':
            right = stack.pop()
            left = stack.pop()
            stack.append(left * right)

        if token == '/':
            right = stack.pop()
            left = stack.pop()
            stack.append(left / right)

    return stack.pop()

expr = "(( 1 + 2 ) * 3) * ( 4 + 5 ) / ( 6 - 7 )"

tokens = tokenize(expr)
queue = shunting_yard(tokens)
# result = evaluate(queue)

print(queue)