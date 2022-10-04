count_t1, count_t2, count_t3 = 0, 0, 0
text1, text2, text3 = '', '', ''
dict_basic, subdict_1, subdict_2, subdict_3 = {}, {}, {}, {}

with open('text1.txt', 'r', encoding='utf8') as f_1:
    for line_t1 in f_1:
        count_t1 += 1
        text1 += line_t1
subdict_1['text1.txt'] = text1
dict_basic[count_t1] = subdict_1

with open('text2.txt', 'r', encoding='utf8') as f_2:
    for line_t2 in f_2:
        count_t2 += 1
        text2 += line_t2
subdict_2['text2.txt'] = text2
dict_basic[count_t2] = subdict_2

with open('text3.txt', 'r', encoding='utf8') as f_3:
    for line_t3 in f_3:
        count_t3 += 1
        text3 += line_t3
subdict_3['text3.txt'] = text3
dict_basic[count_t3] = subdict_3

with open('final_text.txt', 'w', encoding='utf8') as final:
    for q_str, v in dict_basic.items():
        if q_str == min(dict_basic.keys()):
            for file_name, text in v.items():
                final.writelines([str(file_name), '\n', str(q_str), '\n', str(text), '\n'])

    for q_str, v in dict_basic.items():
        if min(dict_basic.keys()) < q_str < max(dict_basic.keys()):
            for file_name, text in v.items():
                final.writelines([str(file_name), '\n', str(q_str), '\n', str(text), '\n'])

    for q_str, v in dict_basic.items():
        if q_str == max(dict_basic.keys()):
            for file_name, text in v.items():
                final.writelines([str(file_name), '\n', str(q_str), '\n', str(text), '\n'])


# РЕКОМЕНДАЦИЯ ПРЕПОДАВАТЕЛЯ
# ________________________________________________
# Татьяна, добрый день.
# Спасибо за работу.
# Задача 3 - предложу вот такой подход к решению
#
#
 # import os
#
# def compile_files(files_list):
#     data = {}
#     for file in files_list:
#         with open(file, encoding="utf-8") as f:
#             file_data = f.readlines()
#             data[len(file_data)] = (file, " ".join(file_data))
#
#     data = dict(sorted(data.items()))
#
#     with open("result_data.txt", "w", encoding="utf-8") as new_file:
#         for key, value in data.items():
#             new_file.write(f"{value[0]} \n")
#             new_file.write(f"{key} \n")
#             new_file.write(f"{value[1]} \n")
#
#
# files = ["1.txt", "2.txt", "3.txt"]
# files = [os.path.join(os.getcwd(), file) for file in files]
# compile_files(files)
