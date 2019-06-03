from aircraft_class import *
from planes_class import *
from passengers_class import *
from flight_trip_class import *
from run_examples import *
import gc


def list_of_flight_num():   # Returns flight numbers in a list
    flight_list = []
    for obj in gc.get_objects():
        if isinstance(obj, Flight_Trip):
            flight_list.append(obj.flightnum)
    return flight_list


def available_flights():    # Returns all flights and their details
    print('Here are all the available flights:')
    for obj in gc.get_objects():
        if isinstance(obj, Flight_Trip):
            print(obj.flightnum, 'From', obj.origin, 'to', obj.destination)


def which_flight():         # Asks which flight do you want
    flight_num_not_provided = True
    while flight_num_not_provided:
        flight = input('What is the flight number of the flight that you would like to take?')
        if flight in list_of_flight_num():
            flight_num_not_provided = False
        else:
            print('Sorry that is not a valid flight number. Please try again.')
    print(f"Great! We'll book you on flight {flight}. We just need some of your details")
    print(passenger_details())
    print(flight)



def passenger_details():        # Gathers passenger details
    name = input("What is your name?").title
    ppnum = input(f"What is your passport number, {name}?")
    nationality = input("What is your nationality?")
    print("Awesome! Just check all your details are correct then we will add you to the flight")
    print("Name:", name)
    print("Passport Number:", ppnum)
    print("Nationality:", nationality)


