import random

def main():
  print("Hello, welcome to Rock, Paper, Scissors!")
  print("Here are the rules:")
  print("""
   Two players secretly pick one of “rock,” “paper,” or “scissors.”
   Both players reveal their selection to the other player at once; the winner is chosen
   based on what the selections are. Rock beats scissors (by crushing them); scissors
   beats paper (by cutting it); and paper beats rock (by covering it). If both players
   select the same one, it is a tie.
  """)
  player_selection = input("What do you select? (rock, paper, scissors): ")
  computer_selection = random.choice(["rock", "paper", "scissors"])

if __name__ == '__main__':
  main()
