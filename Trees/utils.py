from os.path import dirname, abspath


class Paths:
    CURR_DIR = dirname(abspath(__file__))
    DS_DIR = dirname(CURR_DIR)
    QUEUE_DIR = f"{DS_DIR}/Queues"
