from abc import abstractmethod, ABC

class Band(ABC):

    squad = []

    def __init__(self, name, members, sound):
        self.name = name
        self.members = members
        self.sound = sound
        Band.squad.append(self)

    def play_solos(self):
        musicSolo = []

        for x in self.members:
            musicSolo.append(x.play_solo())
        return musicSolo

    def play_sound(self):
        return self.sound

    def __str__(self):

        return '{} members are {}. the sound: {}!'.format(self.name, self.members, self.sound)

    def __repr__(self):

        return f'{self.name} members are {self.members}. the sound: {self.sound}'

    @classmethod
    def to_list(cls):

        return cls.squad

###########################################  

class Musician(ABC):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @staticmethod
    def play_solo():
        pass

    @staticmethod
    def get_instrument():
        pass
 ###########################################  
class Bassist(Musician):

    def __init__(self, name, instrument):
        self.instrument = instrument
        super().__init__(name)

    def __repr__(self):
        return self.name

    def play_solo(self):
        return "dan dan dan"

    def get_instrument(self):
        return 'dan'

###########################################  
class Drummer(Musician):

    def play_solo(self):
        return "bummm bummm"

    def get_instrument(self):
        return "Drum"

###########################################  
class Guitarist(Musician):

    def play_solo(self):
        return "tram tram tram"

    def get_instrument(self):
        return "Guitar"

###########################################  
if __name__ == "__main__":
    
    omar = Musician("omar")
    print(f'this is me {omar} the band leader')
    print(f'my instrument is >>{omar.get_instrument()}<< no instrument for me lol')
    print(f'my sound is {omar.play_solo()} because iam in the silent mode :p')
    print("")
    Charlie_Adams = Drummer("Charlie_Adams")
    print(f'this is {Charlie_Adams} the drummer')
    print(f'my instrument is >>{Charlie_Adams.get_instrument()}<<')
    print(f'my sound is {Charlie_Adams.play_solo()} ooohh yeaaah')
    print("")
    Yiannis_Chryssomallis = Guitarist("Yiannis Chryssomallis")
    print(f'this is me {Yiannis_Chryssomallis} the Guitarist')
    print(f'my instrument is >>{Yiannis_Chryssomallis.get_instrument()}<< daaaaang')
    print(f'my sound is {Yiannis_Chryssomallis.play_solo()} enjoy my music')

    #######################################