!!!OUTDATED!!!

#SIMPL Type 3 Interpreter & Prompt
#Copyright (c) 2025, Alexander Peat
#Author: Alexander Peat
#Program written between: 19/08/2025 - Present

#What's different from Type 2?
#SIMPL Type 3 has arrays, subroutines, and supports floating point numbers.
#Syntax is not backwards compatible

#SIMPL Type 3 will also use a new prompt that is built completely from the ground up with support for subroutines

#NOTES FOR FUTURE:
#Add to the Syntax Notes section examples of float operations for every applicable command

#subroutines are stored in their own list(s) which are in turn stored in a large 'subroutine directory' list that gets printed out with the 'sublist' command
#they can be modified with 

#---Syntax Notes---

#Always write code in increments of ten

#Print Syntax:
#'P' for 'Print'
#P;S;Hello, World; <- prints a string called 'Hello, World'
#P;V;variable_one; <- prints the contents of a variable called 'variable_one'

#Input Syntax:
#'U' for 'inpUt'
#U;N;number_variable;Enter a number: ; <- outputs the prompt 'Enter a number: ' and stores the response in a variable called 'number_variable'
#U;S;string_variable;Enter a string: ; <- outputs the prompt 'Enter a string: ' and stores the response in a variable called 'string_variable'
#U;F;float_variable;Enter a float number: ; <- outputs the prompt 'Enter a float number: ' and stores the response in a variable called 'float_number'

#Initialisation Syntax:
#'I' for 'Initialise'
#I;N;number_variable;0; <- initialises a variable called 'number_variable' and assigns it the value of 0
#I;S;string_variable;Hello, World; <- initialises a variable called 'string-variable' and assigns it the value of 'Hello, World'
#I;F;float_variable;6.9; <- initialises a variable called 'float_variable' and assigns it the value '6.9'

#Mathematical Syntax:
#'M' for 'Mathematics'
#M;answer_variable;V;operand1;+;V;operand2; <- adds the two variable ('operand1' and 'operand2') together and sets the value to the variable 'answer_variable'
#M;answer_variable;V;answer_variable;+;V;operand2; <- the variable set to the result of the operands can also be an operand
#M;answer_variable;V;operand1;(+/-/*///**);V;operand2; <- the operator can be either '+', '-', '*', '/', or '**'
#M;answer_variable;N;420;+;F;6.9; <- the operands can also be numbers or floats, but whether or not the operand is a variable, number, or float, it has to be specified with 'V', 'N', or 'F', respectively
#Also note that whilst the two operand variables have to have been initialised before the 'M'-line, the answer variable does not

#Go to Syntax:
#'G' for 'Go to'
#G;10; <- sets the line_counter variable to 10 thus executing the tenth line of code
#G;goto_variable; <- variables can also be used to specify the desired line number

#Conditional Syntax:
#'W' for 'When' as in 'When condition, then...'
#W;V;variable1;=;V;variable2;10; <- checks if variable1 is equal to variable2 and if it is, then it sets the line number to 10
#W;V;variable1;!;V;variable2;5; <- checks if variable1 is not equal to variable2 and if so, it then sets the line number to 5
#W;V;variable1;(=/!/</>);V;variable2;15; <- the logical operator can be either '=', '!', '<', or '>'
#W;V;variable_one;=;variable_two;V;goto_variable; <- the goto number can also be a variable
#W;N;69;=;F;6.9;20; <- logical operands can also be numbers and floats; they just ave to be specified with 'N' and 'F', respectively

#String Concatenation Syntax:
#'C' for 'Concatenation'
#C;concatenated_string;V;variable_one;V;variable_two; <- concatenates the two variables, 'variable_one' and 'variable_two' together and sets the value to the variable 'concatenated_string'
#C;concatenated_string;S;Hello, ;S;World; <- non variable strings can also be concatenated
#C;concatenated_string;S;Hello, ;V;variable_world; <- non variable strings and variables can be concatenated, too

#Comment Syntax:
#-This is a comment <- comments are written on their own lines and all start with '-' to tell the interpreter to ignore them

#Time Syntax:
#'T' for 'Time'
#T;S;time_variable; <- assigns the variable 'time_variable' a string with the format xx:yy dd/mm/yyyy UTC
#T;N;time_variable; <- assigns the variable 'time_variable' a number representing the Unix Epoch

#Number <--> String Conversion Syntax:
#'B' for 'Become' as in 'Become a string' or 'Become a number'
#B;S;variable_in_question; <- changes the variable 'variable_in_question' from a number to a string
#B;N;variable_in_question; <- changes the variable 'variable_in_question' from a number to a number

#Splicing Syntax:
#'L' for 'spLicing'
#I;S;slice_that_variable;Hello, World!;
#L;slice_that_variable;0;5; <- sets the variable 'slice_that_variable' to equal only the characters from the start to, but not including, the fifth place
#P;V;slice_that_variable; <- prints 'Hello'

#Re-initialisation Syntax:
#'R' for 'Re-initialise'
#R;copied_var;N;original_var; <- sets the variable 'copied_var' to have the same value as the variable 'original_var'
#R;copied_var;S;original_var; <- sets the variable 'copied_var' to have the same value as the string variable 'original_var'

#Sleeping Syntax:
#'S' for 'Sleep'
#S;10; <- that pauses (i.e. sleeps) the program for 10 seconds
#S;pause_time; <- variables can also be used to specify the desired pause length

#List Syntax:
#'A' for 'Array'... sort of, technically they're lists
#Initialising Lists:-
#A;list1;I;V;value1;V;value2;V;value3;V;value4;E; <- initialises a list called 'list1' with the values 1-4; the 'E' at the end signifies that the user is done with adding values to it
#A;list2;I;V;value1;N;69;F;69.0;S;Hello, World;E; <- the values initialised don't have to be variables
#Appending Lists:-
#A;list1;A;V;value5; <- appends value5 to the array
#A;list1;A;N;69;            }
#A;list1;A;S;Hello, World;  }-- non-variables can be appended, too
#A;list1;A;F;6.9;           }
#Popping Lists:-
#A;list1;P;5; <- removes the value with the index 5 from the list
#A;list1;P;value_to_pop_with; <- variables representing the index can also be used
#Indexing Lists
#'N' for 'iNdexing'
#A;list1;N;5;storing_variable; <- sets the value in list1with the index of 5 to the variable called 'storing_variable'

#Ending Programs:
#the last line of any program should always be 'END'
