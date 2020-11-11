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
    print(encrypt_message(message,fname))
    print(decrypt_message(encrypt_message(message,fname), fname))
