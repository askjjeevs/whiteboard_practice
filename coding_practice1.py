""" #1
Write a function that takes in a list of numbers and prints out each number that is less than 10.
"""
def print_num_less_than_10(num_list):
    for num in num_list:
        if num < 10:
            print(num)

""" #2 
Write a function that takes in a list of words. For each word, the function should print a tuple of (first_letter_of_word, word).
"""

def print_word_and_first_letter(word_list):
    for word in word_list:
        print(word[0], word)


""" #3 
Write a function that takes in a list of numbers. It should print every other number, starting with the number at index 0.
"""
def print_every_other_number(num_list):

    """using the range function"""
    for i in range(0, len(num_list), 2):
        print (num[i])
    
    for i in range(len(num_list)):
        if i % 2 == 0:
            print(num_list[i])
    """using list slicing"""
    for num in num_list[::2]:
        print (num)
    """enumerate"""
    for i, num in enumerate(num_list):
        if i % 2 ==0:
            print(num)


""" #4
Write a function that takes in a list and an item. It should return True if the list contains the item. Otherwise, return False.
"""
def is_item_in_list(item_list, item):

    for thing in item_list:
        if thing == item:
            return True


""" #5
Write a function that takes in a string and returns the length of that string. You cannot use the len function.
"""
def length_of_string(str):
    length = 0
    for letter in string:
        length +=1 
    return length

""" #6 
Write a function that takes in a sentence as a string. The function should print the length of each word in the sentence.
Your sentence will not contain any punctuation.
"""
def len_of_words_in_sentence(sentence):
    words_in_sentence = sentence.split()
    for word in words_in_sentence:
        print(len(word))

""" #7
Write a function that takes in a list of numbers and returns the largest number in the list. You cannot use the max function.
"""

def largest_num(num_list):
    largest_num = num_list[0]
    for num in num_list:
        if largest_num < num:
            largest_num == num
        print (largest_num)

        """using sorted function"""
def largest_num(num_list):
    sorted_num_list = sorted(num_list)
    return sorted_num_list[-1]


"""SIMPLE RANGE PRACTICE"""
# Generate a sequence of numbers from 0 to 4
def sequence_numbers(x):
    for num in range(x):
        print (num)
# Output: 0 1 2 3 4

# Generate a sequence of even numbers from 2 to 10
for num in range(2, 11, 2):
    print (num)
# Output: 2 4 6 8 10

# Convert a range to a list

#  numbers = list(range(1,6)):
#  print(numbers)
# # Output: [1, 2, 3, 4, 5]

#Write a function that takes in a number n and calculates the sum of all numbers from 1 to n
def sum_of_nums(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum 

#Write a function that takes in a list of numbers and returns a new list with the numbers in reverse order.
def reverse_nums(num_list):
    reversed = []
    for i in range(len(num_list)-1, -1, -1):
        reversed.append(i)
    return reversed 
