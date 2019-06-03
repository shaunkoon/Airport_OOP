class Passenger:
    def __init__(self, name, ppnum, nationality = ''):
        self.name = name
        self.ppnum = ppnum
        self.nationality = nationality

    def talk(self):
        return 'Can I have the chicken please!!'

