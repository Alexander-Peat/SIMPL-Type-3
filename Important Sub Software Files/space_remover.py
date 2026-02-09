string = 'PRINT STR "HELLO WORLD, FROM THE COMPUTER!" TO THE SCREEN;'

def space_remover(line):
    line = list(line) #turn the line into a list

    new_list = [] #initialise the new_list list
    found_speechmark = False
    
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

    print(new_list) #diagnostic print

    new_string = "" #initialise an empty string as new_string
    
    for loop in range(len(new_list)): #loop for the length of the new_list
        new_string = new_string + new_list[loop]

    return new_string

print(space_remover(string))
