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

def rpn_evaluator(rpn_expression):
    intermediate_stack = []
    stack = []
    
    for loop in range(rpn_expression.count(",") + 1):
        num = ""
        while len(rpn_expression) >= 1 and rpn_expression[0] != ",":
            num = num + rpn_expression[0]
            rpn_expression = rpn_expression[1:]
        else:
            rpn_expression = rpn_expression[1:]
                
            intermediate_stack.append(num)

    for loop in range(len(intermediate_stack)):
        if (
            intermediate_stack[loop] != "+"
            and intermediate_stack[loop] != "-"
            and intermediate_stack[loop] != "*"
            and intermediate_stack[loop] != "/"
            and intermediate_stack[loop] != "^"
        ):
            stack.append(intermediate_stack[loop])
        else:
            stack.append(intermediate_stack[loop])

            operator = stack.pop()
            operand2 = str(stack.pop())
            operand1 = str(stack.pop())
            result = 0

            if operand1.count(".") == 0:
                operand1 = int(operand1)
            else:
                operand1 = float(operand1)

            if operand2.count(".") == 0:
                operand2 = int(operand2)
            else:
                operand2 = float(operand2)

            if operator == "+":
                result = operand1 + operand2
            elif operator == "-":
                result = operand1 - operand2
            elif operator == "*":
                result = operand1 * operand2
            elif operator == "/":
                result = operand1 / operand2
            elif operator == "^":
                result = operand1 ** operand2

            stack.append(result)

    return stack[0]

input_expression = ""
while True:
    input_expression = str(input("Enter an expression: "))

    input_expression = "(" + input_expression + ")"
    
    rpn_expression = infix_to_rpn(input_expression)
    answer = rpn_evaluator(rpn_expression)
    print(input_expression + " = " + str(answer))
