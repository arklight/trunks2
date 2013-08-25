#!/usr/bin/env python
"""Define a Die, Dice and CrapsDice."""
__author__ = 'Brandon'

import random


class Die(object):
    """Simulate a 6-sided die."""
    def __init__(self):
        self.domain = range(1, 7)

    def roll(self):
        self.value = random.choice(self.domain)
        return self.value

    def getValue(self):
        print self.value
        return self.value


class Dice(object):
    """Simulate a pair of dice."""

    def __init__(self):
        """Create the two Die objects."""
        self.myDice = (Die(), Die())

    def roll(self):
        """Return a random roll of the dice."""
        for d in self.myDice:
            d.roll()

    def getTotal(self):
        """Return the total of two dice."""
        return self.myDice[0].value + self.myDice[1].value

    def getTuple(self):
        """Return a tuple of the dice."""
        return self.myDice


class CrapsDice(Dice):
    """Extends Dice to add features specific to Craps."""
    def hard_ways(self):
        """Returns True if this was a hard_ways roll?"""
        return self.myDice[0].value == self.myDice[1].value

    def isPoint(self, value):
        """Returns True if this roll has the given total"""
        return self.getTotal() == value

