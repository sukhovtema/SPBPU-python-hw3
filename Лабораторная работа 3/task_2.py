def find_common_participants(group1, group2, delimiter=','):
    participants1 = group1.split(delimiter)
    participants2 = group2.split(delimiter)

    # множества для удобной работы с пересечениями
    set1 = set(participants1)
    set2 = set(participants2)

    common_participants = sorted(list(set1.intersection(set2)))

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
