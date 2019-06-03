from run_examples import *
from interactive import *


unfinished = True
while unfinished:
    book_ques = input('Hi there! Would you like to book a flight?')
    if book_ques == 'yes':
        details_incomplete = True
        while details_incomplete:
            available_flights()
            which_flight()
            invalid_input = True
            while invalid_input:
                correct = input('Are your details correct?')
                if correct == 'yes':
                    invalid_input = False
                    details_incomplete = False
                elif correct == 'no':
                    print("Oh no! Let's try again")
                    invalid_input = False
                else:
                    print('Error! Please answer yes or no.')

        # add passenger
        shaun = Passenger('Shaun', 123, 'British')
        SGA_101.add_passenger(shaun)

    elif book_ques == 'no':
            unfinished = False
    else:
        print('Error, please try again with yes or no.')
print('Ok baiiii!')