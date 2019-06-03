from aircraft_class import *
from planes_class import *
from passengers_class import *
from flight_trip_class import *
import gc


############## Create passengers ##############

shaun = Passenger('Shaun', 123, 'British')
# print(shaun.name)
# print(shaun.talk())
# print('-----------')


############## Create planes ##############

boeing = Planes('Boeing 737')
# print(boeing.planetype)
# print(boeing.glide())
# print('-----------')

airbus = Planes('Airbus A300')
# print(airbus.planetype)
# print(airbus.airtime())
# print('-----------')

############## Create Flight Trips ##############

SGA101 = Flight_Trip('SGA101', 'London', 'Singapore')
# print(SGA101.flightnum)
# print(SGA101.destination)

AA345 = Flight_Trip('AA345', 'Birmingham', 'Atlantis')
# print(AA345.flightnum)
# print(AA345.destination)
# print('----------')


############## Set plane ##############

SGA101.set_plane(boeing)
# print(SGA101.plane.planetype)

AA345.set_plane(airbus)
# print(AA345.plane.planetype)
# print('-----------')

############## Extra Flight ##############

# BA999 = Flight_Trip('BA999', 'Heathrow','Gatwick')

############## List existing flight_trips ##############

# print('Lists of flight trips:')
# for obj in gc.get_objects():
#     if isinstance(obj, Flight_Trip):
#         print(obj.flightnum, 'From', obj.origin, 'to', obj.destination)
#
# print('-----------')

############## Add a passenger to a flight_trip ##############

# SGA101.add_passenger(shaun)
# print('Passenger list:')
# for person in SGA101.passenger_list:
#     print(person.name)

