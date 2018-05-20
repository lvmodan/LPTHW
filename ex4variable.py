#!/usr/bin/env python
# coding=utf-8
#define how many cars
cars = 100
#define the space of a car
space_in_a_car = 4.0
drivers = 30
passengers = 90
#caculate how many cars are not driven
cars_not_driven = cars - drivers
cars_driven = drivers
#caculate the car pool
carpool_capacity = cars_driven * space_in_a_car
#caculate the average passengers each car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to car pool today."
print "We need to put about", average_passengers_per_car, "in each car."
