import random 

def get_computer_choice():
  choices = ["Rock", "Paper", "Scissors"]
  computer_choice = random.choice(choices)
  return computer_choice

def get_user_choice():
  user_choice = input("Enter your choice (Rock, Paper, Scissors): ")
  return user_choice

print("Let's play Rock Paper Scissors!")

computer_choice = get_computer_choice()
user_choice = get_user_choice()

print("Computer chose:", computer_choice)
print("You chose:", user_choice)

def get_winner(user_choice, computer_choice):

  if user_choice == computer_choice:
    print("It's a tie!")
    winner = None

  elif user_choice == "Rock":
    if computer_choice == "Scissors":
      print("Rock smashes scissors! You win!")
      winner = "User"
    else:
      print("Paper covers rock! You lose.")  
      winner = "Computer"

  elif user_choice == "Paper":
    if computer_choice == "Rock":
      print("Paper covers rock! You win!")
      winner = "User"
    else:
      print("Scissors cuts paper! You lose.")
      winner = "Computer"

  elif user_choice == "Scissors":
    if computer_choice == "Paper":
      print("Scissors cuts paper! You win!")
      winner = "User"
    else:
      print("Rock smashes scissors! You lose.")
      winner = "Computer"
  
  return winner

def play():

  print("Let's play Rock Paper Scissors!")

  computer_choice = get_computer_choice()
  user_choice = get_user_choice()

  winner = get_winner(user_choice, computer_choice)

  print(winner)

play()