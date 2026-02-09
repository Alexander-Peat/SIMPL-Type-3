#SIMPL Type 3 Interpreter
#Copyright (c) 2025, Alexander Peat
#Author: Alexander Peat

#---Library Imports---
import simpl_type_3_get_time as get_time
#---------------------

variable_dictionary = {} #dictionary storing all the SIMPL variables with the key being the name and the value being the variable value

def line_reader(line):
    global variable_dictionary #tells line_reader function to look for the variable_dictionary dictionary outside itself
    global line_counter #tells line_reader function to look for the line_counter variable outside itself
    
    if line[0] == "I": #if the first character in the line is 'I'
        line = line[2:] #removes the first two characters so that 'I;N;number_variable;0;' is now 'N;number_variable;0;'

        init_type_of_data = "" #initialises the variables type (float (F), number (N), or float (F))
        
        if line[0] == "S": #checks what type of data it is and assigns it to the init_type_of_data
            init_type_of_data = "S"
        elif line[0] == "N":
            init_type_of_data = "N"
        elif line[0] == "F":
            init_type_of_data = "F"

        line = line[2:] #removes the next two characters so that 'N;number_variable;0;' is now 'number_variable;0;'

        init_variable_name = "" #initialises the variable name
        
        while line[0] != ";": #checks if the first character is not a semicolon
            init_variable_name = init_variable_name + line[0] #if it isn't, then the character gets added to the init_variable_name
            line = line[1:] #removes the first character from the line; if it was the first loop of the while loop, it would go from 'number_variable;0;' to 'umber_variable;0;' until the semicolon is met

        line = line[1:] #once the semicolon is hit, said semicolon is removed so that ';0;' is now '0;'

        init_variable_value = ""

        while line[0] != ";": #does the same with the variable value as is done with the variable name
            init_variable_value = init_variable_value + line[0] #same logic
            line = line[1:]

        line = line[1:] #the line goes from ';' to ''

        if init_type_of_data == "S": #checks if the type of data is a string
            init_variable_value = str(init_variable_value) #if it is, it changes the variable value to a string
        elif init_type_of_data == "N": #checks if the type of data is a number
            init_variable_value = int(init_variable_value) #if it is, it changes the variable value to a number
        elif init_type_of_data == "F": #checks if the type of data is a float
            init_variable_value = float(init_variable_value) #if it is, it changes the variable value to a float

        variable_dictionary.update({init_variable_name: init_variable_value}) #updates the variable dictionary to include the variable and its value
        #the update function is really useful

    elif line[0] == "U": #if the first character in the line is 'U'
        line = line[2:] #removes the first two characters so that 'U;N;number_variable;Enter a number: ;' is now 'N;number_variable;Enter a number: ;'

        input_type_of_data = ""

        if line[0] == "S": #checks what type of data it is and assigns it to the input_type_of_data
            input_type_of_data = "S"
        elif line[0] == "N":
            input_type_of_data = "N"
        elif line[0] == "F":
            input_type_of_data = "F"

        line = line[2:] #removes the next two characters so that 'N;number_variable;Enter a number: ;' is now 'number_variable;Enter a number: ;'

        input_variable_name = "" #initialises the variable name
        
        while line[0] != ";": #checks if the first character is not a semicolon
            input_variable_name = input_variable_name + line[0] #if it isn't, then the character gets added to the input_variable_name
            line = line[1:] #removes the next character so that 'number_variable;Enter a number: ;' is now 'umber_variable;Enter a number: ;' this repeats until the code hits the semicolon

        line = line[1:] #once the semicolon is hit, said semicolon is removed so that ';Enter a number: ;' is now 'Enter a number: ;'
        print(input_variable_name)
        input_variable_prompt = "" #initialises the input prompt variable

        while line[0] != ";": #same logic as the while loop above
            input_variable_prompt = input_variable_prompt + line[0]
            line = line[1:]

        line = line[1:] #once the semicolon is hit, said semicolon is removed so that ';' is now ''

        input_variable_value = input(input_variable_prompt) #prompts the user with the input prompt

        if input_type_of_data == "S": #checks if the type of data is a string
            input_variable_value = str(input_variable_value) #if it is, it changes the variable value to a string
        elif input_type_of_data == "N": #checks if the type of data is a number
            input_variable_value = int(input_variable_value) #if it is, it changes the variable value to a number
        elif input_type_of_data == "F": #checks if the type of data is a float
            input_variable_value = float(input_variable_value) #if it is, it changes the variable value to a float

        variable_dictionary.update({input_variable_name: input_variable_value})

    elif line[0] == "P": #if the first character in the line is 'U'
        line = line[2:] #removes the first two characters so that 'P;S;Hello, World;' is now 'S;Hello, World;'

        print_is_var = False

        if line[0] == "V": #checks if the print statement is printing a variable
            print_is_var = True #if it is then it stores that 
        else: #otherwise...
            print_is_var = False #it remembers that, too

        line = line[2:] #removes the first two characters so that 'S;Hello, World;' is now 'Hello, World;'

        print_thing_to_print = "" #initialises the variable that stores the thing to be printed, variable or string

        while line[0] != ";": #checks if the first character is not a semicolon
            print_thing_to_print = print_thing_to_print + line[0] #if it isn't, then said first character is added to the printing variable
            line = line[1:] #the first character is then removed from the line variable

        line = line[1:] #removes the last character left in the string so that ';' is now ''

        print_thing_to_print_actuall = "" #initialises the actuall variable to be printed

        if print_is_var == True: #checks if the thing to be printed is a variable
            print_thing_to_print_actuall = variable_dictionary[print_thing_to_print] #if it is, then the interpreter looks it up in its dictionary
        else: #otherwise...
            print_thing_to_print_actuall = print_thing_to_print #the thing to be printed is set to the exact thing that was scanned from the line of code

        print(print_thing_to_print_actuall) #the thing to be printed is printed

    elif line[0] == "M": #if the first character in the line is 'M'
        line = line[2:] #removes the first two characters so that 'M;answer_variable;N;420;+;F;6.9;' is now 'answer_variable;N;420;+;F;6.9;'

        math_answer_variable = "" #initialises the variable that stores the answer variable

        while line[0] != ";": #while the first character of the line is not a semicolon
            math_answer_variable = math_answer_variable + line[0] #sets the first character to the 'math_answer_variable' variable
            line = line[1:] #removes the first character so that 'answer_variable;N;420;+;F;6.9;' is now 'nswer_variable;N;420;+;F;6.9;'

        line = line[1:] #removes the semicolon so that ';N;420;+;F;6.9;' is now 'N;420;+;F;6.9;'

        math_operand1_status = "" #initialises the variable that stores whether or not operand1 is a variable, number, or float

        math_operand1_status = line[0] #sets the aforementioned variable to the first character of the line
        line = line[2:] #removes the first two characters from the line so that 'N;420;+;F;6.9;' is now '420;+;F;6.9;'

        math_operand1_name = "" #initialises the variable that stores the name of operand1

        while line[0] != ";": #while the first character of the line is not a semicolon
            math_operand1_name = math_operand1_name + line[0] #sets the first character to the 'math_operand1_name' variable
            line = line[1:] #removes the first character so that '420;+;F;6.9;' is now '20;+;F;6.9;'

        line = line[1:] #removes the semicolon so that ';+;F;6.9;' is now '+;F;6.9;'

        math_operator_name = "" #initialises the variable that stores the operator

        while line[0] != ";": #while the first character is not a semicolon
            math_operator_name = math_operator_name + line[0] #adds the first character of the line to the 'math_operator_name' variable
            line = line[1:] #removes the first character of the line so that '+;F;6.9;' is now ';F;6.9;'

        line = line[1:] #removes the semicolon from the line so that ';F;6.9;' is now 'F;6.9;'

        math_operand2_status = "" #initialises the variable that stores whether or not operand2 is a variable, number, or float

        math_operand2_status = line[0] #sets the aforementioned variable to the first character of the line
        line = line[2:] #removes the first two characters from the line so that 'F;6.9;' is now '6.9;'

        math_operand2_name = "" #initialises the variable that stores the name of operand2

        while line[0] != ";": #while the first character of the line is not a semicolon
            math_operand2_name = math_operand2_name + line[0] #sets the first character to the 'math_operand2_name' variable
            line = line[1:] #removes the first character so that '6.9;' is now '.9;'

        line = line[1:] #removes the semicolon so that ';' is now ''

        #this initialises the variables with which the actuall arithmetic will be done with
        math_operand1_actuall = 0
        math_operand2_actuall = 0
        math_operator_actuall = math_operator_name

        if math_operand1_status == "V": #if operand1's type is a variable...
            math_operand1_actuall = variable_dictionary[math_operand1_name] #then its value is found by searching the variable dictionary
        elif math_operand1_status == "N": #if its a number...
            math_operand1_actuall = int(math_operand1_name) #then the value scanned from the line is converted into an integer
        elif math_operand1_status == "F": #and if its a float...
            math_operand1_actuall = float(math_operand1_name) #then the value is converted into a float

        #the same logic is used for operand2
        if math_operand2_status == "V":
            math_operand2_actuall = variable_dictionary[math_operand2_name]
        elif math_operand2_status == "N":
            math_operand2_actuall = int(math_operand2_name)
        elif math_operand2_status == "F":
            math_operand2_actuall = float(math_operand2_name)

        math_answer_actuall = 0 #initialises the variable that stores the actuall answer

        if math_operator_actuall == "+": #if the operator is '+'...
            math_answer_actuall = math_operand1_actuall + math_operand2_actuall #then it adds the operands
        elif math_operator_actuall == "-": #if the operator is '-'...
            math_answer_actuall = math_operand1_actuall - math_operand2_actuall #then it subtracts the operands
        elif math_operator_actuall == "*": #if the operator is '*'...
            math_answer_actuall = math_operand1_actuall * math_operand2_actuall #then it multiplies the operands
        elif math_operator_actuall == "/": #if the operator is '/'...
            math_answer_actuall = math_operand1_actuall / math_operand2_actuall #then it divides the operands
        elif math_operator_actuall == "**": #if the operator is '**'
            math_answer_actuall = math_operand1_actuall ** math_operator2_actuall #then it raises operand1 to the power of operand2

        variable_dictionary.update({math_answer_variable: math_answer_actuall})

    elif line[0] == "G": #if the first character is 'G'
        line = line[2:] #removes the first two characters so that 'G;10;' is now '10;'

        goto_line_number = "" #initialises the variable that holds the goto line

        while line[0] != ";": #while the first character in the line is not ';'
            goto_line_number = goto_line_number + line[0] #add the first character to the 'goto_line_number' variable
            line = line[1:] #remove the first character from the line so that '10;' is now '0;'

        line = line[1:] #removes the last character from the line so that ';' is now ''

        goto_line_number_actuall = 0 #initialises the actuall number to go to

        if goto_line_number.isnumeric() == True: #if the line number name is a number
            goto_line_number_actuall = int(goto_line_number) #then convert it to a number
        else: #otherwise
            goto_line_number_actuall = variable_dictionary[goto_line_number] #find the number in the dictionary

        line_counter = goto_line_number_actuall - 2 #set the line_counter to the goto_line_number_actuall minus one because of list indexing and minus one for the line_counter = line_counter + 1 in the while loop

    elif line[0] == "W": #if the first character is 'W'
        #the starting example string is 'W;N;69;=;F;6.9;20;'
        line = line[2:] #removes the first two characters from a string so that 'W;N;69;=;F;6.9;20;' is now 'N;69;=;F;6.9;20;'

        log_operand1_status = "" #initialises the variable that holds whether or not operand1 is number, float, or variable
        log_operand1_status = line[0] #makes the log_operand1_status variable the first character of the line
        line = line[2:] #removes the first two characters from the line so that 'N;69;=;F;6.9;20;' is now '69;=;F;6.9;20;'

        log_operand1_name = "" #initialises the variable that holds operand1's name

        while line[0] != ";": #while the first character of the line is not ';'
            log_operand1_name = log_operand1_name + line[0] #adds the first character of the line to the log_operand1_name variable
            line = line[1:] #removes the first character from the line so that '69;=;F;6.9;20;' is now '9;=;F;6.9;20;'

        line = line[1:] #removes the first character from the line so that ';=;F;6.9;20;' is now '=;F;6.9;20;'

        #logical operators: '=', '!', '<', '>'

        log_operator = "" #initialises the variable that stores the logical operator
        log_operator = line[0] #sets the log_operator variable to the first character of the line
        line = line[2:] #removes the first two characters from the string so that '=;F;6.9;20;' is now 'F;6.9;20;'

        log_operand2_status = "" #initialises the variable that holds whether or not operand2 is number, float, or variable
        log_operand2_status = line[0] #makes the log_operand2_status variable the first character of the line
        line = line[2:] #removes the first two characters from the line so that 'F;6.9;20;' is now '6.9;20;'

        log_operand2_name = "" #initialises the variable that holds operand2's name

        while line[0] != ";": #while the first character in the line is not ';'
            log_operand2_name = log_operand2_name + line[0] #adds the first character of the line to the log_operand2_name variable
            line = line[1:] #removes the first character from the line so that '6.9;20;' is now '.9;20;'

        line = line[1:] #removes the first character from the string so that ';20;' is now '20;'

        log_goto_number_name = "" #initialises the variable that holds the goto number name

        while line[0] != ";": #while the first character is not ";"
            log_goto_number_name = log_goto_number_name + line[0] #adds the first character of the line to the log_goto_number_name variable
            line = line[1:] #removes the first character from the line so that '20;' is now '0;'

        line = line[1:] #removes the last remaining character from the string so that ';' is now ''

        log_goto_number_actuall = 0 #initialises the variable that holds the actuall line number

        if log_goto_number_name.isnumeric() == True:
            log_goto_number_actuall = int(log_goto_number_name)
        else:
            log_goto_number_actuall = variable_dictionary[log_goto_number_name]

        log_operand1_actuall = "" #initialises the variable that holds the actuall value of operand1
        log_operand2_actuall = "" #initialises the variable that holds the actuall value of operand2

        if log_operand1_status == "S": #if operand1's status is a string...
            log_operand1_actuall = log_operand1_name #...then set the actuall variable to be the log_operand1_name variable
        elif log_operand1_status == "N": #otherwise, if the status is a number...
            log_operand1_actuall = int(log_operand1_name) #...then set the actuall variable to be the log_operand1_name variable converted to an integer
        elif log_operand1_status == "F": #otherwise, if the status is a float...
            log_operand1_actuall = float(log_operand1_name) #...then set the actuall variable to be the log_operand1_name variable converted to an float
        elif log_operand1_status == "V": #otherwise, if the status is a variable...
            log_operand1_actuall = variable_dictionary[log_operand1_name] #...then set the actuall variable to the value of the key called log_operand1_name

        if log_operand2_status == "S": #if operands's status is a string...
            log_operand2_actuall = log_operand2_name #...then set the actuall variable to be the log_operand2_name variable
        elif log_operand2_status == "N": #otherwise, if the status is a number...
            log_operand2_actuall = int(log_operand2_name) #...then set the actuall variable to be the log_operand2_name variable converted to an integer
        elif log_operand2_status == "F": #otherwise, if the status is a float...
            log_operand2_actuall = float(log_operand2_name) #...then set the actuall variable to be the log_operand2_name variable converted to an float
        elif log_operand2_status == "V": #otherwise, if the status is a variable...
            log_operand2_actuall = variable_dictionary[log_operand2_name] #...then set the actuall variable to the value of the key called log_operand2_name

        log_boolean_status = False #initialises the variable that stores whether or not the overall line of code is true or false

        if log_operator == "=": #if the logical operator is '='...
            if log_operand1_actuall == log_operand2_actuall: #...then check if the operation is true
                log_boolean_status = True #if it is, set the log_boolean_status to 'True'
            else: #otherwise...
                log_boolean_status = False #...set the log_boolean_status to 'False'

        elif log_operator == "!": #the logic is pretty much the same for all the other operators
            if log_operand1_actuall != log_operand2_actuall:
                log_boolean_status = True
            else:
                log_boolean_status = False

        elif log_operator == "<":
            if log_operand1_actuall < log_operand2_actuall:
                log_boolean_status = True
            else:
                log_boolean_status = False

        elif log_operator == ">":
            if log_operand1_actuall > log_operand2_actuall:
                log_boolean_status = True
            else:
                log_boolean_status = False

        if log_boolean_status == True: #if the condition in the if statement is found to be true...
            line_counter = log_goto_number_actuall - 2 #sets the line number to the log_goto_number_actuall variable minus one because of list indexing and minus one because after the line_reader function is executed, 1 is added to the line_number variable

    elif line[0] == "C": #if the first character is 'C'...
        #String Concatenation Syntax:
        #'C' for 'Concatenation'
        #C;concatenated_string;V;variable_one;V;variable_two; <- concatenates the two variables, 'variable_one' and 'variable_two' together and sets the value to the variable 'concatenated_string'
        #C;concatenated_string;S;Hello, ;S;World; <- non variable strings can also be concatenated
        #C;concatenated_string;S;Hello, ;V;variable_world; <- non variable strings and variables can be concatenated, too

        line = line[2:] #removes the first two characters so that 'C;concatenated_string;S;Hello, ;V;variable_world;' becomes 'concatenated_string;S;Hello, ;V;variable_world;'

        cat_answer_string = "" #holds the string that the complete, concatenated string goes

        while line[0] != ";": #while the first character of the line is not a semicolon...
            cat_answer_string = cat_answer_string + line[0] #adds the first character of the line to the variable 'cat_answer_string'
            line = line[1:] #removes the first character from the string so that 'concatenated_string;S;Hello, ;V;variable_world;' becomes 'oncatenated_string;S;Hello, ;V;variable_world;'

        line = line[1:] #removes the first character from the string so that ';S;Hello, ;V;variable_world;' becomes 'S;Hello, ;V;variable_world;'

        cat_operand1_stat = "" #holds whether or not operand1 of the concatenation is a string ('S') or a variable ('V')
        cat_operand1_stat = line[0] #adds the first character of the line to the cat_operand1_stat variable
        line = line[2:] #removes the first two characters from the line so that 'S;Hello, ;V;variable_world;' becomes 'Hello, ;V;variable_world;'

        cat_operand1_name = "" #holds either operand1 or operand1's variable name

        while line[0] != ";": #while the first character of the line is not a semicolon...
            cat_operand1_name = cat_operand1_name + line[0] #adds the first character of the line to the cat_operand1_name variable
            line = line[1:] #removes the first character from the line so that 'Hello, ;V;variable_world;' becomes 'ello, ;V;variable_world;'

        line = line[1:] #removes the first character from the line so that ';V;variable_world;' becomes 'V;variable_world;'

        cat_operand2_stat = "" #holds whether or not operand2 of the concatenation is a string ('S') or a variable ('V')
        cat_operand2_stat = line[0] #adds the first character of the line to the cat_operand2_stat variable
        line = line[2:] #removes the first two characters from the line so that 'V;variable_world;' becomes 'variable_world;'

        cat_operand2_name = "" #holds either operand2 or operand2's variable name

        while line[0] != ";": #while the first character of the line is not a semicolon...
            cat_operand2_name = cat_operand2_name + line[0] #adds the first character of the line to the 'cat_operand2_name' variable
            line = line[1:] #removes the first character from the line so that 'variable_world;' becomes 'ariable_world;'

        line = line[1:] #removes the last character from the string so that ';' becomes ''

        #these initialise the variables holding the actuall values of operands 1 and 2:
        cat_operand1_actuall = ""
        cat_operand2_actuall = ""

        if cat_operand1_stat == "V": #if the status of operand1 is 'V' (for variable)...
            cat_operand1_actuall = str(variable_dictionary[cat_operand1_name]) #then look up the name in the dictionary and set its value to the cat_operand1_actuall variable
        else: #otherwise...
            cat_operand1_actuall = str(cat_operand1_name) #set the cat_operand1_actuall variable to just equal the cat_operand1_name variable

        if cat_operand2_stat == "V": #if the status of operand2 is 'V' (for variable)...
            cat_operand2_actuall = str(variable_dictionary[cat_operand2_name]) #then look up the name in the dictionary and set its value to the cat_operand2_actuall variable
        else: #otherwise...
            cat_operand2_actuall = str(cat_operand2_name) #set the cat_operand2_actuall variable to just equal the cat_operand2_name variable

        cat_concatenated_string = "" #temporary variable that holds the two strings concatenated together
        cat_concatenated_string = cat_operand1_actuall + cat_operand2_actuall

        variable_dictionary.update({cat_answer_string: cat_concatenated_string}) #update the variable dictionary to have the new concatenated string at the key of the answer variable

    elif line[0] == "T": #if the first character of the line is 'T'
        #Time Syntax:
        #'T' for 'Time'
        #T;S;time_variable; <- assigns the variable 'time_variable' a string with the format xx:yy dd/mm/yyyy UTC
        #T;N;time_variable; <- assigns the variable 'time_variable' a number representing the number of seconds since the Unix Epoch

        line = line[2:] #removes the first two characters from the string so that 'T;S;time_variable;' becomes 'S;time_variable;'

        time_status = "" #initialises the variable that holds whether or not the time command is asking for the time string or the Unix Epoch
        time_status = line[0] #sets the first character of the line to the time_status variable
        line = line[2:] #removes the first two characters from the line so that 'S;time_variable;' becomes 'time_variable;'

        time_variable = "" #initialises the variable that holds the variable that the value gets assigned to

        while line[0] != ";": #whilst the first character of the line is not a semicolon
            time_variable = time_variable + line[0] #adds the first character of the line to time_variable
            line = line[1:] #removes the first character from the line so that 'time_variable;' becomes 'ime_variable;'

        line = line[1:] #removes the last character in the line so that ';' becomes ''

        time_variable_value = "" #initialises the variable that holds the value to be assigned to the variable
        
        if time_status == "S": #if the status is string...
            time_variable_value = get_time.get_time_string() #then assign the variable the time string
        else: #otherwise...
            time_variable_value = get_time.get_time_secs() #assign the variable the number of seconds since the Unix Epoch

        variable_dictionary.update({time_variable: time_variable_value}) #update the variable dictionary with the value
    
line_list = ["T;N;unix_epoch;", "T;S;time_string;", "P;V;unix_epoch;", "P;V;time_string;", "END"] #list full of all the code lines
line_counter = 0 #this variable holds the number that the line_reader function is processing at a given time

while True: #loop forever
    if line_list[line_counter] == "END": #if the line in question is 'END'
        break #break the loop
    elif line_list[line_counter] == "GOSUB": #subroutine inclusion
        pass #does nothing for now
    else: #otherwise...
        line_reader(line_list[line_counter])
        #try: #try to...
            #line_reader(line_list[line_counter]) #run the current line through the line_reader function
        #except KeyboardInterrupt: #but if the user presses ctrl + c...
            #print("escape at line " + str(line_counter + 1)) #print 'escape at line' plus whichever line it is
            #break #and then break
        #except Exception as error: #if it's any other type of error...
            #print("error at line " + str(line_counter + 1)) #print 'error at line' plus whichever line it is
            #print(error)
            #break #and then break

        line_counter = line_counter + 1 #adds one to the line counter variable so that the next time the loop comes around, the next line is referenced
        
print(variable_dictionary)
