# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group: str,
                             participants_second_group: str,
                             divider=',') -> list:
    shared_participants = list(set(participants_first_group.split(divider)).
                               intersection(participants_second_group.split(divider)))
    """ можно использовать set (уникальные элементы) для participants_first_group, т.к.
        если, скажем, два Сидорова было бы в списке участников, нужно было бы уточнить, какой 
        именно (введя еще имя). А если и имена совпадают, то ввели бы и отчество (малая вероятность, 
        что все три слова в ФИО будут у двух людей одинаковыми)
    """
    shared_participants.sort()

    return shared_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
