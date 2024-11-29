import random
comp=random.randrange(1,100)
user=input("enter your name : ")
user_inp=int(input('enter any number between 1 to 100 : '))

score=0

while user_inp!=comp:
    if user_inp <= 0 :
        print("please type a positive number ")
        quit()
    else :
        if user_inp>comp:
            print("lower number please")
            user_inp=int(input("enter number : "))
        elif user_inp<comp:
            print("greater number please")
            user_inp=int(input("enter number : "))
        else :
            break
        score += 1
print(f"{user.capitalize()} guessed it in {score} attempts")
    


