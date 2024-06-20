import random
attempts=5

def game():
    
    global attempts
    attempts=5
    random_number=random.randint(1,20)

    user_input=int(input("guess a number between 1 and 20:"))


    while attempts>0:

        if random_number==user_input:
            print("good you do it")
            game_sucess()
    
        else:
            attempts=attempts-1
    
            print(f"false,you have {attempts} more chances")
            user_input=int(input("guess a number between 1 and 20:"))
            

game()    
def game_failed():
    msg_failed="""
oh next time -_-
do you want to replay?
-yes
-no
"""     
    replay_ask=str(input(msg_failed))
    if replay_ask=="yes":
        game()
    
    else:
        print("have a good time")

def game_sucess():
    msg_failed="""

do you want to replay?
-yes
-no
"""     
    replay_ask=str(input(msg_failed))
    if replay_ask=="yes":
        game()
    
    else:
        print("have a good time")
        
if attempts==0:
    game_failed()
    

