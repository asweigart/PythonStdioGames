"""Blackjack, by Al Sweigart al@inventwithpython.com

A card game also known as 21.
More info at: https://en.wikipedia.org/wiki/Blackjack"""
__version__ = 1

import random, sys

# Setup the constants:
HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
BACKSIDE = 'backside'


def main():
    """Runs a single game of Blackjack."""
    print('''BLACKJACK
    By Al Sweigart al@inventwithpython.com

    Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the pot carries over to the next round.
    The dealer stops hitting themselves at 17.''')

    money = 100
    pot = 0
    while True:  # Main game loop.
        # Check if the player has run out of money:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

        # Let the player enter their bet for this round:
        print('Money:', money)
        bet = getBet(money)

        # Set up the pot and deal the cards:
        pot += bet * 2  # Dealer matches the player's bet.
        money -= bet
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Handle player actions:
        print('Pot:', pot)
        while True:  # Keep looping until player stands or busts.
            displayHands(playerHand, dealerHand, False)
            print()

            # Check if the player has bust:
            if getCardValue(playerHand) > 21:
                break

            # Get the player's move, either H, S, or D:
            move = getMove(playerHand, money)

            # Handle the player actions:
            if move == 'D':
                # Player is doubling down, they can increase their bet:
                additionalBet = getBet(min(bet, money))
                money -= additionalBet
                pot += additionalBet * 2  # Dealer matches the bet.
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Pot:', pot)

            if move in ('H', 'D'):
                # Hit/doubling down takes another card.
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getCardValue(playerHand) > 21:
                    # The player has busted:
                    continue

            if move in ('S', 'D'):
                # Stand/doubling down stops the player's turn.
                break
            # At this point, go back to the start of the loop.

        # Handle the dealer's actions:
        if getCardValue(playerHand) <= 21:
            while getCardValue(dealerHand) < 17:
                # The dealer hits:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getCardValue(dealerHand) > 21:
                    break  # The dealer has busted.
                pause()

        displayHands(playerHand, dealerHand, True)  # Show the final hands.

        playerValue = getCardValue(playerHand)
        dealerValue = getCardValue(dealerHand)
        # Handle whether the player won, lost, or tied.
        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(pot))
            money += pot
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
        elif playerValue > dealerValue:
            print('You won ${}!'.format(pot))
            money += pot
        elif playerValue == dealerValue:
            print('It\'s a tie, the dealer wins.')
        else:
            # This line should never run unless there's a bug:
            assert False
        pot = 0  # Reset the pot.

        pause()


def displayCards(cards):
    """Display all the cards in the `cards` list."""
    rows = ['', '', '', '', '']  # Stores the text to display.

    for i, card in enumerate(cards):
        rows[0] += ' ___  '  # Print the top line of the card.
        if card == BACKSIDE:
            # Print a card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print the card's front:
            rank, suit = card  # The card is a tuple data structure.
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # Print each row on the screen:
    for i in range(4):
        print(rows[i])


def getCardValue(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are
    worth 11 or 1 (this function picks the most suitable ace value)."""
    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards:
    for card in cards:
        rank = card[0]  # `card` is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):  # Face cards are worth 10 points.
            value += 10
        else:
            value += int(rank)  # Numbered cards are worth their number.

    # Add the value for the aces:
    for i in range(numberOfAces):
        if value + 11 <= 21:
            value += 11  # Add 11 if it doesn't push the total over 21...
        else:
            value += 1  # ...otherwise, just add 1.

    return value


def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # Add the numbered cards.
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))  # Add the face and ace cards.
    random.shuffle(deck)
    return deck


def getBet(maxBet):
    """Ask the user how much they want to bet for this round."""
    while True:  # Keep asking until they enter a valid amount.
        print('How much do you bet? (1-{}, or "quit")'.format(maxBet))
        bet = input().upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue  # If the player didn't enter a number, ask again.

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet  # Player entered a valid bet.
        # At this point, go back to the start of the loop.


def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards."""
    print()
    if showDealerHand:
        print('DEALER:', getCardValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # Hide the dealer's first card:
        displayCards([BACKSIDE] + dealerHand[1:])

    # Show the player's cards:
    print('PLAYER:', getCardValue(playerHand))
    displayCards(playerHand)


def pause():
    input('Press Enter to continue...')
    print('\n\n')


def getMove(playerHand, money):
    while True:  # Keep looping until the player enters a correct move.
        # Determine what moves the player can make:
        moves = ['(H)it', '(S)tand']

        # The player can double down on their first move, which we can
        # tell because they'll have exactly two cards:
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get the player's move:
        movePrompt = ', '.join(moves) + ': '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move  # Player has entered a valid move.
        if move == 'D' and '(D)ouble down' in moves:
            return move  # Player has entered a valid move.
        # At this point, go back to the start of the loop.


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
