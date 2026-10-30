
import random
import math

def game():

    score=0

    operaters=["+","-","/","*"]

    while True:
        num1=random.randint(1,999)
        num2=random.randint(1,999)
        operator=random.choice(operaters)

        #Geeting answer from computer
        if operator =="+":
            answer=num1+num2
        elif operator =="-":
            answer=num1-num2
        elif operator == "/":
            answer=num1/num2
        elif operator=="*":
            answer=num1*num2

        #Asking answer to user
        print(f"\n{num1}{operator}{num2}:?")


        try:
            user_answer=float(input("Enter your ans: "))
        except ValueError:
            print("Invalid value!!")
            break


        #Cheak answer
        if math.isclose(user_answer,answer):
            print("Correct answer")
            score+=1
            print(f"Current score:{score}")
        else:
            print("Wrong answer")
            print("Coorect answer was:",answer)
            break
    return score
#Play game
print("Welcome to Math Quize game")

current_score=game()

try:
    with (open("Hi-score.txt","r")) as file:
        content=file.read().strip()

        if content=="":
            previos_score=0
        else:
            previos_score=int(content)
except FileNotFoundError:
    previos_score=0

if current_score>previos_score:
    print("\nCongratulations you brok the high-score")
    with (open("Hi-score.txt","w")) as  file:
        file.write(str(current_score))
    print(f"New high score is : {current_score}")

else:
    print("\nGame Over")
    print(f"Curret score is :{current_score}")
    print(f"Preiveas high score is:{previos_score}")