# Дан список состоящий из данных разного типа.
# Вернуть новый список, где при помощи функции map() каждый элемент типа int первоначального списка
# приведён к типу str, элементы всех остальных типов передаются в новый список без изменения их типа.
# В качестве входной функции в map() использовать lambda-функцию.

values = [1, 2, '3', 'forth', 'end', 99, True, None]

for item in values:
    if [item(list)] is int():
        for [item(list)] in item:
            print(str([item(list)]))
        # new_list.append(item)

print(new_list)

# new_list = []
# if  != int in range(len(values)):
#     x.append(str(values[i]))


# new_list_3 = list(map(lambda x : for i in range(len(values)): x.append(str(values[i])), values))
#
#
# # new_list_2 = list(map(str, values))
# new_list = list(map(lambda x : str(x) if x != int(), values))
# # new_list = list(map(lambda x: str(x) if type(x) is type(int), values))
#
# print(new_list_2)
print(new_list)
# print(new_list_3)