import random
import time
import os

number_of_attempts = 7
user_attempts = 0
user_answer = 0
correct_answer = random.randint(1, 100)

print("Hi! Let's try guessing a number from 1 to 100.")
print("You have only 7 attempts.")

running = True

while running:
    starting_time = time.perf_counter()
    number_of_attempts = 7
    print(correct_answer)
       
    while True:
        current_time = time.perf_counter()
        elipsed_time = current_time - starting_time
        seconds = int(elipsed_time) % 60
        minutes = int(elipsed_time / 60) % 60
        try:
            user_answer = int(input("Guess the number! "))
        except ValueError:
            print("Only numbers! You haven't lose your attempt this time!")
            continue    
        if number_of_attempts == 1:
            print("You have no more attempts.")
            print("The number was",correct_answer)            
            break
        else:
            if user_answer == correct_answer:
                user_attempts = 1
                print("Congratulations, the number was", correct_answer, "you won! You only needed", user_attempts,"attempts!")
                break          
            elif user_answer > correct_answer:
                number_of_attempts -= 1
                user_attempts += 1
                print("Too low! You have",number_of_attempts,"attempts left!")
            else:
                number_of_attempts -= 1
                user_attempts += 1
                print("Too high! You have",number_of_attempts, "attempts left!")

    print(f"It only took you: {minutes:02} minutes and {seconds:02} seconds")           
    restart_game = input("Try again? Yes/No ").upper()  
    if restart_game == "YES":
        number_of_attempts = 7
    else:
        print("ending the game")
        break




# starting_time = time.perf_counter()
# while True:
#     current_time = time.perf_counter() # time.time()
#     elipsed_time = current_time - starting_time
#     seconds = int(elipsed_time) % 60
#     minutes = int(elipsed_time / 60) % 60
#     hours = int(elipsed_time / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")


#     time.sleep(1)
#     os.system("cls")












# import random 

# number_of_attempts = 7
# user_attempts = 0
# user_answer = 0
# correct_answer = random.randint(1, 100)

# print("Hi, let's try guessing a number from 1 to 100.")
# print("You have only 7 attempts.")

# running = True

# while running:
#     number_of_attempts = 7
#     while True:
#         try:
#             user_answer = int(input("Guess the number! "))
#         except ValueError: 
#             print("Only numbers! You didn't lose your attempt!")
#             continue     
#         if number_of_attempts == 1: 
#             print("You have no more attempts.")
#             print("The number was",correct_answer)            
#             restart_game = input("Do you want to try again? Yes/No ")                
#             if restart_game == "YES":
#                 continue
#             elif restart_game == "NO":
#                 running = False
#             else:
#                 running = False 
#                 break
#         else:
#             if user_answer == correct_answer:
#                 user_attempts = 1
#                 break          
#             elif user_answer > correct_answer:
#                 number_of_attempts -= 1
#                 user_attempts += 1
#                 print("Too high! You have",number_of_attempts,"attempts left!")
#             else: 
#                 number_of_attempts -= 1
#                 user_attempts += 1
#                 print("Too low! You have",number_of_attempts, "attempts left!")
#     print("Congratulations, the number was", correct_answer, "you won! You only needed", user_attempts,"attempts!")
#     restart_game = input("Do you want to try again? Yes/Нет ")                
#     if restart_game == "YES":
#         number_of_attempts = 7
#         continue
#     elif restart_game == "NO":
#         running = False
#     else:
#         running = False 
#         break         
    
            


# import os
# import random
# import time


# number_of_attempts = 7
# user_attempts = 0
# user_answer = 0
# correct_answer = random.randint(1, 100)
# print("Hello, let's try guessing a number 1-100")
# print("You have 7 attempts")
# running = True
# starting_time = time.perf_counter()    
# while running:       
#         while True: 
#             try:
#                 user_answer = int(input("Guess the number! "))
#             except ValueError: 
#                 print("Type in only numbers! You didn't lose your attempt this time!")     
#             if 1 == number_of_attempts: 
#                 print("You have no more attempts")
#                 print("The number was",correct_answer)
#                 # print(f"Time passed:{hours:02}:{minutes:02}:{seconds:02}")
#                 restart_game = input("Do you want to try again? Yes/No ")                
#                 if restart_game == "Yes,yes,YEs":
#                     running
#                 elif restart_game == "No,no,nO":
#                     running = False
#                 else:
#                     break
#             else:
#                 if user_answer == correct_answer:
#                     user_attempts =+ 1
                     
#                     break              
#                 elif user_answer > correct_answer:
#                     number_of_attempts = number_of_attempts -1
#                     user_attempts = user_attempts + 1
#                     print("Too high! You have",number_of_attempts," attempts left!")
#                 else: 
#                     number_of_attempts = number_of_attempts -1
#                     user_attempts = user_attempts + 1
#                     print("Too low! You have",number_of_attempts, "attempts left!")           
#             # print(f"Time passed:{hours:02}:{minutes:02}:{seconds:02}")
#         restart_game = input("Do you want to try again? Yes/No").upper()                
#         if restart_game == "YES":
#             continue
#         elif restart_game == "NO":
#             running = False
#         else:
#             running = False



# import random 
# number_of_attempts = 7
# user_attempts = 0
# user_answer = 0
# correct_answer = random.randint(1, 100)
# print("Hello, let's try guessing a number 1-100")
# print("You have 7 attempts")
# running = True
    
# while running:
#     while True:
#         try:
#             number_of_attempts = 7
#             user_answer = int(input("Guess the number! "))
#         except ValueError: 
#             print("Type in only numbers! You didn't lose your attempt this time!")     
#         if 1 == number_of_attempts: 
#             print("You have no more attempts")
#             print("The number was",correct_answer)
#             restart_game = input("Do you want to try again? Yes/No ")                
#             if restart_game == "Yes,yes,YEs":
#                 running
#             elif restart_game == "No,no,nO":
#                 running = False
#             else:
#                 break
#         else:
#             if user_answer == correct_answer:
#                 user_attempts =+ 1
#                 print("Congratulations, the number was", correct_answer, "you won! And you needed", user_attempts,"attempts!")
#                 restart_game = input("Do you want to try again? Yes/No").upper()                
#                 if restart_game == "YES":
#                     number_of_attempts = 7
#                     continue
#                 elif restart_game == "NO":
#                     running = False
#                 else:
#                     running = False 
#                     break                
#             elif user_answer > correct_answer:
#                 number_of_attempts = number_of_attempts -1
#                 user_attempts = user_attempts + 1
#                 print("Too high! You have",number_of_attempts," attempts left!")
#             else: 
#                 number_of_attempts = number_of_attempts -1
#                 user_attempts = user_attempts + 1
#                 print("Too low! You have",number_of_attempts, "attempts left!")
            

# while running:
#     while True:
#         try:
#             user_answer = int(input("Guess the number! "))
#         except ValueError: 
#             print("Type in only numbers! You didn't lose your attempt this time!")     
#         if number_of_attempts == 1: 
#             print("You have no more attempts")
#             print("The number was",correct_answer)
#             restart_game = input("Do you want to try again? Yes/No ")                
#             if restart_game.lower() == "yes":
#                 running
#             elif restart_game.lower() == "no":
#                 running = False
#             else:
#                 break
#         else:
#             if user_answer == correct_answer:
#                 user_attempts = 1
#                 print("Congratulations, the number was", correct_answer, "you won! And you needed", user_attempts,"attempts!")
#                 restart_game = input("Do you want to try again? Yes/No").upper()                
#                 if restart_game == "YES":
#                     number_of_attempts = 7
#                     continue
#                 elif restart_game == "NO":
#                     running = False
#                 else:
#                     running = False 
#                     break                
#             elif user_answer > correct_answer:
#                 number_of_attempts -= 1
#                 user_attempts += 1
#                 print("Too high! You have",number_of_attempts," attempts left!")
#             else: 
#                 number_of_attempts -= 1
#                 user_attempts += 1
#                 print("Too low! You have",number_of_attempts, "attempts left!")