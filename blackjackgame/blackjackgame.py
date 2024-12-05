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
    player_cash = 50
    
    # Start the game loop
    main_loop(deck, player_cash)

def card_value(card):
    if card[0] in ["Jack", "Queen", "King"]:
        return 10
    elif card[0] == "A":
        return 11
    else:
        return int(card[0])

def hand_value(hand):
    value = sum(card_value(card) for card in hand)
    aces = sum(1 for card in hand if card[0] == "A")
    
    while value > 21 and aces:
        value -= 10
        aces -= 1
    
    return value

def main_loop(deck, player_cash):
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
                if player_cash > 0:
                    while True:
                        try:
                            player_bet = int(input(f"How much would you like to bet?: "))
                            if player_bet == player_cash:
                                print("All in? That's a huge risk... I like it!")
                                break

                            elif player_bet > player_cash:
                                print("That's too much for you buddy. Do you know how to count? Try again.")
                            elif player_bet < player_cash:
                                input(f"Player has bet {player_bet} dollars.")
                                break

                            else:
                                print("Incorrect value. Try again.")

                        except ValueError:
                            input("That ain't a number buddy. Try again.")

                    if player_bet < player_cash or player_bet == player_cash:
                        player_hand = [deck.pop(), deck.pop()]
                        dealer_hand = [deck.pop(), deck.pop()]

                        print(f"Player has the {player_hand[0][0]} of the {player_hand[0][1]} and the {player_hand[1][0]} of {player_hand[1][1]}.")
                        print(f"Dealer shows the {dealer_hand[0][0]} of {dealer_hand[0][1]}.")

                        player_value = hand_value(player_hand)
                        dealer_value = hand_value(dealer_hand)

                        print(f"Player's total hand value: {player_value}.")
                        
                        while player_value < 21:
                            try:
                                player_choice = input("Would you like to hit, stand, or double?")
                                if player_choice == "hit":
                                    if player_value < 21:
                                        player_hand = deck.pop(0)
                                        print("Player hits.")
                                        print(f"Player has drawn the {player_hand[0][0]} of the {player_hand[0][1]}.")
                                        player_value = hand_value(player_hand)
                                        input(f"Player's total hand value: {player_value}.")
                                        input(f"Dealer flips his other card. It is the {dealer_hand[1][0]} of {dealer_hand[1][1]}.")
                                        input(f"Dealer's current hand value at {dealer_value}.")
                                    if player_value > 21:
                                        print("Player busts.")
                                        break

                                elif player_choice == "stand":
                                    print("Player stands.")
                                    input(f"Player's hand value: {player_value}.")
                                    break

                                elif player_choice == "double":
                                    if player_cash >= player_bet * 2:
                                        print("Player has doubled their bet!")
                                        player_hand = deck.pop(0)
                                        player_value = hand_value(player_hand)
                                        input(f"Player's total hand value: {player_value}.")
                                        break

                                    if player_cash < player_bet * 2:
                                        print("You cannot double. You do not have enough cash.")

                                else:
                                    print("Incorrect input. Try again.")

                            except ValueError:
                                print("Incorrect input. Try again.")

                        if player_value == 21:
                            print("Player's hand value: {player_value}.")

            if ans == "y":
                print("Weakling...")
                break
            input(f"Dealer flips his other card. It is the {dealer_hand[1][0]} of {dealer_hand[1][1]}.")
            input(f"Dealer's current hand value at {dealer_value}.")
                
        if player_cash <= 0:
            print("Player is out of cash.")
            input("Get lost broke boy.")
            break

start_game()
