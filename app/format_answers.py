import pprint
from typing import Type
from itertools import groupby

from app.models import Record


def format_items_data(items_data: list[Type[Record]]) -> dict:
    """Преобразовываем данные из БД в нужную структуру для фронтенда"""

    record_list = [i.__dict__ for i in items_data]
    result_data = {}

    # группируем словарь по ключу и затем проходимся по сгруппированным элементам для добавления во вложенный словарь
    for main_category, group in groupby(record_list, lambda elem: elem['main_category']):
        result_data[main_category] = {}
        for category, group2 in groupby(group, lambda elem: elem['category']):
            result_data[main_category][category] = {}
            for type, group3 in groupby(group2, lambda elem: elem['type']):
                if type:
                    result_data[main_category][category][type] = []
                else:
                    result_data[main_category][category] = None
                for i in group3:
                    if i['ceo']:
                        result_data[main_category][category][type].append(i['ceo'])
                    elif result_data[main_category][category] is not None:
                        result_data[main_category][category][type] = None

    pprint.pprint(result_data)

    return result_data
