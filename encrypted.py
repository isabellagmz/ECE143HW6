# Isabella Gomez A15305555
# ECE143 HW6

import os
from random import randint
def encrypt_message(message,fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple.

    :param message: message to encrypt
    :param fname: filename for source text
    :return: list of 2-tuples
    '''

    # check that filename and message are text
    assert type(fname) == str
    assert type(message) == str

    # check that file exists
    assert os.path.isfile(fname)

    # open the file
    file = open(fname, 'r')

    # store the lines of the text in a list
    list_of_lines = []
    for i, lines in enumerate(file):
        list_of_lines.append(lines)

    list_of_words = []
    for i in range(len(list_of_lines)):
        word = list_of_lines[i].split()
        # remove punctuation and make lowercase
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for j in range(len(word)):
            word[j] = word[j].lower()
            for char in word[j]:
                if char in punctuations:
                    word[j] = word[j].replace(char, "")
        list_of_words.append(word)

    # make a list of words from the message
    message_list = []
    for word in message.split():
        message_list.append(word)

    final_list = []
    temp = []
    # check if the word is in the line
    for k in range(len(message_list)):
        for i in range(len(list_of_words)):
            for j in range(len(list_of_words[i])):
                if message_list[k] == list_of_words[i][j]:
                    temp.append((i+1,j+1))
        # generating a random number
        rand_int = randint(0,len(temp)-1)
        final_list.append(temp[rand_int])
        # empty temp
        temp = []

    # check that every element in final_list is unique
    assert len(final_list) == len(set(final_list))

    # close file
    file.close()

    return final_list

def decrypt_message(inlist,fname):
    '''
    Given `inlist`, which is a list of 2-tuples`fname` which is the
    name of a text file source for the codebook, return the encrypted message.

    :param inlist: inlist to decrypt
    :param fname: filename for source text
    :return: string decrypted message
    '''

    # check that filename is str and inlist is list
    assert type(fname) == str
    assert type(inlist) == list

    # check that every element in inlist is tuple
    for i in range(len(inlist)):
        assert type(inlist[i]) == tuple

    # check that file exists
    assert os.path.isfile(fname)

    # open the file
    file = open(fname, 'r')

    # store the lines of the text in a list
    list_of_lines = []
    for i, lines in enumerate(file):
        list_of_lines.append(lines)

    list_of_words = []
    for i in range(len(list_of_lines)):
        word = list_of_lines[i].split()
        # remove punctuation and make lowercase
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for j in range(len(word)):
            word[j] = word[j].lower()
            for char in word[j]:
                if char in punctuations:
                    word[j] = word[j].replace(char, "")
        list_of_words.append(word)


    # store the word in the return message
    final_string = ''
    for tup in range(len(inlist)):
        string = list_of_words[inlist[tup][0]-1][inlist[tup][1]-1]
        final_string = final_string + string + ' '

    #close file
    file.close()

    return final_string
