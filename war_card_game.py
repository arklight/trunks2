#!/usr/bin/env python
# the card game war
import random
from random import choice

card_faces = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
# values of the elements
# build dict for this and map values to them


#spade heart diamond clubs
deck = card_faces * 4
random.shuffle(deck)


def deal_cards(num_user):
#    hands = [[] * num_user]
    cards_per_hand = len(deck) / num_user
    return deck[:cards_per_hand], deck[cards_per_hand:]


def split_hands(hands):
#split the deck to each players hands
    player1_hand, player2_hand = hands[0], hands[1]
    return player1_hand, player2_hand


def play(split_hands):

    for player in split_hands:
        if card >= card


def main():
# pick user to go first
    hands = deal_cards(2)
    split_hands(hands)




#        hand = randrange(0, len(users))
#        print users[hand]
#        return users[hand]
#    for user in users:
#        choice(user)
#        return hand

#    print hands
#    print len(hands[0])
#    print len(hands[1])

if __name__ == '__main__':
    main()