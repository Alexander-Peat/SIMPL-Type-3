#Helpful websites:
#brilliant.org/wiki/shunting-yard-algorithm/#the-shunting-algorithm
#mathcenter.oxford.emory.edu/site/cs171/shuntingYardAlgorithm/

def infix_to_rpn(infix_expression):
    operator_stack = []
    output = []
    infix_expression = list(infix_expression) #convert to a list

    def find_operator_precedence(op): #+ & - are 0, * & /, and ^ is 2
        op_prec = 0

        if op == "+" or op == "-":
            op_prec = 0
        elif op == "*" or op == "/":
            op_prec = 1
        elif op == "^":
            op_prec = 2

        return op_prec

    while len(infix_expression) > 0: #while there are tokens to be read
        if infix_expression[0].isnumeric(): #if it's a number...
            number = ""

            if len(infix_expression) == 1:
                number = infix_expression[0]
                infix_expression = infix_expression[1:]
            else:
                while len(infix_expression) > 1 and infix_expression[0].isnumeric():
                    number = number + infix_expression[0]
                    infix_expression = infix_expression[1:]

            output.append(number)

        elif(
            infix_expression[0] == "+"
            or infix_expression[0] == "-"
            or infix_expression[0] == "*"
            or infix_expression[0] == "/"
            or infix_expression[0] == "^"
        ):
            token_precedence = find_operator_precedence(infix_expression[0])

            if len(operator_stack) == 0:
                top_stack_precedence = 0
            else:
                top_stack_precedence = find_operator_precedence(operator_stack[-1])

            while top_stack_precedence > token_precedence:
                top_operator = operator_stack.pop()
                output.append(top_operator)

                top_stack_precedence = find_operator_precedence(operator_stack[-1])

            operator = infix_expression[0]
            infix_expression = infix_expression[1:]
            operator_stack.append(operator)

        elif infix_expression[0] == "(":
            operator = infix_expression[0]
            infix_expression = infix_expression[1:]
            operator_stack.append(operator)

        elif infix_expression[0] == ")":
            while operator_stack[-1] != "(":
                operator = operator_stack.pop()
                output.append(operator)

            operator_stack.pop()
            infix_expression = infix_expression[1:]

    while len(operator_stack) > 0:
        operator = operator_stack.pop()
        output.append(operator)

    final_output = ""

    for loop in range(len(output)):
        final_output = final_output + output[loop]
        final_output = final_output + ","

    final_output = final_output[:-1]

    return final_output

print(infix_to_rpn("2+3^2"))
