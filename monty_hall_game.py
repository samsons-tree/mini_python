import random
from time import sleep

def randomise_doors():
    prizes = ['car', 'goat', 'goat']
    doors = {1: None, 2: None, 3: None}
    random.shuffle(prizes)
    for n in range(0,3):
        doors[n + 1] = prizes[n]
    return doors
        
def check_guess(guess: int, doors: dict) -> bool:
        if doors[guess] == 'car':
            return True
        elif doors[guess] == 'goat':
            return False

def reveal(guess: int, doors: dict):
    for n in range(1,4):
        if doors[n] == 'goat' and n != guess:
            goat_door = n
            break
    other_door = 6 - (guess + goat_door)
    return goat_door, other_door
        

def monty_hall():
    doors = randomise_doors()
    sleep(2)
    print('Welcome to the Monty Hall Game Show!')
    sleep(2)
    print("There are three doors. One has an expensive car behind, and the other two have some goats.")
    sleep(4)
    print("The prize behind the door you open will be yours until your dying days.")
    sleep(3)
    print("So, which door do you want to open?")
    sleep(1.5)
    guess1 = int(input("Input 1, 2 or 3. \n"))
    print(f'\nYou selected door {guess1}.\n')
    revealed, other_door = reveal(guess1, doors)
    sleep(2)
    print(f'''Let's make this more interesting...''')
    sleep(2.5)
    print('''I'll open one of the doors with a goat.''')
    sleep(2)
    print("...")
    sleep(1)
    print(f'I can reveal that behind door number {revealed} is a {doors[revealed]}!')
    sleep(2)
    print(f'Would you still like to open door {guess1}, or would you like to open door {other_door} instead?')
    sleep(4)
    guess2 = int(input(f'Input {other_door} to switch, or {guess1} to stick with your gut. \n'))
    sleep(1)
    print(f'''\nHuh, well okay, if that's REALLY your decision... Let's see whats behind door number {guess2}!\n''')
    sleep(2)
    if check_guess(guess2, doors) == True:
        print("Wow, lucky guess! You're now the owner of a brand new 2009 Ford Ka!!")
    else:
        print("Congratulations! You've won yourself a goat.")
    sleep(20)
    
if __name__ == '__main__':
    monty_hall()