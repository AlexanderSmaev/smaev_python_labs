# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "task_2_input.csv"
OUTPUT_FILENAME = "task_2_output.json"
INDENT = 4


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'rt', newline='\n') as input_file:
        input_data = csv.DictReader(input_file, delimiter=',')

        # TODO Сериализовать в файл с отступами равными 4
        with open(OUTPUT_FILENAME, 'wt') as output_file:
            json.dump([row for row in input_data], output_file, indent=INDENT)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")



