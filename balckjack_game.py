import random
import art

# Print the logo of the game
print(art.logo)

# Function to deal a random card
def deal_card():
    """Returns a random card value."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # Jack, Queen, King = 10; Ace = 11
    return random.choice(cards)

# Function to calculate the score with Ace adjustment
def calculate_score(cards):
    """Calculates the score, adjusting Aces from 11 to 1 if necessary."""
    total = sum(cards)
    while 11 in cards and total > 21:  # Adjust Ace (11 → 1) if total > 21
        cards.remove(11)
        cards.append(1)
        total = sum(cards)
    return total

# Function to play the game
def blackjack():
    """Runs the Blackjack game loop."""
    while True:  # Ensure valid starting money
        pocket_input = input("How much do you bring to the table? :$ ")
        if pocket_input.isdigit() and int(pocket_input) > 0:
            pocket = int(pocket_input)
            break
        else:
            print("Invalid input! Enter a positive number for the money.")

    while pocket > 0:
        print(f"\nYour current balance: ${pocket}")
        
        # Bet validation
        while True:
            bet_input = input("How much do you want to bet? :$ ")
            if bet_input.isdigit():
                bet = int(bet_input)
                if 0 < bet <= pocket:
                    break
                else:
                    print(f"Bet must be between $1 and ${pocket}.")
            else:
                print("Invalid input! Please enter a number.")

        # Initialize cards
        player_cards = [deal_card(), deal_card()]
        dealer_cards = [deal_card(), deal_card()]

        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"\nYour cards: {player_cards}, current total: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        # Check for Blackjack at the start
        if player_score == 21 and dealer_score == 21:
            print(f"\nBoth you and the dealer got Blackjack! It's a Draw! 😐")
            print(f"Dealer's cards: {dealer_cards}, total: {dealer_score}")
        elif player_score == 21:
            print(f"\nYou got a Blackjack! 🎉 You Win 1.5x your bet!")
            print(f"Dealer's cards: {dealer_cards}, total: {dealer_score}")
            pocket += int(bet * 1.5)
        elif dealer_score == 21:
            print(f"\nDealer got a Blackjack! You lose! 😟")
            print(f"Dealer's cards: {dealer_cards}, total: {dealer_score}")
            pocket -= bet
        else:
            # Player's turn
            while player_score < 21:
                choice = input("Do you want to 'h' (Hit) or 's' (Stand)? ").lower()
                if choice == 'h':
                    player_cards.append(deal_card())
                    player_score = calculate_score(player_cards)
                    print(f"Your cards: {player_cards}, current total: {player_score}")
                elif choice == 's':
                    break
                else:
                    print("Invalid input! Choose 'h' (Hit) or 's' (Stand).")

            # Check if player busts
            if player_score > 21:
                print("Bust! You lose! 😟")
                pocket -= bet
            else:
                # Dealer's turn
                print("\nDealer's turn...")
                while dealer_score < 17:
                    dealer_cards.append(deal_card())
                    dealer_score = calculate_score(dealer_cards)

                print(f"Dealer's cards: {dealer_cards}, total: {dealer_score}")

                # Compare results
                if dealer_score > 21 or player_score > dealer_score:
                    print("You Win! 🎉")
                    pocket += bet
                elif dealer_score > player_score:
                    print("Dealer Wins! You Lose! 😟")
                    pocket -= bet
                else:
                    print("It's a Draw! 😐")

        # Check if out of money
        if pocket <= 0:
            print("\nYou are out of money! Game over!")
            break

        # Play again?
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print(f"Thanks for playing! Your final balance is ${pocket}.")
            break

# Start the game
blackjack()
