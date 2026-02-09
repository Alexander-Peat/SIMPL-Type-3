#TODO: Come up with own file extension for SIMPL files; already done it mate: '.sim'
#Also, have the 'clear' command apply to subroutines to
#Also Also, have the ability to type in a subroutine and a line number and then nothing, leaving the line cleared
#e.g. '/X10' or '/X10 ' would clear subroutine X's line 10 without any bugs
#Also Also Also, migrate the subroutine command code to their own functions in the subroutine_utilities folder

#fix the fucking file name shit

#SIMPL Type 3 Prompt/Main file
#Copyright (c) 2025, Alexander Peat
#Author: Alexander Peat
#Written in version 3.13.6

#---Library Imports---
import simpl_type_3_get_time as get_time
import simpl_type_3_file_utilities as file_utilities
import simpl_type_3_subroutine_utilities as subroutine_utilities
#---------------------

code_list = [""] * 10000
subroutine_dictionary = {}

#opening statement
print('''
SSSSSSSSS  IIIIIIIII  MMMMMMMMM  PPPPPPPPP  L
S              I      M   M   M  P       P  L
S              I      M   M   M  P       P  L
SSSSSSSSS      I      M   M   M  PPPPPPPPP  L
        S      I      M   M   M  P          L
        S      I      M   M   M  P          L
SSSSSSSSS  IIIIIIIII  M   M   M  P          LLLLLLLLL
-------------------------------------------------------------------------------------
Single Letter Interpreted Machine Programming Language (SIMPL) Interpreter and Prompt
Copyright (c) 2025, Alexander Peat
SIMPL Type 3
''')

while True: #loop forever
    command = "" #initialise the command variable

    try: #try to
        command = str(input(">")) #prompt the user with '>'
    except KeyboardInterrupt: #if there is a keyboard interrupt because the user pressed ctrl + c
        print("escape")
    except:
        print("error")

    #note that 'command' can also always be entered in uppercase as well

    if len(command) == 0: #if the length of the command is 0
        pass #pass

    elif command == "help" or command == "HELP": #if the command is 'help'
        print('''Command List:
'help' - prints the command list
'exit' - ends the program
'time' - prints the time in the format hh:mm dd/mm/yyyy
'unixtime' - prints the number of seconds since the unix epoch
'debug' - prints the entire code_list list
'list' - prints all the lines of code
'clear' - deletes all the lines of code
'speclist x,y' - prints the lines of code between lines x and y
'save [file name].txt' - saves the code currently in the prompt to a file with the specified name
'load [file name].txt' - loads the code saved in the specified file to the prompt
'dir' - prints out the file directory
'subdebug' - prints out all of the subroutines in the memory
'sublist [subroutine name/"all"]' - prints out either the specified subroutine or all of them in the memory
'subclear [subroutine name/"all"] - clears either the specified subroutine or all of them in the memory
'how' - how did i create this?''') #big ol' command list

    elif command == "exit" or command == "EXIT": #if the command is 'exit'
        print("exiting")
        break #end the program

    elif command == "time" or command == "TIME": #if the command is 'time'
        print(get_time.get_time_string()) #retrieve the time string from the get_time file and print it

    elif command == "unixtime" or command == "UNIXTIME": #likewise, if the command is unix time
        print(get_time.get_time_secs()) #retrieve the number of seconds from the unix epoch and print it

    elif len(command) > 0 and command[0].isnumeric(): #if the first character of the command is a number
        file_utilities.line_number_reader(command, code_list) #then call the line_number_reader on the line

    elif command == "debug" or command == "DEBUG": #if the command is 'debug'
        print(code_list) #print the entire code_list list

    elif command == "list" or command == "LIST": #if the command is 'list'
        file_utilities.code_list_lister(code_list) #call the code_list_lister()

    elif command == "clear" or command == "CLEAR": #if the command is 'clear'
        file_utilities.clear(code_list)

    elif command[0:8] == "speclist" or command[0:8] == "SPECLIST": #if the command is 'speclist'
        command = command[8:] #remove the 'speclist' part from the command
        while command[0] == " ": #while the first character of the rest of the command is a space
            command = command[1:] #remove the first character
        
        try: #try to run the parameters through the function
            file_utilities.code_list_speclister(command, code_list)
        except: #if there's an error...
            print("invalid format")

    elif command[0:4] == "save" or command[0:4] == "SAVE": #if the command is 'save'
        command = command[4:] #remove the 'save' part of the command

        if len(command) > 0: #if the length of the rest of the command is greater than 0
            while len(command) > 0 and command[0] == " ": #while the first character of the rest of the command is a space
                command = command[1:] #remove the first character
        
            if len(command) > 0 and command[-1] == "m" and command[-2] == "i" and command[-3] == "s" and command[-4] == "." and command.count(" ") == 0: #check if filename ends in '.txt' and the number of spaces left is 0
                file_utilities.save_code(command, code_list, subroutine_dictionary) #run the filename through the function and, hopefully, this should work
            else: #if the command does not satisfy these conditions...
                print("invalid format")
        else: #otherwise...
            print("invalid format")

    elif command[0:4] == "load" or command[0:4] == "LOAD": #if the command is 'load'
        command = command[4:] #remove the 'load' part of the command

        if len(command) > 0: #if the length of the rest of the command is greater than 0
            while len(command) > 0 and command[0] == " ": #while the first character of the rest of the command is a space
                command = command[1:] #remove the first character

            if len(command) > 0 and command[-1] == "m" and command[-2] == "i" and command[-3] == "s" and command[-4] == "." and command.count(" ") == 0: #check if filename ends in '.txt' and the number of spaces left is 0
                code_list, subroutine_dictionary = file_utilities.load_file(command, code_list, subroutine_dictionary)
            else: #if the command does not satisfy these conditions...
                print("invalid format")
        else: #otherwise...
            print("invalid format")

    elif command == "dir" or command == "DIR": #if the command is 'dir'
        file_utilities.print_directory() #execute the print_directory function

    elif command[0] == "/": #if the first character of the command is '/'
        try: #try to execute...
            subroutine_utilities.subroutine_creator_editor(command, subroutine_dictionary)
        except Exception as error: #if something went wrong, print the exception out
            print("subroutine error - " + str(error))

    elif command == "subdebug" or command == "SUBDEBUG":
        print(subroutine_dictionary)

    elif command[0:7] == "sublist" or command[0:7] == "SUBLIST" and len(command) > 7: #if the command starts with 'sublist' and the overall length of the command is greater than 7
        command = command[7:] #removes the first seven characters from the command
        while len(command) > 0 and command[0] == " ": #while the first character of the command is a space
            command = command[1:] #remove the first character from the command

        subroutine_name = "" #initialises the variable that holds the name of the subroutine
        subroutine_name = command #set the subroutine_name variable to command

        if command == "all" or command == "ALL": #if the command is 'all'
            if len(subroutine_dictionary) > 0: #if the length of the subroutine dictionary is greater than one
                print("subroutine list:")
                for key in subroutine_dictionary: #for all the keys in the subroutine dictionary
                    print(key) #print the specific key
            else: #otherwise
                print("no subroutines currently in program")
                
        elif len(command) == 1: #if the length of the subroutine is 1
            subroutine_utilities.subroutine_lister(subroutine_dictionary, subroutine_name) #call the subroutine_lister function with 'subroutine_dictionary' and 'subroutine_name' as the parameters
            
        else: #otherwise
            print("invalid format")

    elif command[0:8] == "subclear" or command[0:8] == "SUBCLEAR" and len(command) > 8: #if the command starts with 'subclear' and the overall length of the command is greater than 8
        command = command[8:] #remove the 'subclear' part of the command

        while len(command) > 0 and command[0] == " ": #if the length of the string is greater than 0 and the first letter of the command is a space
            command = command[1:] #remove the first character of the string

        if command == "all" or command == "ALL": #if the rest of the command is 'all'
            subroutine_dictionary.clear() #pops the keys out the dictionary............ must really hurt

        elif len(command) == 1: #if the length of the command is one
            try:
                subroutine_dictionary.pop(command)
            except KeyError:
                print("subroutine " + command + " does not exist")

        elif len(command) == 0: #if the length of the command is zero
            print("invalid format")

    elif command == "how" or command == "HOW": #if the command is 'how?'
        print("with divine intellect, you liberal fucktard")
        print('"An idiot admires complexity; a genius admires simplicity"')
        print("-Terry Davis (1969-2018)")
