#!/usr/bin/env python
# coding: utf-8

# In[2]:


#write a program to guess a number from a user




n=18
nog=1 #nog = number of guesses
print("Number of guesses is limited to only 9 times: ")
while (nog<=9):
    gn = int(input("Guess the number :\n")) #gn = guess number
    if gn<18:
        print("you entered a less number please enter a greater number.\n")
    elif gn>18:
        print("you entered a greater number please enter a smaller number.\n ")
    else:
        print("you won\n")
        print(nog,"no.of guesses you took to finish.")
        break
    print(9-nog,"no. of guesses left")
    nog = nog + 1

if(nog>9):
    print("Game Over")


# In[ ]:




