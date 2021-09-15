"""Blackjack (barebones version)
by Al Sweigart al@inventwithpython.com
The classic card game also known as 21."""
import random

HEARTS   = chr(9829)
DIAMONDS = chr(9830)
SPADES   = chr(9824)
CLUBS    = chr(9827)


def main():
    print('Blackjack (barebones version)')
    print('by Al Sweigart al@inventwithpython.com')

    # Create the deck of cards:
    deck = []
    for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
        for suit in [HEARTS, DIAMONDS, SPADES, CLUBS]:
            deck.append([rank, suit])
    random.shuffle(deck)

    # Give the dealer and player two cards each:
    dealerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]

    # Handle player actions:
    while True:  # Keep looping until player stands or busts.
        displayHands(playerHand, [['??', '?']] + dealerHand[1:])
        print()

        if getHandValue(playerHand) > 21:
            break  # Player has busted.

        # Get the player's move, either 'H' or 'S':
        move = input('H or S > ').upper()

        if move == 'H':
            # Hit/doubling down takes another card.
            newCard = deck.pop()
            print('You drew a', newCard[0], 'of', newCard[1])
            playerHand.append(newCard)

            if getHandValue(playerHand) > 21:
                continue  # The player has busted.
        elif move == 'S':
            break  # Standing stops the player's turn.

    # Handle the dealer's actions:
    if getHandValue(playerHand) <= 21:
        while getHandValue(dealerHand) < 17:
            print('Dealer hits...')
            dealerHand.append(deck.pop())
            displayHands(playerHand, [['??', '?']] + dealerHand[1:])

            if getHandValue(dealerHand) > 21:
                break  # The dealer has busted.
            input('Press Enter to continue...\n\n')

    # Show the final hands:
    displayHands(playerHand, dealerHand)

    playerValue = getHandValue(playerHand)
    dealerValue = getHandValue(dealerHand)

    if dealerValue > 21:
        print('Dealer busts! You won!')
    elif (playerValue > 21) or (playerValue < dealerValue):
        print('You bust.')
    elif playerValue > dealerValue:
        print('You won!')
    elif playerValue == dealerValue:
        print('It is a tie.')


def displayHands(playerHand, dealerHand):
    print('DEALER:')
    displayCards(dealerHand)
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(allCards):
    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards:
    for card in allCards:
        rank = card[0]  # card is a list like [rank, suit]
        if rank == 'A':
            numberOfAces += 1  # Aces are worth at least 1.
        elif rank in ['K', 'Q', 'J']:  # Face cards are worth 10.
            value += 10
        elif rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            value += int(rank)  # Numbered cards are worth their number.

    # Add the value for the aces:
    value += numberOfAces  # Add 1 per ace.
    for i in range(numberOfAces):
        # If another 10 can be added without busting, do so:
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(allCards):
    rows = ['', '', '', '', '']  # The text to display on each row.

    for card in allCards:
        rank = card[0]
        suit = card[1]
        rows[0] += ' ___  '  # Print the top line of the card.
        rows[1] += '|{} | '.format(rank.ljust(2))
        rows[2] += '| {} | '.format(suit)
        rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # Print each row on the screen:
    for row in rows:
        print(row)


# Call the main() function to play the game:
main()
