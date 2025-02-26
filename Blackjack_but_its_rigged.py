import random, sys, time

# Need to fix:
# - When dealer's hand is too big on user hit and dealer hit, user loses.
# RULES TO CONSIDER:

# You start with 2 cards, not 1, so track the number of times cards have been dealt
# If you get blackjack, you need to see if the dealer hits blackjack as well since then its a standoff and results in draw
# Need to pick a random card from a dict, since aces + king / queen / jack == win, but ace can be 1.
# If user hits 5 times and under 21 still, they win automatically.




# This is my first personal project; a fun game of poker
# It uses the 'random' module to generate all random integers

# in main, ask for 3 options.
def main():
    # define int variables
    balance = 100
    balance = int(balance)
    wins = 0
    wins = int(wins)
    losses = 0
    losses = int(losses)
    draws = 0
    draws = int(draws)

    while True:
        dealer_choice = "None"
        user_choice = "None"


        player_action = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWhere to?\n\n         |    ' Play '    |   ' Stats '    |   ' End Game '   |\n\n")
        # stats, show stats, wait until 'b' to return back
        if balance == 0:
            sys.exit("You're broke.")
        elif player_action.lower().strip() == "stats":
            print(f"\n\nBalance: ${balance}\n-------------------------------------")
            print(f"Wins: {wins} | Losses: {losses} | Draws: {draws}\n-------------------------------------")
            time.sleep(3.25)
            print("Going back to main menu in 3 seconds...")
            time.sleep(3)
        # end game, sys.exit("")
        elif player_action.lower().strip() == "end game":
            sys.exit("We closed the program for you.")
        # if ' play ':
        elif player_action.lower().strip() == "play":
            # loop
            while True:
                #  - bet = bet
                print(f"\n\n\n\n\nYou have ${balance}")
                bet = input("\nPlace your bet: $")
                try:
                    bet = int(bet)
                    #  - check bet is within balance, if it is then:
                    if bet > balance:
                        print("\nStop gambling more than you can afford fukhed")
                        continue
                    elif bet < 1:
                        print("\nYour bet is too small")
                        time.sleep(1.5)
                        continue
                    # break loop
                    else:
                        break
                except ValueError:
                    print("\nCan't even type a real number can ya?")
                    continue
            dealer_hand = 0
            user_hand = 0
            #  - randomly generate dealers and players hand
            dealer_hand = random.randrange(dealer_hand + 1, (dealer_hand + 10), 1)
            user_hand = random.randrange(user_hand + 1, (user_hand + 10), 1)
            dealer_choice = "hit"

            print("\nYour hand: ", end="")
            time.sleep(1)
            print(user_hand)
            print("Dealers' hand: ", end="")
            time.sleep(1)
            print(f"{dealer_hand}\n\n")
            time.sleep(1)

            # loop hit / stand until games over
            while True:
                #  - ask for hit or stand
                if user_choice != "stand":
                    user_choice = input("\n'Hit' or 'Stand'?\n\n")
                    pass
                else:
                    pass
                # if hit:
                # userhand = userhand.random...
                if user_choice.lower().strip() == "hit":
                    user_hand = random.randrange(user_hand + 1, (user_hand + 10), 1)
                    print("\nYour Hand: ", end="")
                    time.sleep(1)
                    print(user_hand)
                    if user_hand == 21:
                        print("You got Blackjack!")
                        balance += bet
                        wins += 1
                        leave_to_menu_display()
                        break
                    elif user_hand > 21:
                        print("You lost")
                        balance -= bet
                        losses += 1
                        leave_to_menu_display()
                        break
                    elif dealer_choice == "stand":
                        print(f"Dealers hand: {dealer_hand}\n")
                        continue
                    elif dealer_choice != "stand":
                    # If dealers hand is smaller than 16, dealer hits
                    # If dealers hand > 16, but user hand is above that but still legal, dealer hits
                        if (dealer_hand < 16) or (dealer_hand > 16 and 21 > user_hand and user_hand >= dealer_hand):
                            dealer_hand = random.randrange(dealer_hand + 1, (dealer_hand + 10), 1)
                            print(f"Dealer hand: {dealer_hand}")
                            game_finish_check = check_cards(dealer_hand, user_hand)
                            if game_finish_check == "win":
                                balance += bet
                                wins += 1
                                leave_to_menu_display()
                                break
                            elif game_finish_check == "draw":
                                draws += 1
                                leave_to_menu_display()
                                break
                            elif game_finish_check == "loss":
                                losses += 1
                                balance -= bet
                                leave_to_menu_display()
                                break
                            else:
                                continue
                    # Elif dealers’ hand > 16 + users hand smaller --> the dealer will choose to stand.
                    # Elif dealers’ hand == users’ hand + dealers’ hand > 16 --> dealer will choose to stand.
                        elif (dealer_hand > 16 and dealer_hand > user_hand) or (dealer_hand == user_hand and dealer_hand > 16):
                            dealer_choice == "stand"
                            print(f"Dealer chose to stand at: {dealer_hand}")
                            continue

                # If the user stands, we need to go through the process for if the dealer has
                # stood yet or not,
                # If the dealer is still hitting, we check dealers card values to make a choice.



                # If the dealer has already chose to stand, we will check the card values for if dealer hand > user hand, etc.
                elif user_choice.lower().strip() == "stand":
                    if dealer_choice == "stand":
                        # if dealer hand is larger, dealer wins
                        if dealer_hand > user_hand:
                            balance -= bet
                            losses += 1
                            print("\nDealer won by card count\n")
                            leave_to_menu_display()
                            break
                        # if user hand is larger, user wins
                        elif user_hand > dealer_hand:
                            balance += bet
                            wins += 1
                            print("\nYou won by card count\n")
                            leave_to_menu_display()
                            break
                        # if both hands are the same, draw
                        else:
                            print("\nYou tied with the dealer.\n")
                            draws += 1
                            leave_to_menu_display()
                            break
                    elif dealer_choice == "hit":
                        # if dealer hand smallest, dealer will hit again and continue through if valid
                        # if dealers hand == users hand + dealers hand < 16  dealer will hit again, then continue on.
                        if (dealer_hand < user_hand) or (dealer_hand == user_hand and dealer_hand < 16):
                            dealer_choice == "hit"
                            dealer_hand = random.randrange(dealer_hand + 1, (dealer_hand + 10), 1)
                            print(f"\nDealer chose to hit.")
                            time.sleep(1)
                            print("Dealer hit: ", end="")
                            time.sleep(1)
                            print(dealer_hand)
                            time.sleep(1)
                            game_outcome = check_cards(user_hand, dealer_hand)
                            if game_outcome == "win":
                                balance += bet
                                wins += 1
                                print(f"+${bet}\n")
                                leave_to_menu_display()
                                break
                            elif game_outcome == "draw":
                                draws += 1
                                leave_to_menu_display()
                                break
                            elif game_outcome == "loss":
                                losses += 1
                                balance -= bet
                                print(f"-${bet}\n")
                                leave_to_menu_display()
                                break
                            else:
                                continue
                        # if dealer hand is biggest, dealer will stand and win
                        elif dealer_hand > user_hand:
                            print(f"The dealer chose to stand at: {dealer_hand}")
                            time.sleep(1)
                            print("\nDealer won by card count\n\n\n")
                            time.sleep(1)
                            balance -= bet
                            losses += 1
                            leave_to_menu_display()
                            break
                        # if both hands are same and above 16, dealer will stand aswell to draw
                        elif (dealer_hand == user_hand) and dealer_hand > 16:
                            print(f"The dealer chose to stand at: {dealer_hand}")
                            time.sleep(1)
                            print("\nYou tied with the dealer.\n\n\n")
                            draws += 1
                            leave_to_menu_display()
                            break

        else:
            print("\nYou typed something wrong buddy...")
            time.sleep(3)
            continue

def leave_to_menu_display():
    print("Leaving to menu in 5 seconds, progress automatically saves until you close the program")
    time.sleep(5)

# checks outcome of cards, prints outcome, and returns name of outcome to be dealt with in main (add balance, etc.)
def check_cards(userhand, dealerhand):
    if userhand < 21 and dealerhand < 21:
        return "continue"
    if userhand > 21 and dealerhand > 21:
        print("You and the dealer had a draw\n")
        time.sleep(1)
        return "draw"
    elif userhand > 21:
        print("You Lose\n")
        time.sleep(1)
        return "loss"
    elif dealerhand > 21:
        print("Dealer lost\n")
        time.sleep(1)
        return "win"
    elif dealerhand == 21 and userhand == 21:
        print("You tied with the dealer\n")
        time.sleep(1)
        return "draw"
    elif userhand == 21:
        print("You got Blackjack!\n")
        time.sleep(1)
        return "win"
    elif dealerhand == 21:
        print("Dealer got blackjack!\n")
        time.sleep(1)
        return "loss"


if __name__ == "__main__":
    main()