#Helpful websites:
#brilliant.org/wiki/shunting-yard-algorithm/#the-shunting-algorithm
#mathcenter.oxford.emory.edu/site/cs171/shuntingYardAlgorithm/

operator_stack = []
infix_expression = "(9+1)+2*3" #(9+1)+2*3 OR 91+23*+ = 16
infix_expression = list(infix_expression)
output = []

def find_operator_precedence(op): #+ & - are 0, * & / are 1, and ^ is 2
    op_prec = 0
    
    if op == "+" or op == "-":
        op_prec = 0
    elif op == "*" or op == "/":
        op_prec = 1
    elif op == "^":
        op_prec = 2

    return op_prec

while len(infix_expression) > 0: #while there are tokens to be read
    print("Current Token:")
    print(infix_expression[0])
    
    if infix_expression[0].isnumeric(): #if it's a number
        print(str(infix_expression[0]) + " is a number")
        #number = infix_expression[0]
        #infix_expression = infix_expression[1:]
        #output.append(number) #add it to queue
        #print("Output:")
        #print(output)

        number = ""

        if len(infix_expression) == 1:
            number = infix_expression[0]
            infix_expression = infix_expression[1:]
        else:
            while len(infix_expression) > 1 and (infix_expression[0].isnumeric()):
                number = number + infix_expression[0]
                infix_expression = infix_expression[1:]

        output.append(number)
        print("Output:")
        print(output)
        

    elif(
        infix_expression[0] == "+"
        or infix_expression[0] == "-"
        or infix_expression[0] == "*"
        or infix_expression[0] == "/"
        or infix_expression[0] == "^"
    ):
        print("Op Stack:")
        print(operator_stack)
        token_precedence = find_operator_precedence(infix_expression[0])

        if len(operator_stack) == 0:
            top_stack_precedence = 0
        else:
            top_stack_precedence = find_operator_precedence(operator_stack[-1])

        while top_stack_precedence > token_precedence:
            top_operator = operator_stack.pop()
            print("Op Stack:")
            print(operator_stack)
            output.append(top_operator)
            print("Output:")
            print(output)

            top_stack_precedence = find_operator_precedence(operator_stack[-1])

        operator = infix_expression[0]
        infix_expression = infix_expression[1:]
        operator_stack.append(operator)
        print("Op Stack:")
        print(operator_stack)

    elif infix_expression[0] == "(":
        operator = infix_expression[0]
        infix_expression = infix_expression[1:]
        operator_stack.append(operator)
        print("Op Stack:")
        print(operator_stack)

    elif infix_expression[0] == ")":
        while operator_stack[-1] != "(":
            operator = operator_stack.pop()
            print("Op Stack:")
            print(operator_stack)
            output.append(operator)
            print("Output:")
            print(output)

        operator_stack.pop()
        infix_expression = infix_expression[1:]

while len(operator_stack) > 0:
    operator = operator_stack.pop()
    print("Op Stack:")
    print(operator_stack)
    output.append(operator)
    print("Output:")
    print(output)

print("The output: ")
print(output)

final_output = ""
for loop in range(len(output)):
    final_output = final_output + output[loop]
    final_output = final_output + ","

final_output = final_output[:-1]

print("Final Output:")
print(final_output)
