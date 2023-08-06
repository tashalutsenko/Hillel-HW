import time

from hime_1 import Auto


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
            super().__init__(brand, age, mark, color, weight)
            self.max_load = max_load

    def move(self):
            print("attention")
            super().move()

    def load(self):
            time.sleep(1)
            print("load")
            time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
            super().__init__(brand, age, mark, color, weight)
            self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")