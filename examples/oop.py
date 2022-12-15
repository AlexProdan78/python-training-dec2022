from datetime import date


class Person:
    count = 0  # class attribute

    def __init__(self, name, date_of_birth):
        self.name = name  # instance attributes
        self.date_of_birth = date_of_birth
        self.increment_count()

    def greet(self, greeting):  # instance method
        print(f"{greeting.capitalize()}! I'm {self.name}.")

    @classmethod
    def increment_count(cls):  # class method
        cls.count += 1

    @staticmethod
    def compute_age(date_of_birth):  # static method
        timediff = date.today() - date_of_birth
        return int(timediff.days / 365.25)

    def __str__(self):
        return f"{self.__class__.__name__} instance with name={self.name}"

    def __eq__(self, other):
        return self.date_of_birth == other.date_of_birth

    def __lt__(self, other):
        return self.date_of_birth > other.date_of_birth


if __name__ == "__main__":
    p1 = Person("Ana", date(2000, 10, 12))
    p2 = Person("George", date(1992, 4, 1))

    # Changing attributes
    # Person.count += 1
    p1.name = "Maia"

    print(p1.name, p2.name, p1.name is p2.name)
    print(Person.count, p1.count is p2.count, p1.count is Person.count)

    p1.greet("hello")
    Person.greet(p1, "good morning")  # calling instance method from class
    p2.greet("hi")

    print(p1)
    print(str(p2))

    print('Persons are identical:', p1 is p2)
    print('Persons have the same age:', p1 == p2)
    print(f'{p1.name} is younger than {p2.name}:', p1 < p2)

    print("Persons created:", Person.count)

    print(f"{p1.name}'s age:", Person.compute_age(p1.date_of_birth))
