# TODO решите задачу
import json


INPUT_FILE = "task_1_input.json"


def task() -> float:
    with open(INPUT_FILE) as f:
        data_from_file = json.load(f)

    sum_ = sum([each_dict["score"] * each_dict["weight"] for each_dict in data_from_file])
    return round(sum_, 3)


print(task())

