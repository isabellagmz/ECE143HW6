import os


def split_by_n(fname, n=3):
    '''
    Description: splits the original value by n
    Parameter1: fname(str)
    Parameter2: n(integer)
    '''
    assert isinstance(fname, str)
    assert isinstance(n, int)
    assert n >= 1

    i = 0  # increment txt file
    x = 0  # keep track
    input_size = 0  # increment the size of the string giving in each line
    txt = '{}_000{}.txt'.format(fname, i)

    size = os.path.getsize(fname)
    size_3 = int(size / n)
    input_txt = open(txt, 'wt')
    with open(fname, 'rt') as outputfile:
        for line in outputfile:

            input_size += len(line)

            if input_size > size_3:

                input_txt.close()
                txt_size = os.path.getsize(txt)
                #print('txt_size: ',txt_size, 'folder', txt)
                i += 1
                txt = '{}_000{}.txt'.format(fname, i)
                input_txt = open(txt, 'wt')
                input_size = 0
            else:
                input_txt.write(line)

    input_txt.close()
    outputfile.close()
    txt_size = os.path.getsize(txt)

    print('txt_size: ', txt_size, 'folder', txt)

