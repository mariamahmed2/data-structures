class Stack:
    '''Python implementation the stack'''

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def InfixToPostfix(expression):
        '''infix to postfix conversion'''

        # Precedence
        prec = {}
        prec["*"] = 3
        prec["^"] = 3
        prec["/"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1

        # Create an empty stack called data_stack for keeping operators. Create an empty list for output.
        data_stack = Stack()
        postfix_exp = []
        tokens = expression

        for token in tokens:
            # If the token is an operand, append it to the end of the output list.
            if token in "abc":
                postfix_exp.append(token)

            # If the token is a left parenthesis, push it on the data_stack.
            elif token == '(':
                data_stack.push(token)
            # elif tokens + tokens[token] == "--":
            #     pass

            # If the token is a right parenthesis, pop the data_stack until the corresponding left parenthesis is removed.
            elif token == ')':
                top_token = data_stack.pop()
                while top_token != '(':
                    # Append each operator to the end of the output list.
                    postfix_exp.append(top_token)
                    top_token = data_stack.pop()
            else:
                # If the token is an operator, *, /, +, or -, push it on the data_stack.
                # first remove any operators already on the data_stack that have higher or equal precedence and append them to the output list.
                while (not data_stack.is_empty()) and (prec[data_stack.peek()] >= prec[token]):
                    postfix_exp.append(data_stack.pop())
                data_stack.push(token)

        # Any operators still on the stack can be removed and appended to the end of the output list.
        while not data_stack.is_empty():
            postfix_exp.append(data_stack.pop())

        return "".join(postfix_exp)


def eval_postfix(postfixExpr):
    operand_stack = Stack()
    tokenList = postfixExpr
    for token in tokenList:
		# If the token is an operand, convert it from a string to an integer and push the value onto stack
        if token in "0123456789":
            operand_stack.push(int(token))
        # If the token is an operator, *, /, +, or -, Pop the operandStack twice.
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            # Perform the arithmetic operation.
            result = evaluate(token,operand1,operand2)
            # Push the result back on the stack.
            operand_stack.push(result)
    return operand_stack.pop()

def evaluate(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "^":
        return op1 ^ op2
    else:
        print("Error")


exp = input()
post = InfixToPostfix(exp)

print(post)

a_val = input( )
post = post.replace("a",a_val[2:])

b_val = input()
post = post.replace("b",b_val[2:])

c_val = input( )
post = post.replace("c",c_val[2:])


res = eval_postfix(post)
print(res)


# (a+b+c)
# a=1
# b=2
# c=3
