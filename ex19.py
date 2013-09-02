def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "OR, we can use variables from out script:"
amount_of_cheese = 10
amount_of_crackers = 50

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def money_and_monkeys(money, monkeys):
    print "You have %d amount of money!" % money
    print "You have %d amount of monkeys!" % monkeys

money_and_monkeys(5, 10)
money_and_monkeys(1, 1)
more_money = 100
more_monkeys = 5
money_and_monkeys(more_money * 5, more_monkeys * 2)