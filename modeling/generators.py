from models.models import Log, Launching, Car
from roads.roads import
from functions.functions import latest_launching_id
import random


class Generator():
    """
    Данный класс используется при конфигурации нового запуска и только тогда

    get_road() - функция, которая достает нужную дорогу из уже имеющихся по ее
    id. Пока что не продумано, каким образом будут создаваться и храниться road
    """

    def generate_car(self, car_id):
        car = Car(
            car_id=car_id,
            start_speed=(60 + random.random() % 20),
            overtaking_speed=(80 + random.random() % 30),
            length=(2 + random.random() % 3)
        )
        return car

    def generate_launching(
            self,
            number_of_cars=random.random() % 20,
            road_id=0):
        road = get_road(road_id)
        cars_list = []
        for car_id in range(number_of_cars):
            cars_list.append(self.generate_car(car_id))
        launching_id = latest_launching_id() + 1
        launching = Launching(
            launching_id=launching_id,
            road=road,
            cars_list=cars_list,
        )
        return launching
