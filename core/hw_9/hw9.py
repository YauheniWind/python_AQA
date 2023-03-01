class House:
    def __init__(self, floors: int, height: float, width: float):
        self.floor = floors
        self.height = height
        self.width = width
        self.work_space()
        self.__list_of_tenants()

    def show_params(self):
        print(
            f"This {self.__class__.__name__} has {self.floor} floors, "
            f"and its height {self.height} and {self.width} width"
        )

    def work_space(self):
        return False

    def __list_of_tenants(self):
        tenants = 0
        if self.floor < 10:
            tenants += 2
            print(f"In this {self.__class__.__name__} living {tenants} Tenants")
        else:
            tenants += 10
            print(f"In this {self.__class__.__name__} living {tenants} Tenants")


house = House(2, 10, 10)
house.show_params()
print(house.work_space())


class Skyscraper(House):
    def __init__(self, floors: int, height: float, width: float, elevator: bool):
        super().__init__(floors, height, width)
        self.elevator = elevator

    def work_space(self):
        return True

    def show_params(self):
        print(
            f"This {self.__class__.__name__} has {self.floor} floors, and its height {self.height} "
            f"and {self.width} width and have elevator {self.elevator}"
        )


skyscraper = Skyscraper(50, 200, 240, True)
skyscraper.show_params()
print(skyscraper.work_space())


class Mansion(House):
    def __init__(self, floors: int, height: float, width: float, pool: bool):
        super().__init__(floors, height, width)
        self.pool = pool

    def show_params(self):
        print(
            f"This {self.__class__.__name__} has {self.floor} floors, and its height {self.height} "
            f"and {self.width} width and have a pool {self.pool}"
        )


mansion = Mansion(3, 20, 70, True)
mansion.show_params()
