#TODO: continue the merge of the evaluater and parser functions into one big one
#Also, think about how you could make an improved version that can have as many operators

def evaluate_expression(expression): #evaluetes mathematical expressions with consideration for BODMAS

    #expression = remove_whitespace(expression)

    left_operand = "" #initialises the left_operand variable as an empty string
    bracket_depth = 0 #initialises the bracket_depth variable as an integer with the value 0

    while True: #loop forever until broken
        if (expression[0] == "+" or expression[0] == "-" or expression[0] == "/" or expression[0] == "*") and bracket_depth == 0: #if the first character of the string is either +, -, /, or * AND the bracket level is 0...
            break #break the loop and thus return the left operand

        if expression[0] == "(": #if the first character of the string is an opening bracket
            bracket_depth = bracket_depth + 1 #add one to the bracket depth, effectively telling the computer that we are inside (another) layer of brackets
        elif expression[0] == ")": #if the first character of the string is a closing bracket
            bracket_depth = bracket_depth - 1 #subtract one from the bracket depth. This tells the computer we have left a layer of brackets

        left_operand = left_operand + expression[0] #does the 'coveted' add the first character of the expression to the left_operand
        expression = expression[1:] #remove the first character from the expression variable

    operator = "" #initialise the operator variable as an empty string
    operator = expression[0] #make the operator variable the first character of the expression string
    expression = expression[1:] #remove the first character from the expression variable

    if expression[0] == "*": #if the first character of the expression is another asterisk (this would only happen with powers where the notation is 'x**y'
        operator = expression[0] #make the operator variable the first character of the expression string
        expression = expression[1:] #remove the first character from the expression variable

    right_operand = "" #initialise the right_operand variable as an empty string
    right_operand = expression #assign the value of the expression variable to the right_operand variable

    #we can do this ^ because a mathematical expression without the left operand and the operator is just the right operand

    if left_operand[0] == "(" and left_operand[-1] == ")": #if the first and last characters of the left operand variable are brackets
