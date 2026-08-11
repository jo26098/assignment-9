def count_letters(string_of_letters):
    """
    Finds the amount of each letter in a string, counting upper- and lower-case letters as the same letter.
        
    Arguments: 
        string_of_letters (string): The string of which the number of each type of letter will be found.
        
    Returns:
        number_of_letters (dictionary): A dictionary containing all of the letters in the original string and the amounts of each.
    """
    number_of_letters = {}
    for i in string_of_letters:
        if i in number_of_letters:
            number_of_letters[i] += 1
        else:
            number_of_letters[i] = 1
    return number_of_letters

#str_of_letters = "one two three four five six seven eight nine ten"
#print(count_letter(str_of_letters))