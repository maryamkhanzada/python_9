
import streamlit as st

class Course:
    def __init__(self, title, lessons):
        self.title = title
        self.lessons = lessons  # dict of {lesson_title: content}

    def display(self):
        st.subheader(f"📘 Course: {self.title}")
        for i, (lesson, content) in enumerate(self.lessons.items()):
            with st.expander(f"📖 Lesson {i + 1}: {lesson}"):
                st.markdown(content, unsafe_allow_html=True)

    @staticmethod
    def load_sample():
        lessons = {
            "Variables": """
                ### 🧠 What are Variables?
                **Definition:**  
                Variables are symbolic names that refer to data stored in the computer's memory. Think of variables as labeled boxes where you can store information such as numbers, text, or other data types. You can then use or modify this stored information throughout your program by referring to the variable’s name.

                **Why are Variables Important?**  
                - They allow programs to store and manipulate data dynamically.
                - Enable code reuse and easier maintenance by avoiding hard-coded values.
                - Facilitate meaningful data representation by using descriptive names.

                **How Variables Work:**  
                When you create a variable, the computer allocates a space in memory to hold the value you assign. The variable name acts as a reference or pointer to that memory location.

                **Syntax:**
                ```python
                variable_name = value
                ```
                You assign a value to a variable using the equal sign (`=`). The variable name should follow certain naming conventions.

                **Example:**
                ```python
                age = 30
                name = "Maryam"
                is_student = True
                ```

                **Common Data Types for Variables:**
                - `int`: Whole numbers like 10, -5
                - `float`: Decimal numbers like 3.14, 0.0
                - `str`: Strings or text like "Hello"
                - `bool`: Boolean values (`True` or `False`)
                - `list`: Ordered collection like [1, 2, 3]
                - `tuple`: Immutable ordered collection like (1, 2, 3)
                - `set`: Unordered collection of unique items like {1, 2, 3}
                - `dict`: Collection of key-value pairs like {"name": "Ali", "age": 25}

                **Variable Naming Rules:**
                - Must start with a letter (a-z, A-Z) or an underscore (_)
                - Cannot start with a number
                - Can contain letters, numbers, and underscores
                - Case sensitive (`age` and `Age` are different variables)
                - Cannot use Python reserved keywords (`if`, `for`, `while`, etc.)

                **Type Conversion:**  
                Sometimes you need to convert values from one type to another:
                ```python
                a = int("5")   # Convert string "5" to integer 5
                b = float(3)   # Convert integer 3 to float 3.0
                c = str(10)    # Convert integer 10 to string "10"
                ```
            """,

            "Functions": """
                ### ⚙️ What are Functions?
                **Definition:**  
                Functions are self-contained blocks of code designed to perform a specific task. They help break down programs into smaller, manageable, and reusable pieces.

                **Why use Functions?**  
                - Avoid repeating the same code multiple times.
                - Organize your code into logical chunks.
                - Improve readability and maintainability.
                - Make debugging easier by isolating functionality.

                **How Functions Work:**  
                You define a function once, and then you can call or invoke it whenever you need to perform the task it handles.

                **Syntax:**
                ```python
                def function_name(parameters):
                    # block of code
                    return value  # optional
                ```

                **Example:**
                ```python
                def greet(name):
                    return f"Hello, {name}!"

                print(greet("Maryam"))
                ```

                **Calling Functions:**  
                To run a function, write its name followed by parentheses, optionally passing arguments:
                ```python
                greet("Ali")
                ```

                **Default Arguments:**  
                You can provide default values to parameters which are used if no argument is passed:
                ```python
                def greet(name="Guest"):
                    return f"Hi, {name}!"

                greet()         # Returns "Hi, Guest!"
                greet("Sara")   # Returns "Hi, Sara!"
                ```

                **Lambda Functions (Anonymous Functions):**  
                Small, unnamed functions useful for simple operations:
                ```python
                add = lambda x, y: x + y
                print(add(3, 4))  # Output: 7
                ```

                **Returning Multiple Values:**  
                Functions can return more than one value as a tuple:
                ```python
                def get_min_max(numbers):
                    return min(numbers), max(numbers)

                mn, mx = get_min_max([2, 4, 7])
                print(mn, mx)  # Output: 2 7
                ```
            """,

            "OOP": """
                ### 🧱 What is Object-Oriented Programming (OOP)?
                **Definition:**  
                Object-Oriented Programming is a paradigm based on the concept of “objects” — entities that contain data in the form of fields (attributes) and code in the form of procedures (methods). It models real-world entities and their interactions.

                **Why use OOP?**  
                - Organizes complex programs using objects, making code more modular and reusable.
                - Promotes code reuse through inheritance.
                - Supports encapsulation (hiding internal details).
                - Enables polymorphism (same interface, different behavior).

                **Key Concepts of OOP:**

                - **Class:**  
                  A blueprint or template for creating objects.
                ```python
                class Person:
                    def __init__(self, name):
                        self.name = name  # attribute

                    def greet(self):
                        print(f"Hello, {self.name}")
                ```

                - **Object:**  
                  An instance of a class representing a specific entity.
                ```python
                p1 = Person("Ali")
                p1.greet()  # Output: Hello, Ali
                ```

                - **Encapsulation:**  
                  Restricting access to some components to protect data integrity.
                ```python
                class BankAccount:
                    def __init__(self):
                        self.__balance = 0  # private variable

                    def deposit(self, amount):
                        self.__balance += amount
                        return self.__balance
                ```

                - **Inheritance:**  
                  Creating new classes from existing classes to reuse code.
                ```python
                class Animal:
                    def speak(self):
                        return "Sound"

                class Dog(Animal):
                    def speak(self):
                        return "Woof!"
                ```

                - **Polymorphism:**  
                  Different classes can define methods with the same name, allowing for flexible code.
                ```python
                class Cat:
                    def sound(self):
                        print("Meow")

                class Bird:
                    def sound(self):
                        print("Chirp")

                for animal in [Cat(), Bird()]:
                    animal.sound()
                ```
            """,

            "Modules": """
                ### 📦 What are Modules?
                **Definition:**  
                Modules are separate Python files that contain reusable code — such as functions, classes, or variables. Using modules helps keep code organized and enables sharing or reusing code easily.

                **Why use Modules?**  
                - Split large programs into smaller, manageable files.
                - Avoid duplicating code.
                - Use pre-written libraries (standard or third-party) to speed up development.

                **Using Modules:**

                - **Importing a module:**
                ```python
                import math
                print(math.sqrt(16))  # Output: 4.0
                ```

                - **Creating your own module:**  
                  Save reusable code in a file, e.g., `mymodule.py`:
                ```python
                def add(a, b):
                    return a + b
                ```
                Then import it:
                ```python
                import mymodule
                print(mymodule.add(5, 3))
                ```

                - **Selective import:** Import only specific functions or variables:
                ```python
                from math import pi, pow
                print(pi, pow(2, 3))
                ```

                - **Aliases:** Rename modules to shorter names for convenience:
                ```python
                import numpy as np
                arr = np.array([1, 2, 3])
                ```

                - **Exploring modules:**  
                See what functions or variables a module contains:
                ```python
                import math
                print(dir(math))  # Lists all attributes and functions in math
                ```
            """
        }
        return Course("Python Basics", lessons)
