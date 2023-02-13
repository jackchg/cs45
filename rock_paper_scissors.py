import random

def rps():
  player_selection = input("What do you select? (rock, paper, scissors): ")
  selections = ["rock", "paper", "scissors"]
  computer_selection = random.choice(selections)
  p_idx = selections.index(player_selection)
  c_idx = selections.index(computer_selection)
  if p_idx == c_idx:
    print(f"You both selected {player_selection}. It's a tie!")
    print("\nThe computer wants a rematch!\n")
    rps()
  elif p_idx == c_idx + 1 or (p_idx == 0 and c_idx == 2):
    print(f'You selected {player_selection}. The computer selected {computer_selection}. You win!')
  else:
    print(f'You selected {player_selection}. The computer selected {computer_selection}. You lose...')

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
  rps()

if __name__ == '__main__':
  main()

