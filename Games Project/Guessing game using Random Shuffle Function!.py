actual_list = [' ','O',' ']

def shuffle_list(actual_list):

    shuffle(actual_list)
    
    return actual_list

actual_list

shuffle(actual_list)

actual_list

def user_guess():
    
    guess =''
    
    while guess not in ["0","1","2"]:
        
        guess = input("Pick a Number: 0 1 or 2: " )
        
        
    return int(guess)    


    user_guess()

    def user_guess_check(actual_list,guess):
    
    if actual_list[guess] =='O':
        
        print("Correct! you have guess is Awesome!!")
        
    else:
        
        print("Sorry Wrong Guess!! Better Luck Nexttime!!")
        
        print(actual_list)

        actual_list=[' ','O',' ']

shuffled_list = shuffle(actual_list)

guess = user_guess()

user_guess_check(actual_list,guess)