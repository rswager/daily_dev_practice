import random
from loguru import logger as log


class Person:
    def __init__(self, name_in):
        self.name: str = name_in
        self._trust:int  = 0
        self._relieved: bool = True
        self._is_vulnerable: bool = False
        self._is_receptive: bool = False
        self._trusted_person: list[Person] = []

    @property
    def trust(self):
        return self._trust

    @trust.setter
    def trust(self,value):
        self._trust = value
        if self._trust:
            log.info(f'{self.name}: {self.name} has trust')


    @property
    def relieved(self):
        return self._relieved

    @relieved.setter
    def relieved(self, value):
        self._relieved = value
        if self._relieved:
            log.info(f'{self.name}:{self.name} is relieved')

    @property
    def is_vulnerable(self):
        return self._is_vulnerable

    @is_vulnerable.setter
    def is_vulnerable(self, value):
        self._is_vulnerable = value
        if self._is_vulnerable:
            log.info(f'{self.name}: {self.name} is vulnerable')

    @property
    def is_receptive(self):
        return self._is_receptive

    @is_receptive.setter
    def is_receptive(self, value):
        self._is_receptive = value
        if self._is_receptive:
            log.info(f'{self.name}: {self.name} is receptive')

    @property
    def trusted_person(self):
        return self._trusted_person

    @trusted_person.setter
    def trusted_person(self,person_in):
        if person_in not in self._trusted_person:
            log.info(f'{self.name}: adding trusted person {person_in.name}')
            self._trusted_person.append(person_in)
            person_in.process_receiving_trust(self.name)


    def process_vulnerability(self, receiving_person):
        if self.is_vulnerable:
            log.info(f'{self.name}: Vulnerable with {receiving_person.name}')
            if receiving_person.is_receptive:
                log.info(f'{self.name}: {receiving_person.name} was Receptive')

                self.trust+=10
                self.relieved=True
                self.trusted_person = receiving_person
            else:
                log.warning(f'{self.name}: {receiving_person.name} wasn\'t receptive :(')
        else:
            log.warning(f'{self.name}: {self.name} wasn\'t vulnerable')

    def process_receiving_trust(self, received_from:str):
        log.info(f'{self.name}: Received Trust from {received_from}')
        self.relieved = True
        self.trust += 10

class RealOne(Person):
    def __init__(self,name_in):
        super().__init__(name_in)
        self.humor_list: list[str] = ['I C++ what you did there',
                                      '404: Joke not found.',
                                      'I tried to catch some exceptions… but they escaped.',
                                      'Trust level increased by 10 points. Achievement unlocked: \'Emotional Debugger\'.',
                                      'Initializing empathy.exe...',
                                      'Debugging emotions with print statements.'
                                      ]

    def mild_humor(self):
        log.info(f'{self.name}: {random.choice(self.humor_list)}')

    def process_receiving_trust(self,received_from:str):
        log.info(f'{self.name}: Received Trust from {received_from}')
        self.relieved = True
        self.trust += 10
        self.mild_humor()

if __name__ == '__main__':
    sam_exe = Person('Sam of the Antha')
    robbie_exe = RealOne('THE Real One')

    sam_exe.is_vulnerable=True
    robbie_exe.is_receptive=True
    sam_exe.process_vulnerability(robbie_exe)
