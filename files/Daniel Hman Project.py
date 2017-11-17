# -*- coding: utf-8 -*-

#importing the time module
import time

#welcoming the user
name = raw_input("What is your name young child? ")

print "Suhh, " + name, "Time to play the best game in your entire existence!"

print ""

#wait for 1 second
time.sleep(1)

print "Start guessing..."
time.sleep(0.5)

import random

#word bank
words =  ["Daniel", "Ugly", "seventeen", "snack", "computer", "watermelon", "gum", "eyes", "Africa", 
            "panther", "thanksgiving", "Idunno", "uhhhhhhhhh", "hangman",  ]
         
word_chosen = random.choice(words).lower()

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 7

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word_chosen:      

    # see if the character is in the players guess
        if char in guesses:  
 
    
        # print then out the character
            print char,
            
        else:
    
        # if not found, print a dash
            print "*",     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print "-----¯\_(ツ)_/¯You won!¯\_(ツ)_/¯----"  

    # exit the script
        break              

    print

    # makes you guess a letter
    guess = raw_input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # the letter is not in the word
    if guess not in word_chosen:  
 
     # subtracts a turn
        turns -= 1        
 
    # Wrong!!!!!!!
        print "The survey says....."
        time.sleep(3)
        print "Wrong!!!!!"
        time.sleep(1)    
 
    # the amount of turns left
        print "You have", + turns, 'more guesses' 
 
    # no more turns left
        if turns == 0:           
    
        # you done lost kid
            print "Ha better luck next time"  