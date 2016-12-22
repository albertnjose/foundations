# procedural method for blackjack
from random import shuffle
import itertools


def sumPoints(playerCards):
    # function to show the points of hand
    total = 0
    for (suit, value) in playerCards:
        if value == 'Ace':
            total += 11
        elif value in ['Jack', 'Queen', 'King']:
            total += 10
        else:
            total += int(value)
    
    aces = sum(card.count('Ace') for card in playerCards)
    
    while total > 21 and aces:
        total += 10
        aces += 1
    
    return total
    

# use loop to create deck with suits and rank, total of 52
print("Welcome to Blackjack!")
suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
rank = ['2', '3','4','5','6','7','8','9','10', 'Jack', 'Queen', 'King', 'Ace']     

deck = list(itertools.product(suits, rank))
    
shuffle(deck)
    

# create player and dealer hands

dealer_cards = []
player_cards = []
dealer_cards.append(deck.pop())
player_cards.append(deck.pop())
dealer_cards.append(deck.pop())
player_cards.append(deck.pop())

dealerPoints = sumPoints(dealer_cards)
playerPoints = sumPoints(player_cards)


# start the game

print ("Dealer's cards:")
print (dealer_cards[0])
print ("Player's cards:")
print (player_cards)
    
if(playerPoints == 21 and dealerPoints == 21):
    print ("Push. Dealer wins.")
    exit()
elif(playerPoints == 21):
    print ("Blackjack! Player wins!")
    exit()
elif(dealerPoints == 21):
    print ("Dealer has blackjack. Player loses!")
    exit()

# Player logic
while playerPoints < 21:
    game = int(input('Hit: 1 or Stay: 2?'))
    
    if(game not in [1, 2]):
        print("Please input 1 or 2.")
        continue
    elif(game == 2):
        print("Player stays.")
        break
    else:
        new_card = deck.pop()
        player_cards.append(new_card)
        playerPoints = sumPoints(player_cards)
        print("You added: " + str(new_card))
        print("New total: " + str(playerPoints))
        
        if(playerPoints == 21):
            print("Blackjack! Player wins.")
            exit()
        elif(playerPoints > 21):
            print("Bust! Player loses!")
            exit()
        else:
            continue


# dealer logic

while dealerPoints < 17:
    new_card = deck.pop()
    dealer_cards.append(new_card)
    dealerPoints = sumPoints(dealer_cards)
    print("Dealer added: " + str(new_card))
    print("Dealer's new total: " + str(dealerPoints))
    
    if(dealerPoints == 21):
        print("Dealer hits blackjack. Player loses!")
        exit()
    elif(dealerPoints > 21):
        print("Dealer busts. Player wins!")
        exit()
    else:
        continue

# compare dealer and player cards

print("Dealer's cards: " + str(dealer_cards))

print("Player's cards: " + str(player_cards))

if(dealerPoints > playerPoints):
    print("Player has: " + str(playerPoints))
    print("Dealer wins with " + str(dealerPoints))
elif(playerPoints > dealerPoints):
    print("Dealer has: " + str(dealerPoints))
    print("Player wins with " + str(playerPoints))
else:
    print("Tie!")
    
exit()
