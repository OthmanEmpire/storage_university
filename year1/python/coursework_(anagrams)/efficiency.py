##### Student name: Othman ALI KHAN
##### Student ID: 200 684 094

### This program has a series of functions/procedures that produce anagrams.
### The final procedure/function of the program reads from a text file, extracts
### all student names and then produces a one word and two word anagrams.



# This function takes two strings and checks whether both strings
# have exactly the same letters in them (e.g. pat, tap ---> return True)
def anagram(str1, str2):

    list1 = sorted(str1.lower().replace(' ', ''))
    list2 = sorted(str2.lower().replace(' ', ''))
    
    if(list1 == list2):
        return True
    else:
        return False


    
# This procedure has some examples of strings which are passed into
# the function 'anagram' in order to test the functionality of 'anagram'
def test_anagram():

    positive_examples = [["Tom Marvolo Riddle", "I am Lord Voldemort"],
                         ["Death", "Hated"],
                         ["Wolf", "Flow"]]


        
    negative_examples = [["Work", "Reward"],
                         ["Solitude", "Insanity"],
                         ["Hope", "Despair"]]

    print("{:#^30}\n".format("POSITIVE CASES"))
    print_test_anagram_output(positive_examples)


    print("\n{:#^30}\n".format("NEGATIVE CASES"))
    print_test_anagram_output(negative_examples)



# This procedure is used in 'test_anagram' to be able print out
# it's output in easy to read format
def print_test_anagram_output(type_examples):


    for example in type_examples:

        test = anagram(*example)
        
        print("Pair of strings to be tested:", example)
        print("Are the strings anagrams?", anagram(*example))
        print()



# This function reads from a a text file and retrieves words from that file
# without a trailing newline
def get_dictionary_word_list():

    try:
        with open("dictionary.txt", 'r') as file:

            unformatted_contents = file.readlines()
            
            dict_contents = [line.strip() for line in unformatted_contents] 
            return dict_contents


    except IOError as err:
        print(err)
        exit()



# This procedure calls 'get_dictionary_word_list' then prints out the total
# number of words followed by the first 10 words of the list returned
def test_get_dictionary_word_list():

    dict_contents = get_dictionary_word_list()

    total_words = len(dict_contents)
    print("Number of words in the dictionary read: {}".format(total_words))
    print()

    print("The first 10 words are:")
    for word_index in range(10):
        
        print(dict_contents[word_index])



# This function searches through str_list to find an anagrams of str1
# then returns the list of found anagrams within str_list
def find_anagrams_in_word_list(str1, str_list):

    anagram_list = []

    for str2 in str_list:

        if(anagram(str1, str2)):
            anagram_list.append(str2)

    return anagram_list



# This function finds anagrams of the inputted string against the
# list of words in a file (in this case, "dictionary.txt")
def find_anagrams(string):

    dict_contents = get_dictionary_word_list()
        
    anagram_list = find_anagrams_in_word_list(string, dict_contents)
    
    return anagram_list



# This procedure calls the function "find_anagram" and inputs 10 strings
# which some will have several anagrams 
def test_find_anagrams():

    string_list = ["Mania", "Insane", "Madness",
                   "Deprived", "Sleep", "Tired",
                   "Torment", "Suffer", "Pain",
                   "Python", "Joy", "Work"]

    for string in string_list:
        
        anagram_list = find_anagrams(string)

        print(("The anagrams of '{}' in the file 'dictionary.txt' are:\n{}\n"
              .format(string, anagram_list)))


        
# This function returns a boolean type true if str1 has every letter in str2
# even though str1 and str2 are of different lengths, otherwise it returns false
def partial_anagram(str1, str2):

    if(len(str1) > len(str2)):      # Condition due to function specification
        return False

    for letter1 in str1:
        for letter2 in str2:

            if(letter1 == letter2):
                str1 = str1.replace(letter1, '', 1)
                str2 = str2.replace(letter1, '', 1)
                break


    if(str1 == ''):
        return True
    else:
        return False



# This function uses the "partial_anagram" function against a list of strings
# and then returns a list of partial anagrams
def find_partial_anagrams_in_word_list(str1, str_list):

    partial_anagram_list = []

    for str2 in str_list:

        if(partial_anagram(str2, str1.lower())):
            partial_anagram_list.append(str2)

    return partial_anagram_list



# This procedure calls "find_partial_anagrams_in_word_list" for 5
# strings against a list of words obtained from "dictionary.txt"
# and then prints out the relevant partial anagrams in a neat format
def test_find_partial_anagrams_in_word_list():


    string_list = ["brandon", "human", "alien", "light", "ilumin"]
    dict_contents = get_dictionary_word_list()

    for string in string_list:
        
        partial_anagrams_list = (find_partial_anagrams_in_word_list(string,
                                                              dict_contents))
        
        print(("The word '{}' has the {} anagrams:\n\n{}\n\n{:#<50}\n"
              .format(string, len(partial_anagrams_list),
                      partial_anagrams_list, '')))



# This function removes all the letters that occur in str1 from str2
# and then returns str2
def remove_letters(str1, str2):

    list1 = list(str1.lower())
    original_length = len(str2)

    for element1 in list1:
       str2 = str2.replace(element1, '', 1)


    if(original_length == len(str2)):
        print("Warning: no letters have been replaced for: {}\n".format(str2))
    
    return str2



# This procedure calls "remove_letters" on several strings and prints out
# the results
def test_remove_letters():

    str1 = ["abc", "atom", "distort", "H2O"]
    str2 = ["abcefg", "atmosphere", "orthopedist", "Water"]


    for string_index in range(len(str1)):
    
        modified_str2 = remove_letters(str1[string_index], str2[string_index])

        print(("str2: {}  ||  str1: {} \nmodified_str2: {}\n\n"
              .format(str2[string_index], str1[string_index], modified_str2)))



# This procedure finds a two word anagram from str1 against a list of strings
# e.g. an output of str1 = "Brandon" would be "and born".
# the function then returns a two word anagrams list
def find_two_word_anagrams_in_word_list(str1, str_list):

    two_word_anagrams_list = []
    
    partial_anagrams_list = find_partial_anagrams_in_word_list(str1, str_list)


    for partial_anagram1 in partial_anagrams_list:
        for partial_anagram2 in partial_anagrams_list:

            full_word = partial_anagram1 + partial_anagram2

            if(anagram(full_word, str1)):
                two_word_anagrams_list.append(partial_anagram1 + " " +
                                            partial_anagram2)

    return two_word_anagrams_list



# This procedure calls "find_two_word_anagrams_in_word_list" for 9 different
# strings and then prints out the list of two word anagrams
def test_find_two_word_anagrams():

    string_list = ["Brandon",
                   "End", "Of", "Rope",
                   "Phoenix", "is", "Reborn",
                   "Tragedy", "Happen"]

    dict_contents = get_dictionary_word_list()

    for string in string_list:
        
        two_word_anagrams_list = (find_two_word_anagrams_in_word_list
                                 (string, dict_contents))

        (print("The available {} two word anagrams for '{}' are:\n{}\n\n"
              .format(len(two_word_anagrams_list), string,
                      two_word_anagrams_list)))
        print("{:#<80}\n".format(''))



# This procedure extracts all the full names available in the file
# "students.txt" and stores it in a list which it then returns
def extract_full_names_from_file():

    full_name_list = []
    last_name = []

    try:
        with open("students.txt", 'r') as file:

            for content in file:
                
                content = content.split()
                content.pop(0)  # Removes the student ID number


                for index in range(len(content)):
                    
                    if(content[index] == 'RE'):     # RE is always after a
                                                    # student's name
                        full_name_list.append([])

                        for name_index in range(index):
                            full_name_list[-1].append(content[name_index])
                            
                        break

            return full_name_list

            
    except IOError as err:
        print(err)
        exit()



# This function categorizes names into first and last names and then returns
# a categorized list. Note: this function will bundle up multiple last names
# belonging to a single person as a single last name.
def sort_full_name_list(full_name_list):

    multiple_last_name_list = []
    first_name_list = []
    last_name_list = []

    
    for full_name in full_name_list:

        multiple_last_name_list.append([])  
        for name in full_name:

            if(name.isupper()):
                multiple_last_name_list[-1].append(name.strip(','))
            else:
                first_name_list.append(name)    # The first name will always be
                break                           # the name directly following
                                                # after the last name
                                                
    for name_index in range(len(full_name_list)):     

        last_name_list.append(' '.join(multiple_last_name_list[name_index]))

        first_and_last_names_list = list(zip(first_name_list, last_name_list))


    return first_and_last_names_list



# This procedure generates one word and two word anagrams from a list of
# first and last names combined strings
def anagram_full_name(first_and_last_names_list):

    dict_contents = get_dictionary_word_list()

    for name in first_and_last_names_list:
      
        name_string = (''.join(name).replace('-', '').replace(' ', '')
                      .replace("'", '').lower())

        print("Full name: {}\nFirst name: {} || Last name: {}"
             .format(' '.join(name), name[0], name[1].capitalize()))

        print("Joined name string: {}".format(name_string))
        print()
        
        one_word_anagram_list = find_anagrams(name_string)
        two_word_anagram_list = (find_two_word_anagrams_in_word_list
                                (name_string, dict_contents))

        print("There are {} one word anagrams:\n{}\n"
              .format(len(one_word_anagram_list), one_word_anagram_list))
        print("There are {} two word anagrams:\n{}\n\n"
              .format(len(two_word_anagram_list), two_word_anagram_list))
        print("{:#<80}\n".format(''))



# This procedure tests the "anagram_party" procedure to ensure it is working
# as intended. Note: for the first name, it will take about 3-5 minutes to
# generate... Talk about inefficiency at it's finest.
def test_anagram_full_name():

    try:

        full_name_list = extract_full_names_from_file()

        first_and_last_names_list = sort_full_name_list(full_name_list)

        anagram_full_name(first_and_last_names_list)


    except Exception as e1:
        print("Unexcepted Error:", e1)

        try:
            import time

            with open("log.txt", "a") as log_file:

                local_time = time.asctime(time.localtime(time.time()))
                log_file.write("{} Unexpected Error: {}".format(local_time, e1))

        except IOError as e2:
            print("Error: Could not generate/write a log file for the error!")

        except ImportError as e3:
            print("Error: Could not import time module for the error log!")
            
                               

test_anagram_full_name()
