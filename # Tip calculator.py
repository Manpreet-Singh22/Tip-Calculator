# Tip calculator - A calculator to calculate tips...,
# (10%, 15%, 18% and 20%)

while True:
    try:
        user_input = input("What is the total of your check? > $")
        total_check = float(user_input)
        break 
    except ValueError:
        print("I'm sorry, it looks like you typed something incorrectly. Please type a number!")

while True:
    tip_choice = input("Type 'w' for 10%, 'x' for 15%, 'y' for 18%, or 'z' for 20% > ")
    if tip_choice not in ('w', 'x', 'y', 'z'):
        print("I'm sorry, it looks like you typed something incorrectly. Please read the instructions and try again!")
    else:
        if tip_choice == "w":
            result = .10 * total_check  
        elif tip_choice == "x":
            result = .15 * total_check  
        elif tip_choice == "y":
            result = .18 * total_check
        elif tip_choice == "z":
            result = .20 * total_check
        
        print("You should leave $%.2f " % (result))
        break