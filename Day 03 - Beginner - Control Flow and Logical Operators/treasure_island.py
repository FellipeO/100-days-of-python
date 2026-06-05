print(r'''
        _
       (_)
       |=|
       |=|
   /|__|_|__|\
  (    ( )    )
   \|\/\"/\/|/
     |  Y  |
     |  |  |
     |  |  |
    _|  |  |
 __/ |  |  |\
/  \ |  |  |  \
   __|  |  |   |
/\/  |  |  |   |\
 <   +\ |  |\ />  \
  >   + \  | LJ    |
        + \|+  \  < \
  (O)      +    |    )
   |             \  /\ 
 ( | )   (o)      \/  )
_\\|//__( | )______)_/ 
        \\|//        
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input("Crossroads ahead. You must choose... left or right?\n")
if choice.lower() == "right":
    choice = input("So far so good! There's a lake in front of you. You must choose... swim or wait?\n")
else:
    print("Game Over! You fell into a hole.")
    exit(0)

if choice.lower() == "wait":
    choice = input("By being patient you were able to get a ride by boat. Now you're at the island and there's "
                   "four doors ahead of you.\nYou must choose... red, yellow or blue?\n")
else:
    print("Game Over! The shark got you.")
    exit(0)

if choice.lower() == "red":
    print("That door leads to an incinerator. As you open it, you're burned to a crisp.\nGame Over!")
elif choice.lower() == "blue":
    print("Hungry tigers comes out of this one...\nGame Over!")
elif choice.lower() == "yellow":
    print("Congratulations!\nThe treasure is yours!")
else:
    print(f"You can't find this particular door... does {choice} even exists?\nYou die longing for an answer\nGame Over!")