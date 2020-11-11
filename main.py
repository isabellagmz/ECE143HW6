# Isabella Gomez A15305555
# ECE143 HW6

from multinomial import multinomial_sample
from chunkify import split_by_n
from encrypted import encrypt_message
from encrypted import decrypt_message
class Homework6:
    def __init__(self):
        pass

if __name__ == '__main__':
    my_Homework6 = Homework6()
    fname = "/Users/isabellagomez/Documents/ECE143/metamorphosis.txt"
    # print(multinomial_sample(10,[1/3,1/3,1/3],k=10))
    #print(split_by_n("/Users/isabellagomez/Documents/ECE143/metamorphosis.txt", 3))
    message ="let us not say we met late at the night about the secret"
    print(encrypt_message('let us not say we met late at the night about the secret vermin bedding familiar proper',fname))
    print(decrypt_message([(1394, 2), (1775, 4), (613, 5), (940, 10), (1741, 1), (1192, 5), (732, 5), (849, 2), (207, 10), (382, 2), (1977, 2), (271, 1), (850, 3), (48, 9), (51, 3), (574, 3), (284, 6)], fname))
