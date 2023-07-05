""" Write a function that takes in a list of strings. Return the longest string in the list."""
def find_longest_string(strings_list):

    strings_set = set(strings_list)
    longest_str = ""  #keeps track of the longest
    for str in strings_set:
        if len(str) > len(longest_str):
            longest_str == str
    return longest_st



"""Write a function that takes in an item and a list. Return the number of times the given item appears in the list."""

def times_item_in_list(item_list, item):
    times_seen = 0 
    for thing in item_list:
        if thing == item:
            times_seen +=1
    return times_seen

"""Write a function that takes in a list of numbers. It should find all even numbers and return a list of their indices. For example
[2, 4, 1] => [0, 1]
[] => []
[1] => []"""

def even_nums_and_indices(num_list):
    list_of_indices = []
    for index, num in enumerate(num_list):
        if num % 2 == 0:
            list_of_indices.append(index)
    return list_of_indices


"""Write a function that takes in a string and returns a string with all vowels replaced with *"""
def replace_vowels(str):
    vowels = "aeiou"
    return_str = ""
    for letter in str:
        if letter in vowels:
            return_str += "*"
        else:
            return_str += letter
    return return_str


"""Write a function that takes in a string and returns all unique characters in the string"""
#apple --> a p l e 
#mississipi  --> m i s p
def unique_chararcters(str):
    
    unique_chars = set(str)
    return list(unique_chars)
"""using a dictionary and a list. Dictionary holds k:v pairs of chars:count. Add to the dictionary every character and a count of 1 if it is not in char append unique chars"""
def unique_chars_in_str(str):
    char_count = {}
    unique_chars = [] 
    for char in str:
        if char not in char_count:
            char_count[char] = 1
            unique_chars.append(char)
    return unique_chars

"""Write a function that takes in a string and returns a character count dictionary. For example,
"catty" => {"c": 1, "a": 1, "t": 2, "y": 1}"""

def char_count_dictionary(str):
    char_count = {}
    for letter in string:
        if letter in char_count:
            char_count[char] += 1
        else:
            char_count = 1 
    return char_count



"""Write a function that takes in a string and returns True if it is a palindrome and False otherwise. A palindrome is a word that is spelled the same backwards and forwards.
You cannot use the reverse or reversed functions.
"noon" => True
"racecar" => True
"a" => True
"math" => False
"" => True
Treat spaces and uppercase letters normally:
"Racecar" => False"""

def is_palindrome(str):
    
    for i in str:
        if str[i] == str [-i]:
            return True 