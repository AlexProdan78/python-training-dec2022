import unittest
from datetime import date

from oop import Person


class TestCreatePerson(unittest.TestCase):
    def test_create_person_valid_date_of_birth(self):
        valid_date = date(1980, 1, 2)
        person = Person("Ion", valid_date)
        self.assertEqual(person.date_of_birth, valid_date)

    def test_create_person_invalid_date_of_birth(self):
        invalid_date = date(1949, 1, 2)
        with self.assertRaises(ValueError):
            Person("Ion", invalid_date)


class TestUpdatePerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("Ion", date(1980, 1, 2))

    def test_person_set_valid_date_of_birth(self):
        valid_date = date(1952, 4, 22)
        self.person.date_of_birth = valid_date
        self.assertEqual(self.person.date_of_birth, valid_date)

    def test_person_set_invalid_date_of_birth(self):
        initial_date = self.person.date_of_birth

        with self.assertRaises(ValueError):
            self.person.date_of_birth = date(1942, 4, 22)

        self.assertEqual(self.person.date_of_birth, initial_date)
