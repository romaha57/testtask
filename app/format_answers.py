import pprint
from typing import Type
from itertools import groupby

from app.models import Record


def format_items_data(items_data: list[Type[Record]]) -> dict:
    """Преобразовываем данные из БД в нужную структуру для фронтенда"""

    record_list = [i.__dict__ for i in items_data]
    result_data = {}

    # группируем словарь по ключу и затем проходимся по сгруппированным элементам для добавления во вложенный словарь
    for elem in record_list:
        if elem['type'] and elem['ceo']:
            result_data.setdefault(elem['main_category'], {}).setdefault(elem['category'], {}).setdefault(elem['type'], []).append(elem['ceo'])
        elif not elem['type']:
            result_data.setdefault(elem['main_category'], {}).setdefault(elem['category'])

        elif not elem['ceo']:
            result_data.setdefault(elem['main_category'], {}).setdefault(elem['category'], {}).setdefault(elem['type'])
        else:
            result_data.setdefault(elem['main_category'], {}).setdefault(elem['category'], {}).setdefault(elem['type'], {}).setdefault(elem['ceo'])


    pprint.pprint(result_data)

    return result_data
