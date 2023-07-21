import json
from .load_save import load_data, save_data
from .show import show_data
from .change import change_data
from .filter import filter_data
from .count import count_data
from .sort import sort_data
def terminal_data():

    data = load_data()
    save_data(data)
    try:
        inp = input("Введите команду(show, change, filter, count, sort): ")

        if inp == "show":
            show_data(data)
        elif inp == "change":
            change_data(data)
        elif inp == "filter":
            filter_data(data)
        elif inp == "count":
            count_data(data)
        elif inp == "sort":
            sort_data(data)
        else:
            print("Ошибка!!! Не правильный ввод команды")
            terminal_data()
    except KeyboardInterrupt:
        print()

