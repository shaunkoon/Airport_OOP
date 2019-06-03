from run_examples import *
import gc


def list_of_flight_num():  # Returns flight numbers in a list
    flight_list = []
    for obj in gc.get_objects():
        if isinstance(obj, Flight_Trip):
            flight_list.append(obj.flightnum)
    return flight_list


def available_flights():  # Returns all flights and their details
    print('Here are all the available flights:')
    for obj in gc.get_objects():
        if isinstance(obj, Flight_Trip):
            print("-",obj.flightnum, 'From', obj.origin, 'to', obj.destination)
#
#
# def which_flight():  # Asks which flight do you want
#     flight_num_not_provided = True
#     while flight_num_not_provided:
#         flight = input('What is the flight number of the flight that you would like to take?')
#         if flight in list_of_flight_num():
#             flight_num_not_provided = False
#         else:
#             print('Sorry that is not a valid flight number. Please try again.')
#     print(f"Great! We'll book you on flight {flight}. We just need some of your details")
#     print(passenger_details())
#     print(flight)
#
#
# def passenger_details():  # Gathers passenger details
#     name = input("What is your name?").title
#     ppnum = input(f"What is your passport number, {name}?")
#     nationality = input("What is your nationality?")
#     print("Awesome! Just check all your details are correct then we will add you to the flight")
#     print("Name:", name)
#     print("Passport Number:", ppnum)
#     print("Nationality:", nationality)






unfinished = True
while unfinished:
    book_ques = input('Hi there! Would you like to book a flight? ')
    if book_ques.lower() == 'yes':
        details_incomplete = True
        while details_incomplete:
            print('____________________')
            available_flights()
            flight_num_not_provided = True
            while flight_num_not_provided:
                flight = input('What is the flight number of the flight that you would like to take? ')
                print('____________________')
                if flight in list_of_flight_num():
                    flight_num_not_provided = False
                else:
                    print('Sorry that is not a valid flight number. Please try again.')
            print(f"Great! We'll book you on flight {flight}. We just need some of your details")
            name = input("What is your name? ").title()
            ppnum = input(f"What is your passport number, {name}? ")
            nationality = input("What is your nationality? ").title()
            print('____________________')
            print("Awesome! Just check all your details are correct then we will add you to the flight")
            print("Name:", name)
            print("Passport Number:", ppnum)
            print("Nationality:", nationality)
            print("Flight:", flight)
            print(f'From: {eval(flight).origin}')
            print(f"To: {eval(flight).destination}")
            invalid_input = True
            while invalid_input:
                correct = input('Are your details correct?')
                if correct.lower() == 'yes':
                    invalid_input = False
                    details_incomplete = False
                elif correct.lower() == 'no':
                    print("Oh no! Let's try again")
                    invalid_input = False
                else:
                    print('Error! Please answer yes or no.')
        # add passenger
        passenger = Passenger(name, ppnum, nationality)
        eval(flight).add_passenger(passenger)
        print("You've been added to the flight! Enjoy your trip")

        unfinished = False
    elif book_ques.lower() == 'no':
            unfinished = False
    else:
        print('Error, please try again with yes or no.')
print('Ok baiiii!')


# Check that passenger is added
# for person in eval(flight).passenger_list:
#    print(person.name)
