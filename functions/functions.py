import os


def latest_launching_id():
    launching_id = 0
    current_dir = os.path.abspath(os.curdir)
    route = current_dir[:current_dir.rfind('\\')]
    while os.path.exists(route + "\logs\log_" + str(launching_id())):
        launching_id += 1

    return launching_id
