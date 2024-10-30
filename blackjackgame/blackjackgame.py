# Import necessary modules
import random

def start_game():
    # Define the ranks and suits
    ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "A")
    suits = ("hearts", "diamonds", "clubs", "spades")

    # Create a deck of cards
    input("Creating deck...")
    deck = [(rank, suit) for rank in ranks for suit in suits]

    # Shuffle the deck 
    random.shuffle(deck)
    input("Shuffling deck...")

    player = []
    dealer = []
    player_bet = 0
    player_cash = 50
    
    # Start the game loop
    main_loop(dealer, player, deck)

def card_value(card):
    if card[0] in ["Jack", "Queen", "King"]:
        return 10
    elif card[0] == "A":
        return 11 or 1
    else:
        return int(card[0])

def card_comparison(player, dealer):


def main_loop(dealer, player):
    while len(deck) > 0:
        if player_cash > 0: 
            while True:
                try:
                    ans = input(f"Would you like to take your earnings and leave?: y or n")
                    if ans == "y":
                        input("Understood, have a nice day!")
                        break
                    elif ans == "n":
                        print("Yaaaa, that's the spirit. Quitting is for the weak!")
                        break
                    else:
                        input("That isn't a valid answer cuzzo. Try again.")
                except ValueError:
                    input("That isn't a valid answer cuzzo. Try again")

            if ans == "n":
                print(f"Player has {player_cash} dollars.")
                player_bet = int(input(f"How much would you like to bet?: "))
                
                input(f"Player has bet {player_bet} dollars.")
                player_card1 = deck.pop(0)
                dealer_card1 = deck.pop(0)
                player_card2 = deck.pop(0)
                dealer_card2 = deck.pop(0)

                print(f"Player has the {player_card1[0] of player_card1[0]} and the {player_card2[0]} of {player_card2[1]}.")
            if ans == "y":
                input("Weakling...")
                break
        if player_cash == 0:
            print("Player is out of cash.")
            input("Get lost broke boy.")
            break

start_game()
