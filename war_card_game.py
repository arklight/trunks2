#!/usr/bin/env python
# the card game war
import random
from random import choice

value = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
deck = value * 4
random.shuffle(deck)


def card_face_value():
    card_face = choice(value)
    return card_face


def deal(num_user):
#    hands = [[] * num_user]
    cards_per_hand = len(deck) / num_user
    return deck[:cards_per_hand], deck[cards_per_hand:]


# def game_play_war():


def main():
# pick user to go first
    hands = deal(2)
    for hand in hands:
        user_hand = random.randrange(len(hand))
    return user_hand.pop(hand)

#    print hands
#    print len(hands[0])
#    print len(hands[1])

if __name__ == '__main__':
    main()