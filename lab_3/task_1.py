# TODO Напишите функцию для поиска индекса товара
from typing import Optional


def find_item_index(items_list: list, find_item: str) -> Optional[int]:
    for index_current_item, current_item in enumerate(items_list):
        if current_item == find_item:
            return index_current_item
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
