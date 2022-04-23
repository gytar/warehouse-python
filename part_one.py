##############################
########## PART ONE ##########
##############################

# Functions 

# gets the words from a file and put them in an array
# filepath : path to the file (str)
# separator : separator between words (str)
# returns : list of words (arr)
def get_words(filepath, separator):
    file = open(filepath, "r")
    file_content = file.read()
    id_list = file_content.split(separator)
    file.close()
    return id_list

# For both function, the letters that appears twice or thrice are returned. 
# Takes the ID as argument.
def letters_appears_twice(id):
    letters_that_appears_twice = []
    for letter in id:
        if id.count(letter) == 2 and letter not in letters_that_appears_twice:
            letters_that_appears_twice.append(letter)
    return letters_that_appears_twice

def letters_appears_thrice(id):
    letters_that_appears_thrice = []
    for letter in id :
        if id.count(letter) == 3 and letter not in letters_that_appears_thrice:
            letters_that_appears_thrice.append(letter)
    return letters_that_appears_thrice


# Vars
id_list = get_words("checksum.txt", "\n")
checksums = 0
boxes_with_two_same_letters = 0
boxes_with_three_same_letters = 0

# __main__
print("Length of ID list: " + str(len(id_list)))

for id in id_list:
    list_letters_twice = letters_appears_twice(id)
    list_letters_thrice = letters_appears_thrice(id)
    
    # If you want to print some details: 
    
    # prints all IDs with the numbers of letters that appears twice and thrice
    # print("{}: {} {}".format(id, len(list_letters_twice), len(list_letters_thrice)))
    # prints all IDs with the letters that appears twice and thrice
    # print("{}: {} {}".format(id, list_letters_twice, list_letters_thrice))
    
    if len(list_letters_twice) > 0:
        boxes_with_two_same_letters += 1
    if len(list_letters_thrice) > 0:
        boxes_with_three_same_letters += 1

checksums = boxes_with_two_same_letters * boxes_with_three_same_letters

# prints the checksums and the number of boxes with two same letters and three same letters
print("Checksums = {} - ({} * {})".format(checksums, boxes_with_two_same_letters, boxes_with_three_same_letters))
    


