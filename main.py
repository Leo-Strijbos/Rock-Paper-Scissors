import random

moves = {1: "Rock",
2: "Paper", 3: "Scissors"}

win = {
  "Rock": "Scissors",
  "Scissors":"Paper",
  "Paper":"Rock"
}

print("Press [1] for Rock")
print("Press [2] for Paper")
print("Press [3] for Scissors")

Userinput = int(input("Choose Move:"))
playerMove = moves[Userinput]

compMove = random.randint(1, 3)

if compMove in moves:
  print("The computer chooses: " + moves[compMove])

if win[playerMove] == moves[compMove]:
  print("You Win!")
elif moves[compMove] == playerMove:
  print("Its a tie!")
else:
  print("You lose!")
