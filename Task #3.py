count_t1, count_t2, count_t3 = 0, 0, 0
text1, text2, text3 = '', '', ''

with open('text1.txt', 'r', encoding='utf8') as f_1:
    for line_t1 in f_1:
        count_t1 += 1
        text1 += line_t1

with open('text2.txt', 'r', encoding='utf8') as f_2:
    for line_t2 in f_2:
        count_t2 += 1
        text2 += line_t2

with open('text3.txt', 'r', encoding='utf8') as f_3:
    for line_t3 in f_3:
        count_t3 += 1
        text3 += line_t3

max_el = max(count_t1, count_t2, count_t3)
min_el = min(count_t1, count_t2, count_t3)

with open('final_text.txt', 'w', encoding='utf8') as final:
    if count_t1 == min_el and count_t2 == max_el:
        final.writelines('\ntext1.txt\n')
        final.writelines(str(count_t1))
        final.writelines('\n')
        final.writelines(str(text1))

        final.writelines('\ntext3.txt\n')
        final.writelines(str(count_t3))
        final.writelines('\n')
        final.writelines(str(text3))

        final.writelines('\ntext2.txt\n')
        final.writelines(str(count_t2))
        final.writelines('\n')
        final.writelines(str(text2))

    elif count_t1 == min_el and count_t3 == max_el:
        final.writelines('\ntext1.txt\n')
        final.writelines(str(count_t1))
        final.writelines('\n')
        final.writelines(str(text1))

        final.writelines('\ntext2.txt\n')
        final.writelines(str(count_t2))
        final.writelines('\n')
        final.writelines(str(text2))

        final.writelines('\ntext3.txt\n')
        final.writelines(str(count_t3))
        final.writelines('\n')
        final.writelines(str(text3))

    elif count_t2 == min_el and count_t1 == max_el:
        final.writelines('\ntext2.txt\n')
        final.writelines(str(count_t2))
        final.writelines('\n')
        final.writelines(str(text2))

        final.writelines('\ntext3.txt\n')
        final.writelines(str(count_t3))
        final.writelines('\n')
        final.writelines(str(text3))

        final.writelines('\ntext1.txt\n')
        final.writelines(str(count_t1))
        final.writelines('\n')
        final.writelines(str(text1))

    elif count_t2 == min_el and count_t3 == max_el:
        final.writelines('\ntext2.txt\n')
        final.writelines(str(count_t2))
        final.writelines('\n')
        final.writelines(str(text2))

        final.writelines('\ntext1.txt\n')
        final.writelines(str(count_t1))
        final.writelines('\n')
        final.writelines(str(text1))

        final.writelines('\ntext3.txt\n')
        final.writelines(str(count_t3))
        final.writelines('\n')
        final.writelines(str(text3))

    elif count_t3 == min_el and count_t1 == max_el:
        final.writelines('\ntext3.txt\n')
        final.writelines(str(count_t3))
        final.writelines('\n')
        final.writelines(str(text3))

        final.writelines('\ntext2.txt\n')
        final.writelines(str(count_t2))
        final.writelines('\n')
        final.writelines(str(text2))

        final.writelines('\ntext1.txt\n')
        final.writelines(str(count_t1))
        final.writelines('\n')
        final.writelines(str(text1))
    else:
        final.writelines('\ntext3.txt\n')
        final.writelines(str(count_t3))
        final.writelines('\n')
        final.writelines(str(text3))

        final.writelines('\ntext1.txt\n')
        final.writelines(str(count_t1))
        final.writelines('\n')
        final.writelines(str(text1))

        final.writelines('\ntext2.txt\n')
        final.writelines(str(count_t2))
        final.writelines('\n')
        final.writelines(str(text2))
