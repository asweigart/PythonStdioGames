# Blackjack, by Al Sweigart al@inventwithpython.com

import random, sys

# Setup constants:
HEARTS   = chr(9829)
DIAMONDS = chr(9830)
SPADES   = chr(9824)
CLUBS    = chr(9827)
BACKSIDE = 'backside'

def printCards(cards):
    # Display all the cards in the `cards` list:
    rows = ['', '', '', '', ''] # Stores the text to display.

    for i, card in enumerate(cards):
        rows[0] += '----- ' # Print the top line of the card.
        if card == BACKSIDE:
            # Print a card's back:
            for i in range(1, 4):
                rows[i] += '|###| '
        else:
            # Print the card's front:
            rank, suit = card # The card is a tuple data structure.
            rows[1] += '|%s | ' % (rank.ljust(2))
            rows[2] += '| %s | ' % (suit)
            rows[3] += '| %s| ' % (rank.rjust(2))
        rows[4] += '----- ' # Print the bottom line of the card.

    # Print each row on the screen:
    for i in range(5):
        print(rows[i])


def getCardValue(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are
    worth 11 or 1 (this function picks the most suitable ace value)."""
    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards:
    for card in cards:
        rank = card[0] # `card` is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'): # Face cards are worth 10 points.
            value += 10
        else:
            value += int(rank) # Numbered cards are worth their number.

    # Add the value for the aces:
    for i in range(numberOfAces):
        if value + 11 <= 21:
            value += 11 # Add 11 if it doesn't push the total over 21...
        else:
            value += 1 # ...otherwise, just add 1.

    return value


def getDeck():
    # Create a deck of all 52 cards:
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) # Add the numbered cards.
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) # Add the face and ace cards.
    random.shuffle(deck)
    return deck


def getBet(maxBet):
    # Ask the user how much they want to bet for this round:
    while True:
        print('How much do you bet? (1-%s, or "quit")' % (maxBet))
        bet = input().upper()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue # If the player didn't enter a number, just ask again.

        bet = int(bet)
        if (1 <= bet <= maxBet):
            return bet # Player entered a valid bet.


def showHands(playerHand, dealerHand, showDealerHand):
    # Show the dealer's cards:
    print()
    if showDealerHand:
        print('DEALER:', getCardValue(dealerHand))
        printCards(dealerHand)
    else:
        print('DEALER: ???')
        # Hide the dealer's first card:
        printCards([BACKSIDE] + dealerHand[1:])

    # Show the player's cards:
    print('PLAYER:', getCardValue(playerHand))
    printCards(playerHand)


def pause():
    input('Press Enter to continue...')
    print('\n\n')


def getMove(playerHand, money):
    while True: # Keep looping until the player enters a correct move.
        # Determine what moves the player can make:
        moves = ['(H)it', '(S)tand'] # The player can always hit or stand.

        # The player can double down on their first move, which we can
        # tell because they'll have exactly two cards:
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get the player's move:
        movePrompt = ', '.join(moves) + ': '
        move = input(movePrompt).upper()
        if move in ('H', 'S') or (move == 'D' and '(D)ouble down' in moves):
            return move # Player has entered a valid move.


# Main game:
print('BLACKJACK')
print()
print('Rules:')
print('Try to get as close to 21 without going over.')
print('Kings, Queens, and Jacks are worth 10 points.')
print('Aces are worth 1 or 11 points.')
print('2 through 10 are worth their face value.')
print('(H)it to take another card.')
print('(S)tand to stop taking cards.')
print('On your first play, you can (D)ouble down to double up to your bet')
print('but must hit exactly one more time before standing.')
print('In case of a tie, the pot carries over to the next round.')
print('Dealer stops hitting themselves at 17.')
print()



money = 100
pot = 0
while True: # Main game loop.
    # Check if the player has run out of money:
    if money <= 0:
        print("You've run out of money!")
        sys.exit()

    # Let the player enter their bet for this round:
    print('Money:', money)
    bet = getBet(money)

    # Set up the pot and deal the cards:
    pot += bet * 2 # Dealer matches the player's bet.
    money -= bet
    deck = getDeck()
    dealerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]

    # Handle player actions:
    print('Pot:', pot)
    while True:
        showHands(playerHand, dealerHand, False)
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
            pot += additionalBet * 2 # Dealer matches the increased bet.
            bet += additionalBet
            print('Bet increased by %s to %s.' % (additionalBet, bet))
            print('Pot:', pot)

        if move in ('H', 'D'):
            # Hit: take another card. (Doubling down also takes a card.)
            newCard = deck.pop()
            rank, suit = newCard
            print('You drew a %s of %s.' % (rank, suit))
            playerHand.append(newCard)

            if getCardValue(playerHand) > 21:
                # The player has busted:
                continue

        if move in ('S', 'D'):
            # Stand: stop playing this hand and let dealer draw cards.
            # (Doubling down also causes the dealer to begin drawing.)
            break

    # Handle the dealer's actions:
    if getCardValue(playerHand) <= 21:
        while getCardValue(dealerHand) < 17:
            # The dealer hits:
            print('Dealer hits...')
            dealerHand.append(deck.pop())
            showHands(playerHand, dealerHand, False)

            if getCardValue(dealerHand) > 21:
                break # The dealer has busted.
            pause()

    showHands(playerHand, dealerHand, True) # Show the final hands.

    # Handle whether the player won, lost, or tied.
    if getCardValue(dealerHand) > 21:
        print('Dealer busts! You win $%s!' % (pot))
        money += pot
        pot = 0 # Reset the pot.
    elif (getCardValue(playerHand) > 21) or (getCardValue(playerHand) < getCardValue(dealerHand)):
        print('You lost!')
        pot = 0 # Reset the pot.
    elif getCardValue(playerHand) > getCardValue(dealerHand):
        print('You won $%s!' % (pot))
        money += pot
        pot = 0 # Reset the pot.
    elif getCardValue(playerHand) == getCardValue(dealerHand):
        print('Tie! Pot carries over to the next round.')
    else:
        assert False

    pause()
