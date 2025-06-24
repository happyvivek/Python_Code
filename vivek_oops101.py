# Decorator Example
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Base Class: Person
class Person:
    # Class variable (shared by all instances)
    species = "Human"

    def __init__(self, name, age):
        # Public variable
        self.name = name
        # Protected variable (by convention)
        self._country = "India"
        # Private variable (name mangling)
        self.__age = age
        print(f"Person object created for {self.name}")

    # Getter for private variable
    @property
    def age(self):
        return self.__age

    # Setter with validation
    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Age must be positive")

    # Instance method
    def introduce(self):
        print(f"Hi, I'm {self.name}. I'm {self.__age} years old. I live in {self._country}.")

    # Static method
    @staticmethod
    def species_info():
        print("All persons belong to the species 'Human'.")

    # Class method to change class variable
    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species
        print(f"Species changed to {cls.species}")

    # Class method as alternative constructor
    @classmethod
    def from_string(cls, info_string):
        name, age = info_string.split(",")
        return cls(name.strip(), int(age.strip()))

# Subclass: Student
class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade
        print(f"Student object created for {self.name} with ID {self.student_id}")

    # Method override with decorator
    @log_call
    def introduce(self):
        super().introduce()
        print(f"I'm a student in grade {self.grade}. My ID is {self.student_id}.")

    # Static method for Student class
    @staticmethod
    def school_name():
        print("ABC International School")

# Testing the Code

# 1. Create Person object
print("\n--- Creating a Person ---")
person1 = Person("Ravi", 35)
person1.introduce()
print("Age (using getter):", person1.age)

# 2. Try changing age (using setter)
person1.age = 40
print("Updated Age:", person1.age)

# 3. Access private variable (not recommended directly)
print("Private age using name mangling:", person1._Person__age)

# 4. Use static method
Person.species_info()

# 5. Use class method to change species
Person.change_species("Advanced Human")

# 6. Use alternative constructor
print("\n--- Using class method as constructor ---")
person2 = Person.from_string("Seema, 28")
person2.introduce()

# 7. Create Student object (uses inheritance and super)
print("\n--- Creating a Student ---")
student1 = Student("Aryan", 15, "S123", "10th")
student1.introduce()

# 8. Use static method from Student
Student.school_name()
