#Callum Brown
#10-10-14
#Python ascii task 2

character_numbers = int(input("Please enter the amount of characters that you would like in your password: "))

import random
import string

list1 = ""
while character_numbers > 0:
    a = random.choice(string.ascii_letters + string.digits)
    list1 = list1 + a
    character_numbers = character_numbers -1

print(list1)
    

                              

