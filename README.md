
## OOPS Concepts Demonstrated in `vivek_oops101.py`

The file [`vivek_oops101.py`](vivek_oops101.py) is a comprehensive example of Object-Oriented Programming (OOPS) concepts in Python. Here’s a detailed breakdown for learners:

### 1. Class and Object

- **Class**: A blueprint for creating objects (instances). Defines attributes and methods.
- **Object**: An instance of a class with actual values.
- **In the code**:  
  - `Person` and `Student` are classes.
  - `person1 = Person("Ravi", 35)` creates an object.

---

### 2. Encapsulation

- **Definition**: Bundles data and the methods that operate on that data. Restricts direct access to some of the object’s components.
- **Access Levels**:  
  - Public: `self.name` (accessible everywhere)
  - Protected: `self._country` (convention: internal use, still accessible)
  - Private: `self.__age` (name-mangled, not easily accessible)
- **Getter/Setter**: Controlled access via `@property` and `@age.setter`.
- **Example**:  
  ```python
  @property
  def age(self):
      return self.__age

  @age.setter
  def age(self, value):
      ...
  ```

---

### 3. Inheritance

- **Definition**: A class (child) inherits attributes and methods from another (parent).
- **In the code**:  
  - `class Student(Person):` means `Student` inherits from `Person`.
  - `super().__init__(name, age)` calls the parent’s constructor.

---

### 4. Polymorphism

- **Definition**: Different classes can define methods with the same name, offering different implementations.
- **In the code**:  
  - `Student` overrides `introduce()` from `Person`.  
  - Calls `super().introduce()` to include base class behavior, then adds its own.

---

### 5. Abstraction

- **Definition**: Hides internal complexity, exposing only necessary parts.
- **In the code**:  
  - Methods like `introduce()`, `species_info()`, and `school_name()` provide simple interfaces.

---

### 6. Class Methods and Static Methods

- **Class Method (`@classmethod`)**: Works at the class level, can change class variables or provide alternate constructors.
  - Example: `change_species`, `from_string`
- **Static Method (`@staticmethod`)**: Utility function, does not access class or instance data.
  - Example: `species_info`, `school_name`

---

### 7. Decorators

- **Definition**: Functions that modify the behavior of other functions or methods.
- **In the code**:  
  - `@log_call` decorator prints a message every time the decorated method is called.

---

### 8. Super() Usage

- **Definition**: Calls a method from the parent class, ensuring base class initialization or behavior is included.
- **In the code**:  
  - `super().__init__(...)` in `Student`.
  - `super().introduce()` in overridden methods.

---

### 9. Alternative Constructors

- **Definition**: Additional ways to create objects, often using `@classmethod`.
- **In the code**:  
  - `from_string` lets you create a `Person` from a string:  
    `person2 = Person.from_string("Seema, 28")`

---

### Summary Table

| Concept                 | Example in Code                                     |
|-------------------------|----------------------------------------------------|
| Class/Object            | `Person`, `Student`, `person1 = Person(...)`       |
| Encapsulation           | `self.name`, `self._country`, `self.__age`, getter/setter |
| Inheritance             | `class Student(Person)`                            |
| Polymorphism            | Overriding `introduce` in `Student`                |
| Abstraction             | Methods: `introduce`, `species_info`               |
| Class Method            | `@classmethod change_species`, `from_string`        |
| Static Method           | `@staticmethod species_info`, `school_name`         |
| Decorator               | `@log_call`                                        |
| super()                 | `super().__init__()`, `super().introduce()`        |
| Alternative Constructor | `from_string` class method                         |

---

### Try It Yourself

The second half of `vivek_oops101.py` contains sample code that creates objects, calls methods, and demonstrates each of these OOPS principles. Run the script and observe the output for practical understanding.

---

**Refer to [`vivek_oops101.py`](vivek_oops101.py) for actual Python code examples and demonstrations of each concept.**

---

Would you like help committing this update to your repository, or do you need a step-by-step guide on how to add it via the GitHub web interface?
