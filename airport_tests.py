from passengers_class import *
from planes_class import *
from flight_trip_class import *
from planes_class import *
import pytest


# As a user I can create a Passenger

def test_create_passenger():
    test = Passenger('test_name', 'test_passport_num')
    assert isinstance(test, Passenger)

# As a user I can create a Passenger with name and passport number
# I can create 'Joana Thomson' with the Passport number 'B343123'

def test_joana_passenger():
    joana = Passenger('Joana Thomson', 'B343123')
    assert joana.name == 'Joana Thomson', joana.ppnum == 'B343123'

# I can create 'Birt Kuman' with the Passport number 'B13927'

def test_birt_passenger():
    birt = Passenger('Birt Kuman', 'B13927')
    assert birt.name == 'Birt Kuman', birt.ppnum == 'B13927'

# If I try to create a user with out a name or a passport number I get an error

def test_error_without_details():
    with pytest.raises(Exception):
        Passenger()

# As a User I can create a Plane with a plane number

def test_create_plane_with_num():
    test = Planes(5678)
    assert test.planenum == 5678


# As a user I can create a flight with no specific information

def test_create_flight():
    test = Flight_Trip()
    assert test

# As a user I can add a plane

def test_add_plane():
    test_plane = Planes(planetype="Boeing 737")
    test_flight = Flight_Trip()
    test_flight.set_plane(test_plane)
    assert test_plane == test_flight.plane

# As a User I can add a destination

def test_add_destination():
    test = Flight_Trip(destination="Australia")
    assert test.destination == "Australia"

# As a user I can add a origin

def test_add_origin():
    test = Flight_Trip(origin="Chad")
    assert test.origin == "Chad"

# As a user I can add a Passenger to the list of passengers

def test_add_passenger():
    test_passenger = Passenger("name", "passport number")
    test_flight = Flight_Trip()
    test_flight.add_passenger(test_passenger)
    assert test_passenger in test_flight.passenger_list





