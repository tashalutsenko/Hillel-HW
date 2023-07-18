number_list = [1, 3, 7, 1, 1, 2, 3, 7, 6, 5, 5, 4, 1, 5, 9, 1, 7, 0, 0, 7, 6, 5, 5, 4, 1, 5, 9, 3, 7, 1, 1, 2, 3, 7]

freq_dict = {}

for num in number_list:
    if num in freq_dict:
        freq_dict[num] += 1
    else:
        freq_dict[num] = 1

for i in range(10):
     print(i, ":", freq_dict.get(i, 0))