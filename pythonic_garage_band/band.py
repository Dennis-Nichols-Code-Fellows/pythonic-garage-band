class Band:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def __str__(self):
        return f'Band: {self.name}, Members: {", ".join(self.members)}'

    def __repr__(self):
        return f'<Band class. Name: {self.name}, Members: {self.members}>'

    def play_solos(self):
        return [member.play_solo() for member in self.members]


class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    def get_instrument(self):
        return self.instrument


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, instrument='guitar')

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, instrument='bass')

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, instrument='drums')

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    def play_solo(self):
        return "rattle boom crash"
