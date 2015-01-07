# -*-coding: utf-8 -*-

import random

from models.models import Launching, Car
from common.functions import latest_launching_id, get_road


class Generator():
    """
    Данный класс используется при конфигурации нового запуска и только тогда
    """

    def __generate_car(self, car_id):
        car = Car(
            car_id=car_id,
            start_speed=(60 + random.random() % 20),
            overtaking_speed=(80 + random.random() % 30),
            length=(2 + random.random() % 3)
        )
        return car

    def generate_launching(
            self,
            number_of_cars=(1 + random.random() % 20),
            road_id=0
    ):
        road = get_road(road_id)
        cars_list = []
        for car_id in range(number_of_cars):
            cars_list.append(self.__generate_car(car_id))
        launching_id = latest_launching_id() + 1
        launching = Launching(
            launching_id=launching_id,
            road=road,
            cars_list=cars_list,
        )
        return launching
