#SIMPL Type 3 subroutine_utilities module
#Copyright (c) 2025, Alexander Peat

def subroutine_creator_editor(command, subroutine_dictionary): #the subroutine creator or editor function
    if command[1:2] not in subroutine_dictionary: #if the subroutine name is not already in the subroutine dictionary, then...
        specific_subroutine = [""] * 10000 #initialises the specific subroutine as a list

    else:
        specific_subroutine = subroutine_dictionary.get(command[1:2]) #gets the the list with the key of the subroutine name from the subroutine_dictionary and assigns it to the variable 'specific_subroutine'

    command = command[1:] #'/X;10 P;S;Hello, World;' becomes 'X;10 P;S;Hello, World;'

    subroutine_name = "" #initialises the variable that holds the name of the subroutine
    subroutine_name = command[0] #set the subroutine_name variable to first line
    command = command[1:] #removes the first character from the line so that 'X;10 P;S;Hello, World;' becomes '10 P;S;Hello, World;'

    subroutine_line_number = "" #initialises the variable that holds the specific line number of this subroutine
    while command[0] != " ": #while the first character of the line is not a space
        subroutine_line_number = subroutine_line_number + command[0] #add the first character of the line to the subroutine_line_number variable
        command = command[1:] #removes the first character of the line so that '10 P;S;Hello, World;' becomes '0 P;S;Hello, World;'

    command = command[1:] #removes the first character of the line so that ' P;S;Hello, World;' becomes 'P;S;Hello, World;'

    actuall_code = command #set what is left of the line to the variable 'actuall_code'
    subroutine_line_number = int(subroutine_line_number) #converts the subroutine_line_number variable to an integer
    specific_subroutine[subroutine_line_number - 1] = actuall_code #set the line of code to its index in the specific subroutine

    subroutine_dictionary.update({subroutine_name: specific_subroutine}) #update the dictionary to include the subroutine_name as the key and the specific_subroutine as the value

    return subroutine_dictionary

def subroutine_lister(subroutine_dictionary, subroutine_name): #the subroutine_lister function
    try: #try to execute
        specific_subroutine = subroutine_dictionary.get(subroutine_name) #set the specified subroutine to equal the subroutine dictionary's thing

        for loop in range(len(specific_subroutine)): #loop for the length of the specified subroutine
            if specific_subroutine[loop] != "": #if the specific instance of the subroutine is not an empty string
                print(str(loop + 1) + " " + specific_subroutine[loop]) #print the specific string along with a line number

    except: #if something went wrong...
        print("subroutine " + subroutine_name + " not found or something else failed")
