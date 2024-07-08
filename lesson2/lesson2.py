"""
    ТЕМА: Мурастоо (ООП)
"""

class Building:

    def __init__(self, type, year, city, pupils, floor):
        self.type = type
        self.year = year
        self.city = city
        self.pupils = pupils
        self.floor = floor

    def get_info(self):
        print(f"Type: {self.type}\n"
              f"Year: {self.year}\n"
              f"City: {self.city}\n"
              f"Pupils: {self.pupils}\n"
              f"Floor: {self.floor}")

class School(Building):

    def __init__(self, type, year, city, pupils, floor, library):
        super().__init__(type, year, city, pupils, floor)
        self.library = library


    def get_info(self):
        super().get_info()
        print(f"Library: {self.library}")

class House(Building):

    def __init__(self, type, year, city, pupils, floor, garage):
        super().__init__(type, year, city, pupils, floor)
        self.garage = garage

    def get_info(self):
        super().get_info()
        print(f"Garage: {self.garage}")

school = School("School", 2000, "Bishkek", 500, 7, "True")
school.get_info()
print()
house = House("House", 1998, "Naryn", 4, 2,"No")
house.get_info()