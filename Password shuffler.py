#!/usr/bin/env python
# coding: utf-8

# In[12]:


import string
import random

#collecting needed characers form module "string"
letters = string.ascii_letters
digits = string.digits

#creating empty lists for letters and digits ready to fill in
l_letters = []
l_digits = []


#filling the lists of letters and digits
start1 = 0
start2 = 0

for i in letters:
    l_letters.append(letters[start1])
    start1 += 1

for j in digits:
    l_digits.append(digits[start2])
    start2 +=1

print("This is the list of possible letters for password:\n",l_letters,"\n")
print("This is the list of possible digits for password:\n",l_digits)




#___________________________________________________________________________________________#
###START!###

def random_pass(size_letters,size_digits):
       
    #creating ready to fill list for password's characers
    password = []
    
    #requirement for the password: at lest 8 characters (at least 5 letters ans at least 3 digits)
    while int(size_letters)+int(size_digits) < 8:
        print("The pasword must contain from at least 8 characters (at least 5 letters and at least 3 digits).")
        
        #getting amount of letters
        size_letters = input("Enter the number bigger than 5:\n")
        size_letters = int(size_letters)
        
        #getting amount of digits
        size_digits = input("Enter the number bigger than 3:\n")
        size_digits = int(size_digits)
        
        
        
    #__________________________________________#   
    #Password needs to have 2 uppercase letters#
    
    
    #collecting lowercase letters
    for n in range(int(size_letters-2)):
        random_smallletters = random.choice(l_letters)
        password.append(random_smallletters.lower())
    
    #collecting 2 uppercase letters that do not occur withinh lowercase letters
    for n in range(2):
        random_bigletters = random.choice(l_letters)
        if random_bigletters not in password:
            password.append(random_bigletters.upper())
        else:
            random_bigletters = random.choice(l_letters)
    
    #collecting digits
    for n in range(size_digits):
        random_2 = random.choice(l_digits)
        password.append(random_2)
    
    #shufflig list of collected letters and digits
    random.shuffle(password)
    #changing password from list to string
    password = "".join(password)
    
    return password


print("\nThis is you random password:\n"+random_pass(15,15))


# In[ ]:




