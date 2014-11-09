# -*-coding: utf-8 -*-
__author__ = 'Nikolay'


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
    #
    # тип машины - пока не обязателен
    #
    def __init__(self, car_id, car_type, start_speed, length, overtaking_speed):
        self.car_id = car_id
        self.car_type = car_type
        self.start_speed = start_speed
        self.length = length
        self.overtaking_speed = overtaking_speed


class Launching():
    def __init__(self, launching_id, road, list_of_cars, **kwds):
        self.launching_id = launching_id
        self.road = road
        self.list_of_cars = list_of_cars


class RoadState():
    def __init__(self, launching_id, cur_time=0, **kwds):
        self.launching_id = launching_id
        self.cur_time = cur_time


class CurrentCar(Car):
    def __init__(self, coordinate=0, current_speed=0, road_line=1, **kwds):
        super(Car, self).__init__(**kwds)
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
