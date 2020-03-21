"""
Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples:

rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!
rockpaperscissors
"""
def rps(p1, p2):
    if {"scissors":"paper", "paper": "rock", "rock":"scissors"}[p1] == p2:
        return "Player 1 won!"
    if p1 == p2:
        return "Draw!"
    return "Player 2 won!"
  
