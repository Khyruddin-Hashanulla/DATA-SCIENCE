"""
Q8. Create a class Player with:
- A class variable player_count
- Instance variables name and level
Track how many players were created.
"""

class Player:
    player_count = 0  # Class variable to track the number of players

    def __init__(self, name, level):
        self.name = name  # Instance variable for player's name
        self.level = level  # Instance variable for player's level
        Player.player_count += 1  # Increment player count when a new player is created

    @classmethod
    def get_player_count(cls):
        return cls.player_count  # Class method to get the current player count

# Example usage:
player1 = Player("Alice", 5)
player2 = Player("Bob", 10)
print(f"Player 1: Name = {player1.name}, Level = {player1.level}")
print(f"Player 2: Name = {player2.name}, Level = {player2.level}")
print(f"Total players created: {Player.get_player_count()}")
