# Isabella Gomez A15305555
# ECE143 HW6

import os
import sys
def split_by_n(fname,n=3):
    '''
    This function will take in a file then it will divide it into n chunks and
    store each individual chunk into a separate file. The program should not go
    over the file more than once. It should store the lines as they come in and
    there should be no truncated lines in any file.

    :param fname: name of the downloaded file
    :param n: number of chunks to divide the file into
    :return:
    '''

    # check that n is an int >0 and fname a string
    assert type(n) == int
    assert n > 0
    assert type(fname) == str

    # check if file exists
    assert os.path.isfile(fname)

    # open the file
    original_file = open(fname, 'r')

    # get size of sub-files
    file_size = os.path.getsize(fname) # check size of original file
    nth_file_size = int(file_size / n) # approximate size of each sub-file
    # print(nth_file_size)
    file_index = 0

    # number of files we need
    for new_file in range(n):
        sub_file_name = fname + str(file_index) + '.txt'
        sub_files = open(sub_file_name, 'wt')

        line_size = 0
        # put lines into another file until it reaches limit
        for i, lines in enumerate(original_file):
            line_size = line_size + sys.getsizeof(lines)
            sub_files.write(lines)
            if line_size >= nth_file_size and file_index != n-1:
                break
        # print(os.path.getsize(sub_file_name))
        file_index = file_index + 1  # increase index
        sub_files.close() # close sub-file

    # close the file
    original_file.close()

    return
