##############################
########## PART TWO ##########
##############################

import random

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

# Compares word to word if they have the same letters
# Returns : list of common letters at the same index (arr)
def compare_two_words(word1, word2):
    common_letters = []
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            common_letters.append(word1[i])
    return common_letters

# compares all the words in the list to a given word
# Arguments : word to compare to (str) and list of words (arr)
# returns : the nearest word to the given word (str)
def compare_word_to_list(word, list_of_words):
    nearest_word = ""
    nearest_word_common_letters = []
    for word_to_compare in list_of_words:
        # the word which we compare is in the list, you don't compare it to itself!
        if word != word_to_compare:
            common_letters = compare_two_words(word, word_to_compare)
            if nearest_word_common_letters < common_letters:
                nearest_word = word_to_compare
                nearest_word_common_letters = common_letters
    return nearest_word


# Variables 
id_list = get_words("checksum.txt", "\n")

# the program assumes that all ID are the same length
number_of_characters = len(id_list[0])
# generate random strings as a starting point
guess_id_one = ''.join(random.choice('0123456789ABCDEF') for i in range(number_of_characters))
guess_id_two = ''.join(random.choice('0123456789ABCDEF') for i in range(number_of_characters))

# __main__
for id in id_list:
    nearest_id = compare_word_to_list(id, id_list)
    same_letters_new_guess = compare_two_words(id, nearest_id)
    same_letters_old_guess = compare_two_words(guess_id_one, guess_id_two)
    if same_letters_new_guess > same_letters_old_guess:
        guess_id_one = id
        guess_id_two = nearest_id
    # print("{} - {}".format(guess_word_one, guess_word_two))
    
result_same_letters = compare_two_words(guess_id_one, guess_id_two)
# Result (yeah, I had fun front ending this)
print("\n============================================================")
print("======== You've got a nice robot with both packages ========")
print("============================================================")

print("\n   --- Box n°1 to get: {} ---\n   --- Box n°2 to get: {} ---\n".format(guess_id_one.upper(), guess_id_two.upper()))
print("                         __")
print("                 _(\    |@@|")
print("                (__/\__ \--/ __")
print("                   \___|----|  |   __")
print("                       \ }{ /\ )_ / _\\")
print("                       /\__/\ \__O (__")
print("                      (--/\--)    \__/")
print("                      _)(  )(_")
print("                     `---''---`")
print("\n               --- Common letters: ---\n{}\n\n        --- Which makes {} / {} letters ---".format(result_same_letters, len(result_same_letters), number_of_characters))
print("\n============================================================")
