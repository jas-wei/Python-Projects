import doctest
import random

MIN_ROLL = 1
MAX_ROLL = 6
MIN_BET = 5

def digit_sum (number:int)->int:
    '''
    This function takes an integer and returns the sum of 
    each digit in the integer. If the integer is a negative
    value, the function should ignore the negative sign.
    
    >>> digit_sum(0)
    0
    >>> digit_sum(432)
    9
    >>> digit_sum(-571)
    13
    >>> digit_sum (-23)
    5
    '''
    
    absolute_value = abs(number)
    
    sum = 0
    value1 = absolute_value
    value2 = absolute_value
    
    while value2 > 0:
        value1 = value2 % 10
        sum += value1
        value2 //= 10
        
    return sum

def gcd (num1:int, num2:int)->int:
    '''
    This function takes two integers and returns the
    greatest common divisor of these two integers.
    
    Precondition: num1 and num2 > 0
    
    >>> gcd(4, 7)
    1
    >>> gcd(12, 18)
    6
    '''
    
    if num1-num2 >= 0:
        smallest_num = num2
    else:
        smallest_num = num1
    
    for divisor in range(smallest_num,0,-1):
        if num1 % divisor ==0 and num2 % divisor ==0:
            return divisor
            
def roll_one_die() -> int:
    """ simulates the roll of a single dice between MIN_ROLL and MAX_ROLL
    inclusive and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    # generates a random number between MIN_ROLL and MAX_ROLL inclusive
    die = random.randint(MIN_ROLL, MAX_ROLL)

    # for testing to allow you to enter the dice roll you want at the keyboard
    # comment out the line above and uncomment this line:
    # die = int(input('enter a simulated dice roll\n'))

    return die

def play_again ()->bool:
    '''
    This function prompts the player to determine whether 
    they want to play again. If the player enters yes the
    function should return True but if the player enters any
    other value the function should return False.
    '''
    phrase = 'Do you want to make a bet?  Enter yes if you do: '
    prompt = input(phrase)
    
    if prompt == 'yes':
        return True
    else:
        return False
    
def get_guess ()->int:
    '''
    This function takes no arguments and prompts the player
    for the number they guess will be rolled on the dice. The
    function repeatedly prompts the player for a valid
    guess. An invalid guess is one that is not a whole number 
    or is a number smaller than 1 or bigger than 6. The function 
    should return the valid guess.
    '''
    phrase = 'Enter an integer between 1 and 6 inclusive: '
    guess = input(phrase)
    
    while (not guess.isdigit () 
           or int(guess) < MIN_ROLL or int(guess) > MAX_ROLL):
        guess = input(phrase)
    
    return int(guess)

def get_bet (max_money:int)->int:
    '''
    This function takes as an argument a maximum value the
    player can bet and prompts the player for the amount up
    to that maximum they would like to bet. 
    
    Precondition: max money >= MIN_BET
    '''
    phrase = (f'Enter an integer between 5 and {max_money} inclusive: ')
    money = input(phrase)
    
    while (not money.isdigit () or int(money) < MIN_BET 
           or int(money) > max_money):
        money = input(phrase)    
    
    return int(money)

def roll_dice (dice_guess:int)->int:
    '''
    This function takes as an argument the number the player
    guessed and it will simululate the roll of three dice by 
    calling the roll_one_die function. The function counts and 
    returns the number of the dice rolls that match 
    the given guess.
    
    Precondition: dice_guess needs to be between 1 and 6 inclusive
    '''
    match = 0
    count = 0
    
    for rolling in range(3):
        roll = roll_one_die ()
        print(f'Dice roll {count}: {roll}')
        count += 1
        if roll == dice_guess:
            match += 1
    
    return match

def compute_winnings (match:int, bet:int)->int:
    '''
    The function returns the amount the player has won (a positive number), 
    or lost (a negative number).
    
    Precondition: match is between 1 and 3 inclusive and bet >= MIN_BET
    
    >>> compute_winnings (0, 10)
    -10
    >>> compute_winnings (1, 10)
    10
    >>> compute_winnings (2, 10)
    20
    >>> compute_winnings (3, 10)
    100
    '''
    if match == 1:
        return bet
    elif match == 2:
        return bet * 2
    elif match == 3:
        return bet * 10
    else: 
        return bet * -1

def play_one_round (max_money: int):
    '''
    This function plays one round of the dice game which consists of the 
    player's guess, rolling three dice, and computing the amount that 
    the player won or lost.
    
    Precondition: max_money >= MIN_BET
    '''
    dice_guess = get_guess ()
    print()
    match = roll_dice (dice_guess)
    print()
    winnings = compute_winnings (match, max_money)
    
    return winnings

def play_game (max_money: int):
    '''
    This function takes as an argument the amount of money the
    player has to play with. The function should continually
    allow the player to play single rounds of the game if the 
    amount of money the player has to play with is at least MIN_BET
    and they still want to play again. The function should NOT ask
    the user if they want to play again if they do not have at least
    MIN_BET left to play with.
    '''
    if max_money >= MIN_BET:
        print(f'You have ${max_money} to play with \n')
        play = play_again ()
        print ()
    
        while max_money >= MIN_BET and play == True:
            bet_money = get_bet(max_money)
            print (f'You bet ${bet_money} \n')        
            winnings = play_one_round (bet_money)
        
            if winnings < 0:
                losings = winnings * -1
                print(f'Sorry you lost ${losings}')
            
            else:   
                print(f'Congrats!  You won ${winnings}')
        
            max_money += winnings
        
            if max_money >= MIN_BET:
                print(f'You have ${max_money} in your bankroll \n')
                play = play_again ()
                print ()            
    
        print(f'You have ${max_money} in your bankroll')
        return max_money