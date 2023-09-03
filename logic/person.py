class Person(object):
    """
    Class used to represent a Person
    """

    def __init__(self, id_person: int = 0, name: str = 'Name', gender: str = "gender", birthdate: str ="birthdate", vital_signs: list = None, notes: str = 'Notes', medicines: list = None):
        """ Person constructor object.

        :param id_person: id of person.
        :type id_person: int
        :param name: name of person.
        :type name: str
        :param gender: gender of person.
        :type gender: str
        :param birthdate: date of brith of person.
        :type birthdate: str
        :param vital_signs: list containing vital signs [temperature, saturation, frequency]
        :type vital_signs: list
        :param notes: evolution's notes of person.
        :type notes: str
        :returns: Person object
        :rtype: object
        """
        self._id_person = id_person
        self._name = name
        self._gender = gender
        self._birthdate = birthdate
        self._notes = notes
        self._vital_signs = vital_signs if vital_signs is not None else [0, 0, 0, 0]
        self._medicines = medicines if medicines is not None else [0, 0]

    @property
    def id_person(self) -> int:
        """ Returns id person of the person.
          :returns: id of person.
          :rtype: int
        """
        return self._id_person

    @id_person.setter
    def id_person(self, id_person: int):
        """ The id of the person.
        :param id_person: id of person.
        :type: int
        """
        self._id_person = id_person

    @property
    def name(self) -> str:
        """ Returns the full name of the person.
          :returns: name of person.
          :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """ The full name of the person.
        :param name: full name of person.
        :type: str
        """
        self._name = name

    @property
    def gender(self) -> str:
        """ Returns the gender of the person.
          :returns: gender of person.
          :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """ The gender of the person.
        :param gender: gender of person.
        :type: str
        """
        self._gender = gender

    @property
    def birthdate(self) -> str:
        """ Returns the date of brith of the person.
          :returns: birthdate of person.
          :rtype: str
        """
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate: str):
        """ The date of brith of the person.
        :param birthdate: the date of brith of person.
        :type: str
        """
        self._birthdate = birthdate

    @property
    def notes(self) -> str:
        """ Returns the evolution's notes of the person.
          :returns: evolution's notes of person.
          :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes: str):
        """ The evolution's notes of the person.
        :param notes: evolution's notes of person.
        :type: str
        """
        self._notes = notes

    @property
    def vital_signs(self) -> list:
        """ Returns vital signs [temperature, saturation, frequency] of the person.
          :returns: vital signs.
          :rtype: list
        """
        return self._vital_signs

    @vital_signs.setter
    def vital_signs(self, vital_signs: list):
        """ Set vital signs [temperature, saturation, frequency] of the person.
        :param vital_signs: vital signs [temperature, saturation, frequency].
        :type: list
        """
        self._vital_signs = vital_signs

    @property
    def medicines(self) -> list:
        """ Returns list of medicines of the person.
          :returns: medicines [medicines' name, quantity].
          :rtype: list
        """
        return self._medicines

    @medicines.setter
    def medicines(self, medicines: list):
        """ Set medicines [medicines' name, quantity] of the person.
        :param medicines: medicines [medicines' name, quantity].
        :type: list
        """
        self._medicines = medicines

    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(self.id_person, self.name, self.gender, self.birthdate, self.vital_signs, self.notes, self.medicines)


if __name__ == '__main__':
    edwin = Person(id_person=73577376, name="Edwin", gender="Puertas", birthdate="17/07/2003", vital_signs=[30, 98, 75], notes="Evolution's notes", medicines=['acetaminofen', 0])
    print(edwin)
    edwin.name = "Edwin. A"
    edwin.vital_signs = [32, 99, 80]
    print(edwin)

    juan = Person()
    print(juan)



