# -*-coding: utf-8 -*-

import os
from exceptions import IdError
from models.models import Road, Pocket


def route_path():
    current_dir = os.path.abspath(os.curdir)
    route = current_dir[:current_dir.rfind('\\')]

    return route


def latest_launching_id():
    launching_id = 0
    route = route_path()
    while os.path.exists(route + "\\logs\\log_" + str(launching_id())):
        launching_id += 1

    return launching_id


def get_road(road_id):

    def read_road(file_name):
        input_file = open(file_name, mode="r")
        length_str = input_file.readline()
        length_of_road = int(
            length_str[length_str.find(":")+1:].strip().rstrip()
        )
        pockets = []
        pocket_str = input_file.readline()
        while pocket_str:
            pocket_str = pocket_str[pocket_str.find(":")+1:]
            beginning, length = tuple(
                map(int, pocket_str.strip().rstrip().split())
            )
            pocket = Pocket(
                beginning=beginning,
                length=length
            )
            pockets.append(pocket)
            pocket_str = input_file.readline()
        input_file.close()

        return Road(
            road_id=road_id,
            length=length,
            list_of_pockets=pockets
        )

    route = route_path()
    road_file_path = route + "\\roads\\road_" + str(road_id)
    if not os.path.exists(road_file_path):
        raise IdError("No road with such id found")

    return read_road(road_file_path)
