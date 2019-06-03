from passengers_class import *
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

# As a user I can add a plane

# As a User I can add a destination

# As a user I can add a origin

# As a user I can add a Passenger to the list of passengers

# Passenger list is a list of objct that are Passenger




# print('Lists of flight trips:')
# for obj in gc.get_objects():
#     if isinstance(obj, Flight_Trip):
#         print(obj.flightnum, 'From', obj.origin, 'to', obj.destination)
#
# def test_create_passenger():
#     assert create_passenger('Joana Thomson', 'B343123', 'British')
