# -*-coding: utf-8 -*-

import random

from log.log_descrptn import Log
from models.models import Launching, Car, Time, RoadState, CurrentCar
from common.functions import latest_launching_id, get_road


class Generator(Log):
    """
    Данный класс используется при конфигурации нового запуска и только тогда

    Все функции random можно будет сделать более умными, когда будет сделана
    основная часть проекта
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
        time_start = Time(0)
        for car_id in range(number_of_cars):
            cars_list.append([
                self.__generate_car(car_id),
                time_start
            ])
            time_start.increase(1+random.random()%20)
        launching_id = latest_launching_id() + 1
        launching = Launching(
            launching_id=launching_id,
            road=road,
            cars_list=cars_list,
        )
        self.write_in_log(launching)

        return launching_id


class Modeling(Log):
    '''
    Данный класс осуществляет движение машин и запись изменений в лог,
    при visualize = True, происходит визуализация движения, а запись в лог
    отключается.

    get - это функция доставания из лога чего-либо по его id и, возможно,
    типу объекта
    '''

    def __init__(self, launching_id, visualize=False):
        self.launching = self.get(launching_id)
        self.road_state = RoadState(
            launching_id=launching_id
        )
        self.visualize=visualize

    def handler(self):
        cars_list = self.get(
            self.launching.launching_id,
            Car()
        )
        # это должно считывать машины по этому launching_id
        while self.road_state.current_cars_list[0].coordinate >= \
                self.launching.road.length:
            for (car, start_time) in cars_list:
                if start_time == self.road_state.cur_time:
                    new_car = CurrentCar(
                        car=car,
                        coordinate=0,
                        current_speed=car.start_speed
                    )
                    self.road_state.current_cars_list = [new_car] + \
                                        self.road_state.current_cars_list
