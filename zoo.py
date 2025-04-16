class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Some generic animal sound")

    def eat(self):
        print(f"{self.name} is eating.")


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        print("Chirp chirp!")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print("Growl!")


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print("Hiss!")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)


class Employee:
    def __init__(self, name):
        self.name = name


class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name)

    def feed_animal(self, animal):
        print(f"{self.name} feeds {animal.name}.")
        animal.eat()


class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name)

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

import pickle

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_to_file(self, filename):
        """Сохраняет текущее состояние зоопарка в файл"""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_file(filename):
        """Загружает состояние зоопарка из файла"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print("Файл не найден! Создан новый зоопарк.")
            return Zoo()

# Пример использования
if __name__ == "__main__":
    # Создание и заполнение зоопарка
    zoo = Zoo()

    parrot = Bird("Polly", 2, 30)
    tiger = Mammal("Tony", 3, "Orange")
    snake = Reptile("Slinky", 4, "Rough")

    zoo.add_animal(parrot)
    zoo.add_animal(tiger)
    zoo.add_animal(snake)

    keeper = ZooKeeper("John")
    vet = Veterinarian("Lisa")

    zoo.add_employee(keeper)
    zoo.add_employee(vet)

    # Сохранение состояния в файл
    zoo.save_to_file('zoo_state.pkl')

    # Демонстрация работы зоопарка до загрузки
    print("Original Zoo:")
    print("Animals:", [animal.name for animal in zoo.animals])
    print("Employees:", [employee.name for employee in zoo.employees])
    animal_sound(zoo.animals)

    # Загрузка состояния из файла
    loaded_zoo = Zoo.load_from_file('zoo_state.pkl')

    # Демонстрация работы зоопарка после загрузки
    print("\nLoaded Zoo:")
    print("Animals:", [animal.name for animal in loaded_zoo.animals])
    print("Employees:", [employee.name for employee in loaded_zoo.employees])
    animal_sound(loaded_zoo.animals)

    # Проверка функциональности сотрудников
    print("\nActivities in loaded zoo:")
    loaded_zoo.employees[0].feed_animal(loaded_zoo.animals[0])
    loaded_zoo.employees[1].heal_animal(loaded_zoo.animals[1])