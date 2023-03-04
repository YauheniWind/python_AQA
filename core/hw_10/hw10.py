class Flower:
    def __init__(self, name: str, cost: int, deadline: int):
        self.name = name
        self.cost = cost
        self.deadline = deadline

    def show_info(self):
        print(
            f"It is {self.name}, cost is {self.cost}$, deadline ~ {self.deadline} days"
        )


class Rose(Flower):
    def __init__(self, name: str, cost: int, deadline: int):
        super().__init__(name, cost, deadline)


class Sunflower(Flower):
    def __init__(self, name: str, cost: int, deadline: int):
        super().__init__(name, cost, deadline)


class Bouquet:
    def __init__(self, list_of_flower):
        self.list_of_flower = list_of_flower

    def deadline_flower(self):

        deadline_list = [i.deadline for i in self.list_of_flower]
        res_deadline = sum(deadline_list) // len(deadline_list)

        print(f"The bouquet will fade in {res_deadline} days")
        return res_deadline

    def sort_cost(self):

        sorted_cost = [i.cost for i in self.list_of_flower]
        res_cost = sorted(sorted_cost)

        print(f"The bouquet sorted from min to max {res_cost}")
        return res_cost

    def find_flower(self, f):
        if f in self.list_of_flower:
            print(f"Flower {f} is in bouquet")
            return True
        else:
            print(f"Flower {f} is not in bouquet")
            return False

    def total(self):

        total_cost = [i.cost for i in self.list_of_flower]
        res_total = sum(total_cost)

        print(f"Total cost per bouquet {res_total}$ ")
        return res_total


rose = Rose("Rose", 5, 7)
sunflower = Sunflower("Sunflower", 2, 10)
rose.show_info()
sunflower.show_info()

flowers = [rose, sunflower]

bouquet = Bouquet(flowers)

bouquet.deadline_flower()
bouquet.sort_cost()
bouquet.find_flower("Sunflower")
bouquet.total()
