# File: oop_methods.py
# Lập trình hướng đối tượng trong Python

# 1. Lớp và đối tượng cơ bản
class Person:
    def __init__(self, name, age):  # Hàm khởi tạo
        self.name = name            # Thuộc tính (attribute)
        self.age = age

    def introduce(self):            # Phương thức (method)
        return f"Hi, I'm {self.name}, {self.age} years old"

person = Person("Alice", 25)        # Tạo đối tượng
print("1. Class basic:", person.introduce())  # Hi, I'm Alice, 25 years old

# 2. Đóng gói (Encapsulation) - Thuộc tính private
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # Thuộc tính private (dùng __)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"New balance: {self.__balance}"
        return "Invalid amount"

    def get_balance(self):          # Getter để truy cập private
        return self.__balance

account = BankAccount(100)
print("2. Encapsulation:", account.deposit(50))  # New balance: 150
print("   Balance:", account.get_balance())      # 150

# 3. Kế thừa (Inheritance)
class Student(Person):              # Student kế thừa từ Person
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Gọi hàm __init__ của lớp cha
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying"

student = Student("Bob", 20, "S123")
print("3. Inheritance:", student.introduce())  # Hi, I'm Bob, 20 years old
print("   Method:", student.study())           # Bob is studying

# 4. Đa hình (Polymorphism)
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):           # Hàm dùng đa hình
    return animal.speak()

dog = Dog()
cat = Cat()
print("4. Polymorphism:", animal_sound(dog))  # Woof!
print("   ", animal_sound(cat))               # Meow!

# 5. Thuộc tính và phương thức tĩnh (Static)
class MathUtils:
    @staticmethod
    def add(a, b):                  # Phương thức tĩnh, không cần self
        return a + b

print("5. Static method:", MathUtils.add(3, 4))  # 7

# Lưu ý
print("\nLưu ý: OOP giúp tổ chức code theo mô hình thực tế, hữu ích cho cấu trúc dữ liệu phức tạp.")