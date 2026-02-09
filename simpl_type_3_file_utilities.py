#SIMPL Type 3 file_utilities module
#Copyright (c) 2025, Alexander Peat

#---Library Imports---
import simpl_type_3_get_time as get_time
#---------------------

def line_number_reader(line, code_list): #the line_number_reader function

    line_number = "" #initialises the variable that holds the given line's line number

    if line.isnumeric(): #if the whole line is just a number
        line = int(line) #then convert it to an integer
        code_list[line - 1] = "" #and then set its index minus one in the code list to ""
    else: #otherwise
        while line[0].isnumeric(): #while the first character of the line is a number
            line_number = line_number + line[0] #add the first character of the line to the line_number variable
            line = line[1:] #remove the first character of the line

        line_number = int(line_number) #convert the line_number variable to an integer
    
        while line[0] == " ": #while the first character of the line is a space
            line = line[1:] #remove the first character

            if len(line) == 0: #if there are no more characters left in the line
                code_list[line_number - 1] = "" #set the specific index to ""
                break #and break the program

        code_list[line_number - 1] = line #set the line to the list at the line number minus one

def code_list_lister(code_list): #the code_list_lister function

    for loop in range(len(code_list)): #loop for the length of the code list array
        if code_list[loop] != "": #if a specific index in the code_list list is not ""
            print(str(loop + 1) + " " + code_list[loop]) #then print it alongside its line number

def code_list_speclister(command_line, code_list): #the code_list_speclister function

    speclist_start_line = "" #initialises the variable that holds the starting line

    while command_line[0] != ",": #while the first character of the command line is not a comma
        speclist_start_line = speclist_start_line + command_line[0] #add the first character to the speclist_start_line variable
        command_line = command_line[1:] #remove the first character

    command_line = command_line[1:] #remove the first character from the command line

    speclist_end_line = "" #initialises the variable that holds the end line
    speclist_end_line = command_line #set this variable to equal what's left of the command_line variable

    if speclist_start_line.isnumeric() and speclist_end_line.isnumeric() and speclist_start_line < speclist_end_line: #check if the start and end lines are numbers and if the start is less than the end
        for loop in range((int(speclist_start_line) - 1), int(speclist_end_line)): #loop between the start and end lines
            if code_list[loop] != "": #if a specific index is not ""
                print(str(loop + 1) + " " + code_list[loop]) #then print it alongside the line number
    else: #otherwise...
        print("invalid format")

def print_directory(): #the print_directory function
    with open("C:\\Users\\ajpea\\Things I've Written Or Created\\SIMPL Type 3\\simpl_type_3_program_files\\simpl_type_3_directory.txt", "r") as dir_file: #open the directory file and refer to it as 'dir_file'
        directory_contents = dir_file.readlines() #scan the contents of the file and put it into the list 'directory_contents'

        for loop in range(len(directory_contents)): #loop for the length of the list
            total_name = directory_contents[loop] #set the total_name variable to a specific instance of the list --> 'hh:mm dd/mm/yyyy UTC simpl_type_3_[file name].txt\n'
            front = total_name[:16] #set the front variable to the first 16 characters of the total_name --> 'hh:mm dd/mm/yyyy'
            total_name = total_name[34:] #remove the first 34 characters from the total_name --> 'hh:mm dd/mm/yyyy UTC simpl_type_3_[file name].txt' becomes '[file name].txt\n'
            total_name = total_name[:-1] #remove the last 2 characters from the total_name --> '[file name].txt\n' becomes '[file name].txt'

            total_name = front + " " + total_name

            print(total_name)

def clear(code_list): #the clear function

    for loop in range(len(code_list)): #for every instance in the code_list 
        if code_list[loop] != "": #if its not empty
            code_list[loop] = "" #make it empty

def load_file(file_name, code_array, subroutine_dictionary): #the load_file function
    try: #try to...
        with open(("C:\\Users\\ajpea\\Things I've Written Or Created\\SIMPL Type 3\\simpl_type_3_program_files\\simpl_type_3_non_dir_files\\simpl_type_3_" + file_name[:-4]) + ".txt", "r") as load_file: #open the specified file and refer to it as 'load_file'
            temporary_list = load_file.readlines() #set all the lines of the file to the list 'temporary_list'
            subroutine_to_save_to = "" #initialises the variable that holds which subroutine to save to
            
            for loop in range(len(temporary_list)): #for everything in temporary_list
                if temporary_list[loop][0].isnumeric(): #if the first character of the line is a number
                    pass #do nothing
                
                elif temporary_list[loop][0:3] == "SUB": #if the first three characters in the string are 'SUB'
                    temporary_list[loop][3:] #remove the first three characters
                    subroutine_to_save_to = temporary_list[loop][-2] #set the subroutine_to_save_to variable to the first character of the temporary_list
                    temporary_list[loop] = "" #set the string to be empty
                    
                elif temporary_list[loop][0:6] == "ENDSUB": #if the first six characters in the string are 'ENDSUB'
                    temporary_list[loop] = "" #remove the string from the temporary list
                    subroutine_to_save_to = "" #set the subroutine to save to to be null

                if len(temporary_list[loop]) > 0: #if the length of the specific line is greater than zero
                    line_number = "" #initialises the varable that holds the line number of this specific bit of code
            
                    while temporary_list[loop][0].isnumeric(): #while the first character of the line is a number...
                        line_number = line_number + temporary_list[loop][0] #add said character to the line_number variable
                        temporary_list[loop] = temporary_list[loop][1:] #remove the first character from this specific line of code 

                    while temporary_list[loop][0] == " ": #while the first character of the line of code is a space...
                        temporary_list[loop] = temporary_list[loop][1:] #remove the first character from this specific line of code

                    temporary_list[loop] = temporary_list[loop][:-1] #remove the last two characters (\n) from the line of code

                if subroutine_to_save_to == "" and len(temporary_list[loop]) > 0: #if the subroutine_to_save_to variable is default and the length of the line is greater than zero
                    code_array[int(line_number) - 1] = temporary_list[loop] #set the rest of the line of code to the code_array with the specific index of the line number
                    #print(temporary_list[loop]) #diagnostic print; temporary
                elif len(temporary_list[loop]) > 0: #otherwise, if the length of this specific line of code is still greater than zero, load the specific line of code to the specified subroutine in the subroutine dictionary
                    working_list = subroutine_dictionary.get(subroutine_to_save_to) #get the subroutine from the subroutine dictionary
                
                    if working_list is None: #if the subroutine doesnt exist and, thus, the program assigns the type of None to the working list
                        working_list = [""] * 10000 #create a subroutine

                    #print(working_list)
                       
                    working_list[int(line_number) - 1] = temporary_list[loop] #add the line of code (and only the code! not the fucking number) to its respective line
                    subroutine_dictionary.update({subroutine_to_save_to: working_list}) #and update the dictionary with it

        print("file successfully read to prompt")
        
    except Exception as error: #if that doesn't work...
        print("error loading file")
        print("error: " + str(error))

    return code_array, subroutine_dictionary #return the updated code_list and subroutine_dictionary objects

def save_code(save_name, code_list, subroutine_dictionary): #save code function
    dir_save_name = save_name #save the name of the file (from the user's perspective) to a variable for the directory file to store
    save_name = "simpl_type_3_" + save_name #add 'simpl_type_3_" to the front of the save_name variable
    with open(("C:\\Users\\ajpea\\Things I've Written Or Created\\SIMPL Type 3\\simpl_type_3_program_files\\simpl_type_3_non_dir_files\\" + save_name[:-4] + ".txt"), "w") as save_file: #open the file specified and refer to it as 'save_file'
        for loop in range(len(code_list)): #loop for the length of the code list
            if code_list[loop] != "": #if a specific index of the code list is not empty,
                save_file.write(str(loop + 1) + " " + code_list[loop] + "\n") #then write it to the file, alongside it's line number

        #print(subroutine_dictionary)
        
        for key in subroutine_dictionary: #for every subroutine in the subroutine dictionary
            save_file.write("SUB" + key + "\n") #head the line of the subroutine's lines with its name
            specific_subroutine = subroutine_dictionary.get(key) #set the specific_subroutine list to the value of this key in the dictionary
            for loop in range(len(specific_subroutine)): #for every line of code in this specific subroutine
                if specific_subroutine[loop] != "": #if this specific line of code is not empty
                    save_file.write(str(loop + 1) + " " + specific_subroutine[loop] + "\n") #then write it to the file
            save_file.write("ENDSUB" + key + "\n")        

    with open("C:\\Users\\ajpea\\Things I've Written Or Created\\SIMPL Type 3\\simpl_type_3_program_files\\simpl_type_3_directory.txt", "a+") as dir_file: #open the directory file and refer to it as 'dir_file'
        save_name_found = False #initialise a variable that holds whether or not the save name already exists in the directory file
        #this basically means if you are modifying a file and save it, there won't be duplicate names in the directory file

        directory_contents = dir_file.readlines() #set all the lines in the directory to a list called 'directory_contents'

        for loop in range(len(directory_contents)): #loop for the length of the directory_contents list
            #the standard file name for a SIMPL Type 3 file is 'hh:mm dd/mm/yyyy simpl_type_3_[file name].txt'
            specific_instance = directory_contents[loop][30:] #set 'specific_instance' to '[file name].txt'
            specific_instance = specific_instance[:-5] #set specific_instance to '[file name]'

            if specific_instance == save_name: #if '[file name]' is the save name
                save_name_found = True #then say you found it

        if save_name_found == False: #if you didn't find it...
            name_to_save_to_dir = "" #initialises a variable to hold the string to be saved to the directory

            name_to_save_to_dir = name_to_save_to_dir + get_time.get_time_string() #add the time string to the front of the string
            name_to_save_to_dir = name_to_save_to_dir + " " #add a space to seperate it from the file name
            name_to_save_to_dir = name_to_save_to_dir + "simpl_type_3_" #add this prefix to the filename
            name_to_save_to_dir = name_to_save_to_dir + dir_save_name #add '[file name].txt' to the variable
            name_to_save_to_dir = name_to_save_to_dir + "\n" #add the new line thing to the end of the message

            dir_file.write(name_to_save_to_dir) #write the overall string to the directory file
