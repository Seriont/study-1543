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
    def __init__(self, launching_id, road, cars_list):
        self.launching_id = launching_id
        self.road = road
        self.cars_list = cars_list


class RoadState():
    """
        current list of cars - список объектов типа CurrentCar
    """
    def __init__(self, launching_id, current_cars_list, cur_time=0):
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


class Log():
    """
        self.launching - 
            contains Launching object.
            <Launching>
            defines launching parameters
        self.events - 
            contains list of Event objects
            [<Event>]
            defines changes in launching process
        self.log_file - 
            contains file
            <FileObject>
            format "log_n", n - launching_id
            defines name of the log-file
                      
    """
    def __init__(self, launching, events, road):
        self.launching = launching
        self.events = events
        self.log_file = open("log_" + str(self.launching.launching_id), "w")
        self.log_file.write(
            "Launching number: " + str(self.launching.launching_id) + "\n" * 2
            + "Cars number: " + str(len(self.launching.cars_list)) + "\n"
            + "car id | car type | start speed | length | overtaking speed")
        cars_list = self.launching.cars_list
        for car in cars_list:
            self.write_in_log(car)

        self.log_file.write(
            "Road:" + "\n"
            + "road id | length | number_of_pockets\n"
        )
        self.write_in_log(road)
        self.log_file.write(
            "Pockets:\n"
            "beginning | length\n"
        )
        for pocket in road.list_of_pockets:
            self.write_in_log(pocket)

        self.log_file.write(
            "\n"
            + "car id | time | new_speed | new_line\n")

    def write_pocket(self, pocket):
        self.log_file.write(
            str(pocket.beginning) + " | "
            + str(pocket.length) + " | \n"
        )

    def write_road(self, road):
        self.log_file.write(
            "road#" + str(road.road_id)
            + str(road.length) + " | "
            + str(len(road.list_of_pockets)) + "\n")

    def write_car(self, car):
        self.log_file.write(
            "car#" + str(car.car_id) + " | "
            + str(car.car_type) + " | "
            + str(car.start_speed) + " | "
            + str(car.length) + " | "
            + str(car.overtaking_speed) + "\n")

    def write_event(self, event):
        self.log_file.write(
            + "car#" + str(event.car_id) + " | "
            + str(event.time) + " | "
            + str(event.new_speed) + " | "
            + str(event.new_line) + "\n")

    def write_in_log(self, object):
        if type(object) == Pocket:
            self.write_pocket(object)
        elif type(object) == Road:
            self.write_road(object)
        elif type(object) == Car:
            self.write_car(object)
        elif type(object) == Event:
            self.write_event(object)
        else:
            raise Exception
