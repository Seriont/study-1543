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
    """
    def __init__(self, value=0):
        if type(value) != type(int()):
            raise TypeError
        self.__value = value

    def __call__(self):
        return self.__value

    def __lt__(self, other):
        return self.__value < other.__value

    def __le__(self, other):
        return self.__value <= other.__value

    def __eq__(self, other):
        return self.__value == other.__value

    def __ne__(self, other):
        return self.__value != other.__value

    def __ge__(self, other):
        return self.__value >= other.__value

    def __gt__(self, other):
        return self.__value > other.__value

    def increase(self, value=1):
        self.__value += value


class Pocket():
    def __init__(self, beginning, length, pocket_id):
        self.beginning = beginning
        self.length = length
        self.pocket_id = pocket_id


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
        list of cars - список пар объектов типа Car, Time где воторой объект
        задает время старта для той или иной машины
    """
    def __init__(self, launching_id, road, cars_list):
        self.launching_id = launching_id
        self.road = road
        self.cars_list = cars_list


class RoadState():
    """
        current list of cars - список объектов типа CurrentCar
    """
    def __init__(self, launching_id, current_cars_list=[], cur_time=Time(0)):
        self.launching_id = launching_id
        self.current_cars_list = current_cars_list
        self.cur_time = cur_time


class CurrentCar():
    """
        car - объект типа Car (возможно его стоит заменить на car_id)

        road line - полоса, по которой едет машина, если значение:
        натурально число, то это номер полосы (в нашем случае это может быть
        только 1), если машина едет в кармане, то значение равно 0
    """
    def __init__(self, car, current_speed, coordinate=0, road_line=1):
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
