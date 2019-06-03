class Flight_Trip:
    def __init__(self, flightnum="", origin="", destination="", planetype=""):
        self.flightnum = flightnum
        self.origin = origin
        self.destination = destination
        self.plane = planetype
        self.passenger_list = []

    def add_passenger(self, passenger):
        self.passenger_list.append(passenger)
        return f'{passenger} added to flight!'

    def set_plane(self, planetype):
        self.plane = planetype
        return f'Your plane is {planetype}'

