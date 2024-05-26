from abc import ABC

# Define an abstract base class `Person`.
class Person(ABC):
    # Constructor for the `Person` class, which initializes `name` and `age`.
    def __init__(self, name, age):
        # Store the `name` in a protected attribute.
        self._name = name 
        # Store the `age` in a protected attribute.
        self._age = age

    # Method to get the `name`.
    def get_name(self):
        return self._name

    # Method to set the `name`.
    def set_name(self, name):
        self._name = name

    # Method to get the `age`.
    def get_age(self):
        return self._age

    # Abstract method to be implemented by subclasses for providing a description.
    def describe(self):
        pass

# Define a `Student` class that inherits from `Person`.
class Student(Person):
    # Constructor for the `Student` class, which initializes `name`, `age`, and `student_id`.
    def __init__(self, name, age, student_id):
        # Call the constructor of the base class `Person`.
        super().__init__(name, age)  
        # Store the `student_id` in a protected attribute.
        self._student_id = student_id

    # Method to get the `student_id`.
    def get_student_id(self):
        return self._student_id

    # Method to set the `student_id`.
    def set_student_id(self, student_id):
        self._student_id = student_id

    # Method to provide a description of the `Student`.
    def describe(self):
        return f"Student {self._name}, age {self._age}, ID: {self._student_id}"

# Define a `Faculty` class that inherits from `Person`.
class Faculty(Person):
    # Constructor for the `Faculty` class, which initializes `name`, `age`, and `department`.
    def __init__(self, name, age, department):
        # Call the constructor of the base class `Person`.
        super().__init__(name, age)
        # Store the `department` in a protected attribute.
        self._department = department

    # Method to get the `department`.
    def get_department(self):
        return self._department

    # Method to set the `department`.
    def set_department(self, department):
        self._department = department

    # Method to provide a description of the `Faculty`.
    def describe(self):
        return f"Faculty {self._name}, age {self._age}, Department: {self._department}"

# Define a `Staff` class that inherits from `Person`.
class Staff(Person):
    # Constructor for the `Staff` class, which initializes `name`, `age`, and `role`.
    def __init__(self, name, age, role):
        # Call the constructor of the base class `Person`.
        super().__init__(name, age)
        # Store the `role` in a protected attribute.
        self._role = role

    # Method to get the `role`.
    def get_role(self):
        return self._role

    # Method to set the `role`.
    def set_role(self, role):
        self._role = role

    # Method to provide a description of the `Staff`.
    def describe(self):
        return f"Staff {self._name}, age {self._age}, Role: {self._role}"

# Create instances of `Student`, `Faculty`, and `Staff`.
student = Student("Jose", 22, "00885-2022")
faculty = Faculty("Dr. Teresse", 50, "Computer Science")
staff = Staff("Rafael", 29, "Maintenance")

# Create a list to hold the instances of `Student`, `Faculty`, and `Staff`.
people = [student, faculty, staff]

# Iterate over the list `people`, calling the `describe` method on each element.
for person in people:
    # Print the description of each person.
    print(person.describe())
