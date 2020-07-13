import sys


def handling_input(message):
    key = input(message)
    if key != "да":
        return 'Закрываемся...', sys.exit
    return 'Продолжаем ', print

