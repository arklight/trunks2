# number of cars
cars = 100
# how big the car is
space_in_a_car = 4
# number of drivers
drivers = 30
# number of passengers
passengers = 90
# not used cars
cars_not_driven = cars - drivers
# used cars
cars_driven = drivers
# group members in carpool
carpool_capacity = cars_driven * space_in_a_car
# avg pass per cars
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
