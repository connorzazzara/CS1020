choices = ["rock","paper","scissors"]

import random
p = input(" player 1 enter choice: ")

print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")

c = input(" player 2 enter choice: ")
if p not in choices:
    print('please choose rock, paper, or scissors')
    p = input("enter choice: ")
if c not in choices:
      c = random.choice(choices)

print('Player 1:', p)
print('Player 2:', c)

if c==p:
    print("tie")

elif c=="rock":
    if p=="paper":
        print("Player 1 win")
    if p=="scissors":
         print ("Player 2 win")

elif c=="paper" : 
    if p=="rock":
      print ("Player 1 win")
      if p=="scissors":
         print ("Player 2 win")


elif c=="scissors" :
    if p =="paper":
         print ("Player 1 win")
         if p =="rock":
             print ("player 2 win")
