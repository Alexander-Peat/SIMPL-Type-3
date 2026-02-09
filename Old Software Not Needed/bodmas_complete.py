def evaluate_expression(node):
    if isinstance(node, (int, float, str)):
        return node
    
    left = evaluate_expression(node["left"])
    operator = node["operator"]
    right = evaluate_expression(node["right"])
    
    if operator == "+":
        return int(left) + int(right)
    elif operator == "-":
        return int(left) - int(right)
    elif operator == "*":
        return int(left) * int(right)
    elif operator == "/":
        return int(left) / int(right)
    elif operator == "**":
        return int(left) ** int(right)

def expression_parser(expression):
    left_operand = "" #initialises the left_operand variable as an empty string

    bracket_depth = 0 #initialises the bracket_depth variable to 0

    while True: #loop forever
        if (expression[0] == "+" or expression[0] == "-" or expression[0] == "/" or expression[0] == "*") and bracket_depth == 0: #if the first character of the expression is +, -, /, or * and the bracket depth is 0 i.e. we are outside any brackets
            break #break the loop
        
        if expression[0] == "(": #if the first character of the string is an opening bracket...
            bracket_depth = bracket_depth + 1 #add one to the bracket depth
        elif expression[0] == ")": #if the first character of the string is an closing bracket...
            bracket_depth = bracket_depth - 1 #subtract one from the bracket depth
        
        left_operand = left_operand + expression[0] #...add the first character of expression to the left_operand variable
        expression = expression[1:] #remove the first character from expression so that "3+(2*3)" becomes "+(2*3)"

    operator = expression[0] #sets the first character of the expression variable to the operator variable
    expression = expression[1:] #remove the first character from the expression variable so that "+(2*3)" becomes "(2*3)"

    if expression[0] == "*": #if the first character of the expression variable is "*"
        operator = operator + expression[0] #add the first character of the expression variable to the operator variable
        expression = expression[1:] #remove the first character from the expression variable

    right_operand = expression #initialises the right_operand variable as the rest of the expression variable

    #print("left operand: " + left_operand)
    #print("operator: " + operator)
    #print("right_operand: " + right_operand)
    
    if left_operand[0] == "(" and left_operand[-1] == ")": #if the first and last characters of the left_operand variables are brackets...
        left_operand = left_operand[1:] #...remove the opening bracket
        left_operand = left_operand[:-1] #...and remove the closing bracket

        recursive_left_operand = left_operand #set the recursive_left_operand variable to equal the left_operand variable
        left_operand = {} #set the left_operand variable to equal an empty dictionary

        left_operand = expression_parser(recursive_left_operand) #set the left_operand variable to equal the result of the recursive_left_operand being put in the expression_parser function

    if right_operand[0] == "(" and right_operand[-1] == ")": #if the first and last characters of the right_operand variables are brackets...
        #print("before bracket removal " + right_operand)
        right_operand = right_operand[1:] #...remove the opening bracket
        right_operand = right_operand[:-1] #...and remove the closing bracket
        #print("after bracket removal " + right_operand)

        recursive_right_operand = right_operand #set the recursive_right_operand variable to equal the right_operand variable
        right_operand = {} #set the right_operand variable to equal an empty dictionary

        right_operand = expression_parser(recursive_right_operand)#set the right_operand variable to equal the result of the recursive_right_operand being put in the expression_parser function

    final_expression = {"left": left_operand, "operator": operator, "right": right_operand} #set up the 'final_expression' dictionary
    return final_expression #return it

value = 0
expression_dict = {}
string = ""
string = str(input("Enter a mathematical expresssion: "))

expression_dict = expression_parser(string)
#print(expression_dict)
value = evaluate_expression(expression_dict)
print(value)
