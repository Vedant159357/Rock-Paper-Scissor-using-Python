import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input  = int(input("choose your input : 0 for rock, 1 for paper and 2 for scissor"))

computer_list = [rock,paper,scissors]
computer_output = random.choice(computer_list)

if user_input == 0:
    print("you chose\n",rock)
    if computer_output == computer_list[0]:
        print("computer chose\n",computer_output)
        print("its a draw")

    elif computer_output == computer_list[1]:
        print("computer chose\n",computer_output)
        print("you lost")

    else:
        print("computer chose\n",computer_output)
        print("you won!!")

elif user_input == 1:
    print("you chose\n",paper)
    if computer_output == computer_list[0]:
        print("computer chose\n",computer_output)
        print("you won!!")

    elif computer_output == computer_list[1]:
        print("computer chose\n",computer_output)
        print("its a draw")

    else:
        print("computer chose\n",computer_output)
        print("you lost")

elif user_input == 2:
    print("you chose\n",scissors)
    if computer_output == computer_list[0]:
        print("computer chose\n",computer_output)
        print("you lost")

    elif computer_output == computer_list[1]:
        print("computer chose\n",computer_output)
        print("you won!!")

    else:
        print("computer chose\n",computer_output)
        print("its a draw")
else:
    print("invalid input")


