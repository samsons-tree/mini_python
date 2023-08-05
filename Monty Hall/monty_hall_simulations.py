import random

def randomise_doors():
    prizes = ['car', 'goat', 'goat']
    doors = {1: None, 2: None, 3: None}
    random.shuffle(prizes)
    for n in range(0,3):
        doors[n + 1] = prizes[n]
    return doors

def reveal(guess: int, doors: dict):
    for n in range(1,4):
        if doors[n] == 'goat' and n != guess:
            goat_door = n
            break
    other_door = 6 - (guess + goat_door)
    return goat_door, other_door

def check_guess(guess: int, doors: dict) -> bool:
        if doors[guess] == 'car':
            return 1
        elif doors[guess] == 'goat':
            return 0

def monty_hall(guess: int, switch: bool) -> bool:
    doors = randomise_doors()
    revealed, other = reveal(guess, doors)
    if switch == True:
        return check_guess(other, doors)
    else:
        return check_guess(guess,doors)
    
def test_mh(switch, simulations):
    guesses = [1, 2, 3]
    results = []
    for n in range(simulations):
        results.append(monty_hall(random.choice(guesses), switch))
    return results

if __name__ == '__main__':
    switch_results = test_mh(True, 1_000_000)
    stick_results = test_mh(False, 1_000_000)
