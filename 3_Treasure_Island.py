# Conditional Statements, Logical Operators, Code Blocks and Scope

print('''
   ___________________________
   _|__ _________________ __|__
  _|___||               ||_|__
  ___|_||       )  '    ||___|_
   _|__||    ( ()\(     ||_|___
  ___|_||  ( ,|,(X)'    ||___#_
  _|___|| /,)/|`\``\\\  |||__/\
  ejm  ''---------------''  /  `--#
       . - ------------ . #/      |
     (( (((  (( ))) ))))  )\      |
       `  -   ----  __ -/\  `.__.-#
                  C(__)`\ \____
                      /_`\/___/
''') 

print("Welcome to Treasure Island. Your mission is to find the treaure.")

left_or_right = input("Left or Right? ")

if left_or_right == "Left":
    swim_or_wait = str(input("You came across a river, swim or wait? "))

    if swim_or_wait == "Wait":
        which_door = str(input("Which Door? Red, Blue, Yellow? "))

        if which_door == "Red":
            print("Burned by fire. Game Over.")
        elif which_door == "Blue":
            print("Eaten by beasts. Game over.")
        elif which_door == "Yellow":
            print("You Win!")
        else:
            print("Just Game Over!")
    else:
        print("You've been attacked by trout. Game over")

else:
    print("You fell into a hole. Game Over!")