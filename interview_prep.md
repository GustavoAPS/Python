# Python Interview Prep

Python Technical Interview Study Guide

This guide covers all key areas commonly evaluated in senior Python technical interviews —
from core language mechanics to Django best practices and deployment knowledge. It's
structured by topic, with explanations and study prompts.

## 1.Python Core Concepts

### Data Types

- Numeric, int, float, complex.
- Sequence: list, tuple, range.
- Text: string.
- Set: Set, frozen set.
- Mapping: dict, key value pairs.
- Boolean.
- Bynary, bytes, bytearray.

### Object-Oriented Programming

• Understand classes, constructors (**init**), and attributes.

- **Class** = blueprint to create objects.
- **Constructor (`__init__`)** = initializes attributes.
- **Attributes** = data about the object.
- **Methods** = actions the object can do.

```python
# Example: Car class

class Car:
    # Constructor: initializes the object with attributes
    def __init__(self, brand, model, year):
        self.brand = brand      # attribute
        self.model = model      # attribute
        self.year = year        # attribute
        self.speed = 0          # default attribute, starts at 0

    # Method: describe the car
    def describe(self):
        return f"{self.year} {self.brand} {self.model}"

    # Method: accelerate the car
    def accelerate(self, amount):
        self.speed += amount
        print(f"The car accelerated by {amount} km/h. Current speed: {self.speed} km/h.")

    # Method: brake the car
    def brake(self, amount):
        self.speed = max(0, self.speed - amount)  # avoid negative speed
        print(f"The car slowed down by {amount} km/h. Current speed: {self.speed} km/h.")

# --- Using the class ---

# Create two Car objects (instances)
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Tesla", "Model 3", 2023)

# Access attributes
print(car1.describe())  # 2020 Toyota Corolla
print(car2.describe())  # 2023 Tesla Model 3

# Use methods
car1.accelerate(30)  # The car accelerated by 30 km/h...
car1.brake(10)       # The car slowed down by 10 km/h...

# Modify attributes directly
car2.year = 2024
print(car2.describe())  # 2024 Tesla Model 3

# Add a new attribute dynamically
car2.color = "Red"
print(f"Car2 color: {car2.color}")

```

### Learn encapsulation using underscores:

Python don’t have true private attributes, but there are 2 stategies:

- Convention: single underscore, `_attribute` just to signal that “you shouldn’t touch this”
- Name mangling: Python changes the attribute name internally to `_ClassName__attribute`

### inheritance and multiple inheritance.

Inheritance allows one class (**child**) to reuse and extend the functionality of another class (**parent**).

Syntax:

```python
class Parent:
    pass

class Child(Parent):
    pass
```

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Dog inherits from Animal
class Dog(Animal):
    def speak(self):  # Override method
        print(f"{self.name} says Woof!")

# Cat inherits from Animal
class Cat(Animal):
    def speak(self):  # Override method
        print(f"{self.name} says Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()  # Buddy says Woof!
cat.speak()  # Whiskers says Meow!
```

When overriding methods, you can call the **parent class’s version** using `super()`

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # Call parent constructor
        self.breed = breed

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)   # Buddy
print(dog.breed)  # Golden Retriever
```

### How MRO (Method Resolution Order) works in multiple inheritance scenarios.

When multiple parents define the **same method**, Python uses **MRO** to decide which one to call.

Order: **Left to right** in the inheritance list.

### Special / Magic Methods

• Know what **str**, **repr**, **len**, **add**, **eq**, and **call** do.
• Learn how to override operators using dunder methods.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):   # User-friendly
        return f"'{self.title}' by {self.author}"

    def __repr__(self):  # Debug/developer-friendly
        return f"Book(title={self.title!r}, author={self.author!r})"

b = Book("1984", "George Orwell")
print(str(b))   # '1984' by George Orwell
print(repr(b))  # Book(title='1984', author='George Orwell')
```

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1 = Vector(1, 2)
v2 = Vector(1, 2)
print(v1 == v2)  # True
```

### Iterables, Iterators & Generators

• Difference between iter()/next() and yield.
• Use cases for generators (memory-efficient iteration).
• When to use generators over list comprehensions.

- **Iterable** = object you can loop over (`list`, `str`, etc.).
- **Iterator** = object with `__iter__()` + `__next__()` (produces values).
- **Generator** = iterator made with `yield`, lazy and memory-efficient.
- **List comprehension** = builds all results now.
- **Generator expression** = builds results one by one (lazy).

### Memory and Performance

• Understand the GIL (Global Interpreter Lock).
• Difference between multithreading and multiprocessing in Python.
• Use the multiprocessing module for true parallelism.

- **GIL**: only one thread runs Python code at a time.
- **Multithreading**: best for **I/O-bound tasks**.
- **Multiprocessing**: best for **CPU-bound tasks**, achieves **true parallelism**.
- Use `multiprocessing` module for parallel CPU-heavy workloads.

## 2. Django Framework

### ORM (Object-Relational Mapping)

• Understand how Django maps models to database tables.
• Learn to optimize queries using:
o select_related (foreign key joins)
o prefetch_related (many-to-many or reverse relations)

- **ORM**: Models ↔ Tables, Attributes ↔ Columns.
- **`select_related`**: Optimizes queries for **single-object relationships** (FK, OneToOne).
- **`prefetch_related`**: Optimizes queries for **multi-object relationships** (M2M, reverse FK).
- Use them to **prevent N+1 queries** and improve performance.

### Migrations

• What are Django migrations?
• How to create, run, and revert migrations.
• How to handle schema changes safely.

- **Migrations** keep models and database schema in sync.
- `makemigrations` → create migration files.
- `migrate` → apply changes to DB.
- Revert migrations carefully with `migrate app_name <migration_number>`.
- Use safe migration practices (nulls, defaults, step-by-step changes, data migrations).

### Views & APIs

• Build APIs using Django Rest Framework (DRF):
o Class-based views vs. function-based views
o Serializers: purpose and customization
o Permissions & Authentication
o Pagination and filtering

1. **Class-Based Views (CBVs) vs. Function-Based Views (FBVs)**

- **FBVs**: Simple Python functions that handle requests (`request -> response`).
    
    ✅ Easy to understand for small APIs.
    
    ❌ Can get messy for larger projects.
    
- **CBVs**: Python classes where each HTTP method (`GET`, `POST`, etc.) is a method inside the class.
    
    ✅ More reusable and scalable.
    
    ✅ Can inherit from DRF’s built-in views (`APIView`, `GenericAPIView`, `ViewSets`).
    
    ❌ Slightly harder to learn at first.
    

---

2. **Serializers**

- Purpose: Convert **Python objects ↔ JSON** (and validate incoming data).
- **ModelSerializer**: Automatically creates fields based on Django models.
- **Customization**:
    - Add extra fields.
    - Override `create()` or `update()`.
    - Use `validate_<field>()` for field-level validation.
    - Use `validate()` for object-level validation.

---

3. **Permissions & Authentication**

- **Authentication**: Who is the user? (e.g., Token, JWT, OAuth2).
- **Permissions**: What can the user do? (e.g., `IsAuthenticated`, `IsAdminUser`).
- You can apply permissions **globally**, at the **view level**, or at the **object level**.

---

4. **Pagination & Filtering**

- **Pagination**: Split large querysets into chunks (e.g., PageNumberPagination, LimitOffsetPagination).
- **Filtering**:
    - Simple filtering via query params (`?status=active`).
    - Advanced filtering using `django-filter`.
    - Search across fields using `SearchFilter`.
    - Ordering results with `OrderingFilter`.

### Advanced ORM

• Create custom model managers
• Use annotate(), aggregate(), and complex queries
• Connect Django with database views or raw SQL

## 3.Testing in Python

Test Types & Tools
• Unit Tests – test individual functions/methods
• Integration Tests – test systems working together (e.g., Django views + DB)
• End-to-End Tests – full workflows, often with tools like Cypress

Testing Tools
• unittest (built-in)
• pytest (popular 3rd-party framework)
• DRF test clients for API testing
• Use fixtures for setting up test data

Coverage & CI
• Enforce minimum test coverage
• Automate tests via CI tools (GitHub Actions, Jenkins)

## 4.Docker & Deployment

Docker Basics
• Write a Dockerfile for a Django app
• Use Docker Compose to run app + PostgreSQL
• Understand build contexts, ports, and volumes

1. **Dockerfile for Django**
    - Defines the environment to run your Django app.
    - Example:
        
        ```docker
        # Use official Python image
        FROM python:3.12-slim
        
        # Set working directory
        WORKDIR /app
        
        # Copy requirements and install
        COPY requirements.txt .
        RUN pip install --no-cache-dir -r requirements.txt
        
        # Copy app code
        COPY . .
        
        # Expose port
        EXPOSE 8000
        
        # Run Django server
        CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
        
        ```
        
2. **Docker Compose**
    - Orchestrates multiple containers (e.g., Django + PostgreSQL).
    - Example:
        
        ```yaml
        version: "3.9"
        services:
          db:
            image: postgres:15
            environment:
              POSTGRES_USER: user
              POSTGRES_PASSWORD: password
              POSTGRES_DB: mydb
            volumes:
              - postgres_data:/var/lib/postgresql/data
            ports:
              - "5432:5432"
        
          web:
            build: .
            command: python manage.py runserver 0.0.0.0:8000
            volumes:
              - .:/app
            ports:
              - "8000:8000"
            depends_on:
              - db
        
        volumes:
          postgres_data:
        
        ```
        
3. **Build Contexts, Ports, Volumes**
    - **Build context** → directory used for `COPY` and build.
    - **Ports** → map container ports to host (`8000:8000`).
    - **Volumes** → persist data (`postgres_data`) or mount code (`.:/app`).

---

Service Coordination
• Ensure DB containers are ready before Django starts
• Use entrypoint scripts or tools like [wait-for-it.sh](http://wait-for-it.sh/)

1. **DB readiness**
    - Ensure PostgreSQL is ready before Django starts.
    - Use `depends_on` in Compose (basic wait, doesn’t check DB health).
2. **Entrypoint scripts / wait-for-it**
    - Wait for DB to accept connections before running migrations or starting Django.
    - Example in entrypoint script:
        
        ```bash
        #!/bin/sh
        ./wait-for-it.sh db:5432 -- \
        python manage.py migrate && python manage.py runserver 0.0.0.0:8000
        
        ```
        

## 5.CI/CD Pipelines

### Concepts

- Continuous Integration: Practice of frequently integrating code changes into a shared repository.
- Continuous Deployment: Code is automatically tested and prepared for deployment, but deployment to production may require manual approval.
- Typical pipeline steps:
    - Code checkout
    - Linting (e.g., flake8, black)
    - Tests (unit, integration, Cypress)
    - Build & deploy (Docker, GitHub Actions)

### Best Practices

• Fail early (e.g., on linter or test errors)
• Notify team via email or Slack on success/failure
• Use code coverage checks

## 6.Databases & SQL

SQL Performance
• Know how to:
o Create indexes
o Use EXPLAIN to analyze queries
• Difference between INNER JOIN, LEFT JOIN

- **Indexes**
    - Speed up queries by allowing the database to find rows faster.
    - Example: `CREATE INDEX idx_name ON table_name(column_name);`
    - Use on columns frequently used in `WHERE`, `JOIN`, or `ORDER BY`.
- **EXPLAIN**
    - Analyze how the database executes a query.
    - Helps detect full table scans or inefficient joins.
    - Example: `EXPLAIN SELECT * FROM users WHERE age > 30;`
- **JOINs**
    - **INNER JOIN** → returns only matching rows from both tables.
    - **LEFT JOIN** → returns all rows from the left table and matched rows from the right table (NULL if no match).

ORM Optimization
• Avoid N+1 queries
• Use select_related and prefetch_related wisely
• When to use raw SQL or database views

- **Avoid N+1 Queries**
    - Happens when a query is run inside a loop for each row, causing many DB hits.
    - Solution: Use `select_related` and `prefetch_related`.
- **select_related**
    - For foreign key or one-to-one relationships.
    - Performs a SQL JOIN to fetch related objects in a single query.
    - Example:
        
        ```python
        books = Book.objects.select_related('author').all()
        
        ```
        
- **prefetch_related**
    - For many-to-many or reverse foreign key relationships.
    - Performs separate query and caches related objects.
    - Example:
        
        ```python
        authors = Author.objects.prefetch_related('books').all()
        
        ```
        
- **Raw SQL or Database Views**
    - Use when ORM cannot efficiently express complex queries.
    - Example:
        
        ```python
        from django.db import connection
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM my_view WHERE value > %s", [100])
            results = cursor.fetchall()
        
        ```
        

## 7.Data Structures & Time Complexity

### Python Structures

• list, set, dict, tuple: use cases and time complexities
• Why dictionary lookups are O(1)
• When to use sets for fast lookup

- **List** → ordered, duplicates allowed, index-based.
- **Tuple** → immutable version of list.
- **Set** → unordered, unique items, O(1) lookups.
- **Dict** → key-value, hash table, O(1) lookups.
- Use **sets/dicts** for **fast membership tests**.

### Complexity Awareness

• Understand O(n), O(log n), O(1), O(n^2)
• Apply to sorting, searching, loops

**Time Complexity (Big O) Overview**

1. **O(1) – Constant Time**

- Operation takes **the same time** regardless of input size.
- Examples: access an element by index in a list, dictionary lookup by key.

```python
lst = [10, 20, 30]
print(lst[1])   # O(1)
d = {'a': 1, 'b': 2}
print(d['a'])   # O(1)

```

---

2. **O(n) – Linear Time**

- Time grows **linearly** with input size `n`.
- Examples: iterating through a list, simple search, summing elements.

```python
lst = [1,2,3,4,5]
total = 0
for x in lst:   # O(n)
    total += x

```

---

3. **O(log n) – Logarithmic Time**

- Time grows **logarithmically** with input size.
- Examples: binary search in a sorted list, searching in balanced trees.
- **Divide-and-conquer** algorithms often have O(log n).

```python
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:  # O(log n)
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

```

---

4. **O(n^2) – Quadratic Time**

- Time grows **quadratically** with input size.
- Common in **nested loops**, some naive sorting algorithms (bubble sort, insertion sort).

```python
lst = [1,2,3,4]
for i in lst:         # O(n^2)
    for j in lst:
        print(i, j)

```

## 8.Final Interview Tips

• Practice explaining your thought process aloud
• Know the difference between knowing and applying a concept
• Don’t bluff – it’s better to say “I don’t know, but I’d try X”
• Be ready to defend design decisions (e.g., API structure, DB choice)
• Keep your answers structured and specific