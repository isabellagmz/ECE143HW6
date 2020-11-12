# Isabella Gomez A15305555
# ECE143 HW6

import os
def split_by_n(fname, n=3):
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

    # get size of sub-files
    file_size = os.path.getsize(fname)  # check size of original file
    nth_file_size = int(file_size / n)  # approximate size of each sub-file

    file_index = 0  # index of each file in the file name
    line_size = 0  # increment the size of the string giving in each line
    label = '{}_00{}.txt'.format(fname, file_index)

    new_file = open(label, 'wt')

    i = 0
    with open(fname, 'rt') as original_file:
        # copy each line until it reaches the max size allowed
        for line in original_file:
            line_size = line_size + len(line) # update line_size with size of new line
            if line_size >= nth_file_size:
                new_file.close() # close the new_file

                # update index and file label
                file_index = file_index + 1
                label = '{}_00{}.txt'.format(fname, file_index)

                # start a new file
                new_file = open(label, 'wt')
                line_size = len(line)
                i = i + 1

                if i == n - 1:
                    nth_file_size = nth_file_size ** 2

            new_file.write(line) # add the line to new_file

    # close the files
    new_file.close()
    original_file.close()
