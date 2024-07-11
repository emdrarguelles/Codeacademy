# importing random numbers
import random

print("Welcome to the Magic 8-Ball!\nso...")
# assign a name
name = input("     what is your name?")

# assign question variable
question = input("     What do you want to know?")

# store answers here
answer = ""

# store random numbers here
random_number = random.randint(1, 11)  # randomized from 1 to 11

# print random 1-11 number
# print (random_number) -- removed since this now works

# if statement for answer start here:
if random_number == 1:
    answer = "Yes - definitely"

elif random_number == 2:
    answer = "It is decidedly so"

elif random_number == 3:
    answer = "Without a doubt"

elif random_number == 4:
    answer = "Reply hazy, try again"

elif random_number == 5:
    answer = "Ask again later"

elif random_number == 6:
    answer = "Better not tell you now"

elif random_number == 7:
    answer = "My sources say no"

elif random_number == 8:
    answer = "Outlook not so good"

elif random_number == 9:
    answer = "Very doubtful"

elif random_number == 10:
    answer = "Not even in the realm of possible"

elif random_number == 11:
    answer = "You don't even need to ask"

else:
    print("Error")

# if statement for name and question start here:
if name == "":
    if question == "":
        question = input("\nOkay no name. You forgot to ask a question. What is it?")
        print("\nQuestion: " + question)
        print("Magic Ball's answer: " + answer)
        print("\nAsk your next question...")

    else:
        print("Question: " + question)
        print("Magic Ball's answer: " + answer)
    
else:
    if question == "":
        question = input("\nCome on " + name + ", ask your question. What is it?")
        print("\nQuestion: " + question)
        print("Magic Ball's answer: " + answer)
        print("\nAsk your next question...")
 
    else:
        print("\n" + name + " asks: " + question)
        print("Magic Ball's answer: " + answer)
        print("\nStart over...")
