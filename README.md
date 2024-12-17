
# Blackjack Game

This is a simple Blackjack game implemented in Python. The game allows a user to play against a dealer. The game is played by drawing cards, and the objective is to get a card total as close to 21 as possible without exceeding it.

## Requirements
- Python 3.x
- `art.py` file (for displaying game logo)

## Files

1. **blackjack.py**: The main Python script for the Blackjack game.
2. **art.py**: Contains the logo to be displayed at the start of the game.

## How to Run the Game

1. Clone or download the repository to your local machine.
2. Make sure both `blackjack.py` and `art.py` are in the same directory.
3. Run the following command in your terminal:
    ```bash
    python blackjack.py
    ```

## Game Rules

- The game is played with the objective of reaching 21 points without going over.
- Cards numbered 2 to 10 have their respective values, while face cards (Jack, Queen, King) count as 10 points.
- An Ace can count as either 1 or 11, depending on which is more advantageous for the player.
- If both the player and dealer have a Blackjack (21 points) at the start, it's a draw.

## Features

- The game ensures that the player and dealer cannot have more than 21 points.
- The player can choose to "Hit" (draw another card) or "Stand" (keep the current hand).
- The dealer draws cards until their total is 17 or more.
- The game checks if either the player or dealer gets a Blackjack at the start.

## Example Run

```
How much do you bring to the table? :$ 100
Your current balance: $100
How much do you want to bet? :$ 10

Your cards: [10, 7], current total: 17
Dealer's first card: 9
Do you want to 'h' (Hit) or 's' (Stand)? s

Dealer's turn...
Dealer's cards: [9, 5, 6], total: 20
Dealer Wins! You Lose! 😟
Your current balance: $90
Do you want to play again? (y/n): y
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
