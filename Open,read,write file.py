
import pprint
# import json
print('\nTask #1\n')

with open('text.txt', 'rt', encoding='utf8') as f:
    cook_book = {}
    for line in f:
        dish = line.strip()
        recipe = []
        count_ing = f.readline()
        for i in range(int(count_ing)):
            ings = f.readline()
            name, q, unit = ings.split(' | ')
            ingredient = {'ingredients_name': name, 'quantity': int(q), 'measure': unit.strip()}
            recipe.append(ingredient)
            cook_book[dish] = recipe
        f.readline()

pprint.pprint(cook_book, width=100, sort_dicts=False)  # Так красиво, как в задании не получается. Это выглядит компактнее.
# print(json.dumps(cook_book, indent=1, ensure_ascii=False, sort_keys=False))

print('\nTask #2\n')


def get_shop_list_by_dishes(dishes, person_count):
    new_dict = {}
    for dish_name, q_list in cook_book.items():
        if dish_name in dishes:
            for ings_dict in q_list:
                ing = ings_dict.get('ingredients_name')
                del(ings_dict['ingredients_name'])
                for k, v in ings_dict.items():
                    if k == 'quantity':
                        ings_dict['quantity'] = v * person_count
                new_dict[ing] = ings_dict
    return new_dict


res = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint.pprint(res, width=100)