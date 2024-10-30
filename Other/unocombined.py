# THINGS WE (Alexander Derderian and Luke Assaad) ADDED:
# 1. If player doesn't have a valid card to play that matches the central_card, they automatically draw a card.
# 2. If player tries to input incorrect values (the choice of playing or drawing, and which card to play), the game will keep them stuck in the decision until they make a proper choice.
# 3. Win conditions and a different way of swapping whose turn it is.

import random 

def start_game():
    # THE SET UP OF UNO
    colours = ("Red", "Yellow", "Green", "Blue")
    ranks = list(range(1, 11))

    deck = [(rank, colour) for rank in ranks for colour in colours]

    # Shuffle the deck
    random.shuffle(deck)

    # Dealing the hands
    p1 = [deck.pop(0) for _ in range(7)]
    p2 = [deck.pop(0) for _ in range(7)]
    
    # Central card
    central_card = deck.pop(0)

    # Start the game loop
    main_loop(p1, p2, deck, central_card, 0)

def main_loop(p1, p2, deck, central_card, whose_turn):
    while len(p1) > 0 and len(p2) > 0:

        # Whose turn is it
        current_player = p1 if whose_turn == 0 else p2
        print(f"Player {whose_turn + 1}'s turn, here is your hand: {current_player}")
        input(f"Central card is: {central_card}")

        # Check for valid cards
        valid_cards = [card for card in current_player if valid_play(central_card, card)]
        
        # First decision: Play a card or draw a card
        if valid_cards:
            while True:
                try:
                    ans = int(input("You have a choice. You can (0) draw or (1) play: "))
                    if ans in [0,1]:
                        break
                    else:
                        input("Please input a valid number. Either 1 or 0.")
                except ValueError:
                    input("That isn't even a number doofus. Try again")
            
            # Play a card
            if ans == 1:
                while True:
                    try:
                        player_choice = int(input("Which card to play? (1 to {}): ".format(len(current_player)))) - 1
                        if 0 <= player_choice < len(current_player):
                            valid = valid_play(central_card, current_player[player_choice])
                            # If their card is valid, 1. remove that card from the hand
                            # 2. we need to place it on the face_up pile!!!
                            if valid:
                                central_card = current_player.pop(player_choice)
                                break
                            if not valid:
                                input("Please pick a valid card in the deck.")
                        else: 
                            input("Please pick a card in the deck.")
                    except ValueError:
                        input("That isn't a number. Pick a valid card in the deck.")
            
            # Draw a card
            elif ans == 0:
                draw_card = deck.pop(0)
                current_player.append(draw_card)
                input(f"You drew a card: {draw_card}.")
        
        # Automatic Draw
        else:
            print("You have no valid cards to play. You must draw.")
            draw_card = deck.pop(0)
            current_player.append(draw_card)
            input(f"You drew a card: {draw_card}.")
        
        # Player 1 wins
        if len(p1) == 0:
            print("Player 1 has no more cards! Player 1 wins the game!")
            break
        
        # Player 2 wins
        if len(p2) == 0:
            print("Player 2 has no more cards! Player 2 wins the game!")
            break

        # The end of the while loop, switch turns
        whose_turn = (whose_turn + 1) % 2

def valid_play(card1, card2):
    return card1[0] == card2[0] or card1[1] == card2[1]

start_game()
