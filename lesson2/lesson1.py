"""
    ТЕМА: ООП
"""

# class Car:
#     marka = "Mercedes"
#     year = 2022
#     model = "Mers S-class"
#
# mercedes = Car()
# print(f"Marka: {mercedes.marka}\n"
#       f"Year: {mercedes.year}\n"
#       f"Model: {mercedes.model}")
# print()
# lexus = Car()
# lexus.marka = "Lexus"
# lexus.year = 2019
# lexus.model = "Lexus LS"
# print(f"Marka: {lexus.marka}\n"
#       f"Year: {lexus.year}\n"
#       f"Model: {lexus.model}")

class Car:

    def __init__(self, marka, year, model):
        self.marka = marka
        self.year = year
        self.model = model

    def get_info(self):
        print(f"Marka: {self.marka}\n"
              f"Year: {self.year}\n"
              f"Model: {self.model}")

mercedes = Car("Mercedes", 2020, "Mercedes S-class")
mercedes.get_info()
print()
lexus = Car("Lexus", 2023, "Lexus LS")
lexus.get_info()
