# Randomisation and Python Lists

# Mersenne Twister is a pseudorandom number generator (PRNG) that is widely used in programming languages and applications. 
# It was developed by Makoto Matsumoto and Takuji Nishimura in 1997. The Mersenne Twister is known for its high-quality random numbers, long period (2^19937-1), and efficient generation.
# The Mersenne Twister algorithm is based on a twisted generalized feedback shift register (TGFSR) and uses a large state vector to generate random numbers. 
# It is designed to produce high-quality random numbers with good statistical properties, making it suitable for various applications, including simulations, cryptography, and gaming.

import random

random.randint(1, 10)

random.random()

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice == 0:
    print(Rock)
elif user_choice == 1:
    print(Paper)
elif user_choice == 2:
    print(Scissors)
else:
    print("You typed an invalid number, you lose!")

computer_choice = random.randint(0, 2)

print("Computer chose:")

if computer_choice == 0:
    print(Rock)
elif computer_choice == 1:
    print(Paper)
elif computer_choice == 2:
    print(Scissors)
    
if user_choice == computer_choice:
    print("It's a draw")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You lose!")

