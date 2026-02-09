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

print(rpn_evaluator("2,3,4,*,2,3,^,1,8,+,-,+,+"))
