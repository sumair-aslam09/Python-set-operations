import random
import string
dict={"val":1000000}

def random1(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


with open("L1.txt","w") as mail:
    for i in range(dict["val"]):
            mail.write(random1(8)+ "@gmail.com"+ '\n')

with open("L2.txt","w") as mail:
    for i in range(dict["val"]):
            mail.write(random1(8)+ "@gmail.com"+ '\n')

