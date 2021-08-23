import random
words=["calculate,dog,request","computer","rest","software"]
name=input("enter your name: ")
print("let's play with words",name)
word=words.random()
guesses=''
print("guess the word")
turns=12
while turns>0:
    failed=0
    for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed+=1
        if failed==0:
            print("you win")
            print("the word is",i)
            break
        guess=input("enter your guess")
        guesses+=guess
        if guess not in i:
            turns-=1
            print("wrong")
            print("you have",+ turns,"more guesses")
            if turns==0:
               print("you loose")

print("hope you enjoyed playing")
