import random


def get_choises():
  options = ["rock", "paper", "scissors"]
  player_choice1 = input("Enter a choise (rock, paper, scissors): ")
  player_choice = player_choice1.lower()
  while player_choice not in options:
    print("Invalid choice. Please select from rock, paper, or scissors")
    player_choice = input("Enter a choice (rock, paper, scissors): ")
  computer_choice = random.choice(options)
  choises = {"player": player_choice, "computer": computer_choice}
  return choises


def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You lose."
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!"
    else:
      return "Scissors cuts paper! You lose."
  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts paper! You win!"
    else:
      return "Rock smashes scissors! You lose."


choises = get_choises()
result = check_win(choises["player"], choises["computer"])
print(result)
