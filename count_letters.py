def count_letters(string_of_letters):
    """
    Finds the amount of each letter in a string, counting upper- and lower-case letters as the same letter.
        
    Arguments: 
        string_of_letters (string): The string of which the number of each type of letter will be found.
        
    Returns:
        number_of_letters (dictionary): A dictionary containing all of the letters in the original string and the amounts of each.
    """
    number_of_letters = {}
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in string_of_letters:
        if i.upper() in alphabet:
            if i.upper() in number_of_letters:
                number_of_letters[i.upper()] += 1
            else:
                number_of_letters[i.upper()] = 1
    return number_of_letters
  
#str_of_letters = "one two three four five six seven eight nine ten"
#print(count_letters(str_of_letters))