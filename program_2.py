# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------
#Braden Phetsarath
#9/30
#math quiz 
import random
def rng():
    num1 = random.randint(0, 999)
    num2 = random.randint(0, 999)
    return num1, num2

def math_quiz():
    num1, num2 = rng()
    print(f"The two random numbers are", num1 , num2)
    correct_answer = num1 + num2
    answer = int(input("Enter the sum:"))
    if answer == correct_answer:
        print("Correct")
    else:
        print("Incorrect")
        print(correct_answer)

math_quiz()
# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect a message showing the correct answer should be displayed.
# The program must use a function that accomplishes part of the needed tasks.
