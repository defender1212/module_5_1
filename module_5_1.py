class House:
    def __init__(self,name, number_of_floors):
        self.name = name
        self.number = number_of_floors

    def go_to(self, new_floor):

        if int(new_floor) < 1 or int(new_floor) > int(self.number):
            print("Такого этажа не существует")
        else:
            i = 1
            while i <= int(new_floor):
                print(i)
                i += 1

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)





