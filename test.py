import random
a = []
play = True
while play == True :
    secret_number = random.randint(0,10)
    guess_limit = 3 
    guess_count = 0
    while guess_count < guess_limit :
            guess = input("guess: ")
            if guess in a :
                print(f"you have already chose this number : {guess}")
                guess_count -= 1
            a.append(guess)
            guess_count += 1
            if int(guess) == secret_number :
                print('correct')
                
                break
            elif int(guess) > secret_number and guess_count < guess_limit:
                print("wrong! guess lower number")
            elif  int(guess) < secret_number and guess_count < guess_limit:
                print("wrong! guess grater number")
                
    
    print(f" the answer was {secret_number}")
    play_again = input("wanna play again? " )
    if play_again.lower() == "yes" :
        play = True
        a = []
    else : 
        play = False
        print("Bye.......")
        input()


   