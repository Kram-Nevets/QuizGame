print("Welcome To Quiz Game!!!")

PlayerName = input("Name: ")

score = 0

print(f"Hello! {PlayerName}")

Playing = input("Do You Want To play?Yes/No: ")

if Playing.lower() != "yes":
    quit()

else:
    print("okay lets play ")

answer = input("1.what is the center of the earth?:\n")

if answer.lower() == "core":
    score +=1
    print("correct")
    
else:
    print("wrong")

answer = input("2.Who is the king of the jungle?:\n")

if answer.lower() == "lion":
    score +=1
    print("correct")
   
else:
    print("wrong")

answer = input("3.What is the center of the solar system?:\n")

if answer.lower() ==  "sun":
    score +=1
    print("correct")
   
else:
    print("wrong")

print(score)

print(f"Congratulations {PlayerName} you have gained a total score of {score}")