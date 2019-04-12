# Blackjack, by Al Sweigart al@inventwithpython.com

# STILL IN PROGRESS

import random, sys

# Setup constants:
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'

"""
('8', '♥')
-----
|8  |
| ♥ |
|  8|
-----

"""
def printCards(cards):
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += '----- '
        if card == BACKSIDE:
            # Print a card's back
            for i in range(1, 4):
                rows[i] += '|###| '
        else:
            # Print the card's front.
            rank, suit = card
            rows[1] += '|%s | ' % (rank.ljust(2))
            rows[2] += '| %s | ' % (suit)
            rows[3] += '| %s| ' % (rank.rjust(2))
        rows[4] += '----- '

    for i in range(5):
        print(rows[i])


def getCardValue(cards):
    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards:
    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    # Add the value for the aces:
    for i in range(numberOfAces):
        if 21 - value <= 11:
            value += 11
        else:
            value += 1

    return value


def getDeck():
    # Create a deck of all 52 cards.
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def getBet(maxBet):
    while True:
        print('How much do you bet? (1-%s, or "quit")' % (maxBet))
        bet = input().upper()
        if bet == 'QUIT':
            sys.exit('Thanks for playing!')
        try:
            bet = int(bet)
        except ValueError:
            pass # If the player didn't enter a number, just ask again.
        if (1 <= bet <= maxBet):
            break

    return bet


def showCards(playerHand, dealerHand, showDealerHand):
    if showDealerHand:
        print('DEALER:', getCardValue(dealerHand))
        printCards(dealerHand)
    else:
        print('DEALER:')
        printCards([BACKSIDE] + dealerHand[1:])
    print('PLAYER:', getCardValue(playerHand))
    printCards(playerHand)


def pause():
    input('Press Enter to continue...')
    print('\n\n')

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
print('Dealer stops hitting at 17.')
print()



money = 100
pot = 0
while True: # Main game loop.
    # Check if the player has run out of money:
    if money <= 0:
        sys.exit("You've run out of money!")

    print('Money:', money)
    bet = getBet(money)

    pot += bet
    money -= bet
    deck = getDeck()
    dealerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]

    # Play a round:
    results = ''
    while True: # Round loop.
        print('Pot:', pot)
        showCards(playerHand, dealerHand, False)
        print()

        # Check if the player has bust:
        if getCardValue(playerHand) > 21:
            print('Bust!')
            results = 'lost'
            break

        while True:
            # Get the player's move:
            moves = ['(H)it', '(S)tand']
            if len(playerHand) == 2 and money > 0:
                moves.append('(D)ouble down')

            move = input(', '.join(moves) + ': ').upper()
            if move in ('H', 'S') or (move == 'D' and '(D)ouble down' in moves):
                break # Player has entered a valid move.
        #breakpoint()
        if move == 'D':
            # Double down:
            doubleBet = min(bet, money)
            money -= doubleBet
            pot += doubleBet
            print('Your bet increased by %s to a total pot of %s.' % (doubleBet, pot))

        if move in ('H', 'D'):
            # Hit: take another card. (Doubling down also takes a card.)
            newCard = deck.pop()
            #print('You drew a %s of %s.' % (newCard[0], newCard[1]))
            playerHand.append(newCard)

            if getCardValue(playerHand) > 21:
                #showCards(playerHand, dealerHand, False)
                continue # Player has busted.

        if move in ('S', 'D'):
            # Stand: stop playing this hand and let dealer draw cards.
            # (Doubling down also causes the dealer to begin drawing.)
            while getCardValue(dealerHand) < 17:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                showCards(playerHand, dealerHand, True)

                if getCardValue(dealerHand) > 21:
                    print('Dealer busts! You win $%s!' % (pot))
                    results = 'won'
                    pause()
                    break
                pause()

            if getCardValue(playerHand) == getCardValue(dealerHand):
                print('Tie! Pot carries over to the next round.')
                results = 'tie'
                pause()
                break
            elif getCardValue(playerHand) > getCardValue(dealerHand):
                print('You won $%s!' % (pot))
                pause()
                break
            if results != '':
                break


    if results == 'won':
        money += pot * 2
    elif results == 'lost':
        pass
    elif results == 'tie':
        pass
    pot = 0








