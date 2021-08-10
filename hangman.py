word="calculate,dog,request"
words=word.split(",")
for i in words:
    
    guesses=''
    print("guess the word")
    turns=12
    while turns>0:
        failed=0
        for char in i:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed+=1
        if failed==0:
            print("you win")
            print("the word is",i)
            break
        guess=input("enter character")
        guesses+=guess
        if guess not in i:
            turns-=1
            print("wrong")
            print("you have",+ turns,"more guesses")
            if turns==0:
               print("you loose")
        
        
#print(words)
##vowels="a","e","i","o","u"
##for i in word:
##    if vowels in i:
##        print(vowels)
##    else:
##        print("_")
