# -*-coding: utf-8 -*-

"""
Общий комментарий:
    время будет задаваться только целыми числами
    есть предложение сделать время отдельным классом с проеркой
    (я на всякий случай это сделаю, вы напишите, если не понравится)
"""


class Time():
    """
        value - integer

        __value, в котором хранится само его значение не доступен извне
        для его получения нужно вызвать его как функци: time()

        для получения времени в виде строки можно писать str(time)
    """
    def __init__(self, value):
        if type(value) != type(int()):
            raise TypeError
        self.__value = value

    def __str__(self):
        return "({0.__value!r}".format(self)

    def __call__(self):
        return self.__value


class Pocket():
    def __init__(self, beginning, length):
        self.beginning = beginning
        self.length = length


class Road():
    def __init__(self, road_id, length, list_of_pockets):
        self.road_id = road_id
        self.length = length
        self.list_of_pockets = list_of_pockets


class Car():
    """
    тип машины - пока не обязателен
    """
    def __init__(self, car_id, car_type, start_speed, length,
                 overtaking_speed):
        self.car_id = car_id
        self.car_type = car_type
        self.start_speed = start_speed
        self.length = length
        self.overtaking_speed = overtaking_speed


class Launching():
    """
        list of cars - список объектов типа Car
    """
    def __init__(self, launching_id, road, list_of_cars):
        self.launching_id = launching_id
        self.road = road
        self.list_of_cars = list_of_cars


class RoadState():
    """
        current list of cars - список объектов типа CurrentCar
    """
    def __init__(self, launching_id, current_list_of_cars, cur_time=0):
        self.launching_id = launching_id
        self.current_list_of_cars = current_list_of_cars
        self.cur_time = cur_time


class CurrentCar():
    """
        car - объект типа Car (возмодно его стоит заменить на car_id)

        road line - полоса, по которой едет машина, если значение:
        натурально число, то это номер полосы (в нашем случае это может быть
        только 1), если машина едет в кармане, то значение равно 0
    """
    def __init__(self, car, coordinate=0, current_speed=0, road_line=1):
        self.car = car
        self.coordinate = coordinate
        self.current_speed = current_speed
        self.road_line = road_line


class Event():
    def __init__(self, launching_id, time, car_id, new_speed, new_line):
        self.launching_id = launching_id
        self.time = time
        self.car_id = car_id
        self.new_speed = new_speed
        self.new_line = new_line
