"""
    ТЕМА: Инкапсуляция, Полиморфизм
"""
"""
    public
    protected
    private
"""

# class Car:
#
#     def __init__(self, marka, year, model):
#         self.__marka = marka
#         self.__year = year
#         self.__model = model
#
#     def get_marka(self):
#         return self.__marka
#
#     def set_marka(self, newmarka):
#         self.__marka = newmarka
#
#     def get_year(self):
#         return self.__year
#
#     def set_year(self, newyear):
#         self.__year = newyear
#
#     def get_model(self):
#         return self.__model
#
#     def set_model(self, newmodel):
#         self.__model = newmodel
#
#     def get_info(self):
#         print(f"Marka: {self.get_marka()}\n"
#               f"Year: {self.get_year()}\n"
#               f"Model: {self.get_model()}")
#
# mercedes = Car("Mercedes", 2020, "Mercedes S-class")
# mercedes.set_year(2021)
# mercedes.get_info()
# print()
# lexus = Car("Lexus", 2023, "Lexus LS")
# lexus.get_info()


class Animal:

    def __init__(self, type):
        self.__type = type

    def get_type(self):
        return self.__type

    def set_type(self, newtype):
        self.__type = newtype

    def voice(self):
        pass

    def get_info(self):
        print(f"Type: {self.get_type()}")

class Cat(Animal):

    def __init__(self, type, run):
        super().__init__(type)
        self.__run = run

    def get_run(self):
        return self.__run

    def set_run(self, run):
        self.__run = run

    def voice(self):
        print(f"The cat meows")

    def get_info(self):
        super().get_info()
        print(f"Run: {self.get_run()}")

class Kangaroo(Animal):

    def __init__(self, type, eat):
        super().__init__(type)
        self.__eat = eat

    def get_eat(self):
        return self.__eat

    def set_eat(self, eat):
        self.__eat = eat

    def voice(self):
        print("The sound a kangaroo makes can be described as a 'grunting' noise.")

    def get_info(self):
        super().get_info()
        print(f"Eat: {self.get_eat()}")

cat = Cat("Cat", "4.02km")
cat.get_info()
cat.voice()
print()
kangaroo = Kangaroo("Kangaroo", "fruits and grass")
kangaroo.get_info()
kangaroo.voice()
