# Start game
input("Hello Player!")
input("Welcome to the game of Peace!")
input("If you never played this game before, here are the rules.")
input("Peace is a simple card game where the objective is to win all the cards. The player must flip over the top card of their decks after the computer has done so, and the one with the higher card takes both cards. If there's a tie, a peaceful exchange occurs, where the computer and the player need to place 3 cards face down and then place the 4th card face-up. The card with the higher rank will win all the cards on the board. The game continues until either you or the computer collect all the cards. Click enter to proceed when you're ready.")
input("This game is auto-generated, so all you need to do is click enter when prompted to!")
input("Let's start!")

# Import necessary modules
import random

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
input("Creating deck...")
deck = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle the deck 
random.shuffle(deck)
input("Shuffling deck...")

# Split the deck into two hands
mid = len(deck) // 2
player1_hand = deck[:mid]
player2_hand = deck[mid:]
deck = []
input("Splitting deck...")

pile1 = []
pile2 = []
war_pile = []

def card_value(card):
    # Return the index of the card rank
    return ranks.index(card[0])

def card_comparison(p1_card, p2_card):
    # This is the logic that compares two cards to find the stronger card 
    # Return 1 if player 1's card is stronger, 2 for player 2
	# if the cards are equal, return 0.
    if card_value(p1_card) == card_value(p2_card):
        return 0
    if card_value(p1_card) > card_value(p2_card):
        return 1
    if card_value(p1_card) < card_value(p2_card):
        return 2

def play_round(player1_hand, player2_hand):
    # Play a single round of the game.
	# That is, each player flips a card, and the winner is determined using the card_comparison function
	# if both players flip the same value card, call the war function
    if len(player1_hand) > 0 and len(player2_hand) > 0:
        p1_card = player1_hand.pop(0)
        p2_card = player2_hand.pop(0)

        print(f"Player 1 drew {p1_card[0]} of {p1_card[1]}.")
        print(f"Player 2 drew {p2_card[0]} of {p2_card[1]}.")
        
        result = card_comparison(p1_card, p2_card)
        if result == 0:
            print("A draw! Time for Peace")
            war_pile.extend([p1_card, p2_card])
            war(player1_hand, player2_hand)
        if result == 1:
            print("Player 1 wins the round!")
            pile1.extend([p1_card, p2_card])
            print(f"Player 1 score: {len(pile1)}.")
            print(f"Player 2 score: {len(pile2)}.")
        if result == 2:
            print("Player 2 wins the round!")
            pile2.extend([p1_card, p2_card])
            print(f"Player 1 score: {len(pile1)}.")
            print(f"Player 2 score: {len(pile2)}.")
    
    if len(player1_hand) == 0 or len(player2_hand) == 0:
        print("A player is out of cards. Starting next round...")
        print(f"Player 1 has {len(player1_hand)} cards before stitch.")
        print(f"Player 2 has {len(player2_hand)} cards before stitch.")
        player1_hand.extend(pile1)
        pile1.clear()
        player2_hand.extend(pile2)
        pile2.clear()
        print(f"Player 1 has: {len(player1_hand)} cards.")
        print(f"Player 2 has: {len(player2_hand)} cards.")
        print("Current pile counts reset to 0.")
        
def war(player1_hand, player2_hand):
    # Handle the 'war' scenario when cards are equal.
    # recall the rules of war, both players put 3 cards face down, then both players flip face up a 4th card. The player with the stronger card takes all the cards.	
    global war_pile
    if len(player1_hand) > 3 and len(player2_hand) > 3:
        p1_war_cards = [player1_hand.pop() for _ in range(3)]
        p2_war_cards = [player2_hand.pop() for _ in range(3)]

        war_pile.extend(p1_war_cards)
        war_pile.extend(p2_war_cards)
        print(f"Peace pile value: {len(war_pile)}.")

        p1_card = player1_hand.pop(0)
        p2_card = player2_hand.pop(0)

        result = card_comparison(p1_card, p2_card)
        if result == 0:
            print("Another tie! Peace rages on...")
            print(f"Player 1 score: {len(pile1)}.")
            print(f"Player 2 score: {len(pile2)}.")
            war_pile.extend([p1_card, p2_card])
            war(player1_hand, player2_hand)
        if result == 1:
            print("Player 1 wins Peace!")
            pile1.extend([p1_card, p2_card] + war_pile)
            war_pile.clear()
            print(f"Player 1 score: {len(pile1)}.")
            print(f"Player 2 score: {len(pile2)}.")
        if result == 2:
            print("Player 2 wins Peace!")
            pile2.extend([p1_card, p2_card] + war_pile)
            war_pile.clear()
            print(f"Player 1 score: {len(pile1)}.")
            print(f"Player 2 score: {len(pile2)}.")

    if len(player1_hand) < 4 or len(player2_hand) < 4:
        print("A player does not have enough cards for Peace. Starting the next round...")
        player2_hand.extend(pile2)
        player2_hand.extend(war_pile[:mid])
        pile2.clear()
        player1_hand.extend(pile1)
        player1_hand.extend(war_pile[mid:])
        war_pile.clear()
        pile1.clear()
        print(f"Player 1 has: {len(player1_hand)} cards.")
        print(f"Player 2 has: {len(player2_hand)} cards.")
        print("Current pile counts reset to 0.")

def play_game():
    # Main function to run the game.
    global player1_hand, player2_hand, pile1, pile2
    while len(player1_hand) > 0 and len(player2_hand) > 0:
        play_round(player1_hand, player2_hand)

    if len(player2_hand) == 52:
        print("Player 1 has no more cards, Player 2 wins the game!")
    if len(player1_hand) == 52:
        print("Player 2 has no more cards, Player 1 wins the game!")

# Call the main function to start the game
play_game()
