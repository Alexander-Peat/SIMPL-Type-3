#TODO: remember that the 'LET' command isn't just for initialising variables. It's also for doing mathematics and string concatenation
#E.g. 'LET INT NUMBER = INT 5 + INT 10' or 'LET STR MESSAGE = STR "Hello, " + VAR WORLD_STRING'
#Maybe make a function that takes the 'right_side' of the equal sign and finds the operators, variable types, and variables themselves
#and then does the correct operation (be it arithmetic or concatenation).

def space_remover(line): #this function removes the spaces from lines of code, except those within speechmarks ("---")
    line = list(line) #turn the line into a list

    new_list = [] #initialise the new_list list
    found_speechmark = False #initialise the found_speechmark variable to be false
    
    for spec_char in range(len(line)): #loop for every specific character in the list
        if line[spec_char] != '"' and line[spec_char] != " " and found_speechmark == False: #if the specific character is not a speechmark and is also not a space and the found_speechmark variable is false
            new_list.append(line[spec_char]) #add the specific character to the new list
            
        elif line[spec_char] == '"' and found_speechmark == False: #if the specific character is a speechmark and a speechmark hasn't been found yet
            found_speechmark = True #set the found_speechmark variable to true
            new_list.append(line[spec_char]) #add the specific character to the new list
        elif line[spec_char] == '"' and found_speechmark == True: #if the specific character is a speechmark and a speechmark has been found
            found_speechmark = False #set the found_speechmark variable to false
            new_list.append(line[spec_char]) #add the specific character to the new list
            
        elif line[spec_char] != '"' and found_speechmark == True: #if the specific character is not a speechmark and is not a space and a speech mark has been found
            new_list.append(line[spec_char]) #add the specific character to the new list

    #print(new_list) #diagnostic print

    new_string = "" #initialise an empty string as new_string
    
    for loop in range(len(new_list)): #loop for the length of the new_list
        new_string = new_string + new_list[loop] #add each character to the new string

    return new_string

def print_command(line, var_dict): #this function manages print commands
    line = line[5:] #remove the first five characters from the line so that 'PRINTSTR"Hello, World!";' becomes 'STR"Hello, World!";'
    #'PRINTVARTEST_STRING;' becomes 'VARTEST_STRING;'

    if line[0:3] == "STR": #if the first three characters of the line are 'STR'
        line = line[3:] #remove the first three characters of the line so that 'STR"Hello, World!";' becomes '"Hello, World!";'

        line = line[1:] #remove the first character from the line so that '"Hello, World!";' becomes 'Hello, World!";'

        print_line = "" #initialise print_line as an empty variable
    
        while line[0] != '"': #while the first character of the line is not a speechmark
            print_line = print_line + line[0] #add the first character of the line to the print_line variable
            line = line[1:] #remove the first character from the line

        print(print_line) #print the print line

    elif line[0:3] == "VAR": #if the first three characters of the line are 'VAR'
        line = line[3:] #remove the first three characters from the line so that 'VARTEST_STRING;' becomes 'TEST_STRING;'

        var_to_print = "" #initialise an empty variable as 'var_to_print'

        while line[0] != ";": #while the first character of the line is not a semicolon
            var_to_print = var_to_print + line[0] #add the first character of the line to the var_to_print variable
            line = line[1:] #remove the first character from the line

        print(var_dict[var_to_print]) #print the variable stored in the variable dictionary

def line_command(line, var_dict): #LETVARIABLE_NAME={type}SUCHANDSUCH
    line = line[3:] #LETVARIABLE_NAME={type}SUCHANDSUCH becomes VARIABLE_NAME={type}SUCHANDSUCH

    variable_name = ""
    while line[0] != "=":
        variable_name = variable_name + line[0]
        line = line[1:]

    line = line[1:] #={type}SUCHANDSUCH becomes {type}SUCHANDSUCH

    if line[0:3] == "STR":
        

def single_line_interpreter(line, var_dict): #this function interprets single lines of SIMPL code. 'var_dict' means 'Variable Dictionary'

    line = space_remover(line) #remove the spaces from the line
    
    if line[0:5] == "PRINT": #if the first five characters of the line are 'PRINT'
        print_command(line, var_dict) #refer to the print function

    elif line[0:3] == "LET": #if the first three characters of the line are 'LET'
        var_dict = let_command(line, var_dict) #refer to the print function

    return var_dict

#---Testing Area---

print("variable dictionary:")
print(variable_dictionary)
