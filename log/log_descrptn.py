# -*- coding utf-8 -*-
__author__ = 'snusmumrik'
from models.models import Car, Pocket, Road, Event


class Log():

    def log_definition(self, launching, events, road):
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
            "pocket id | beginning | length\n"
        )
        for pocket in road.list_of_pockets:
            self.write_in_log(pocket)

        self.log_file.write(
            "Events:\n"
            + "car id | time | new_speed | new_line\n")

    def __write_pocket(self, pocket):
        self.log_file.write(
            'pocket#' + str(pocket.pocket_id) + '|'
            + str(pocket.beginning) + " | "
            + str(pocket.length) + " | \n"
        )

    def __write_road(self, road):
        self.log_file.write(
            "road#" + str(road.road_id)
            + str(road.length) + " | "
            + str(len(road.list_of_pockets)) + "\n")

    def __write_car(self, car):
        self.log_file.write(
            "car#" + str(car.car_id) + " | "
            + str(car.car_type) + " | "
            + str(car.start_speed) + " | "
            + str(car.length) + " | "
            + str(car.overtaking_speed) + "\n")

    def __write_event(self, event):
        self.log_file.write(
            + "car#" + str(event.car_id) + " | "
            + str(event.time) + " | "
            + str(event.new_speed) + " | "
            + str(event.new_line) + "\n")

    def write_in_log(self, object):
        if type(object) == Pocket:
            self.__write_pocket(object)
        elif type(object) == Road:
            self.__write_road(object)
        elif type(object) == Car:
            self.__write_car(object)
        elif type(object) == Event:
            self.__write_event(object)
        else:
            raise Exception

    def __get_pocket(self, pocket_id):
        pass

    def __get_road(self, road_id):
        pass

    def __get_car(self, car_id):
        pass

    def __get_event(self, car_id, time):
        pass

    def get(self, object):
        if type(object) == Pocket:
            self.__get_pocket(object)
        elif type(object) == Road:
            self.__get_road(object)
        elif type(object) == Car:
            self.__get_car(object)
        elif type(object) == Event:
            self.__get_event(object)
        else:
            raise Exception
