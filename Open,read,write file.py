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

import pprint
# pprint.pprint(cook_book, width=100, sort_dicts=False)


def get_shop_list_by_dishes(dishes, person_count):
    new_dict ={}
    for list in cook_book.values():# получаем список словарей [{'ingredients_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'}] и т.д.
        for ings_dict in list: # получаем словарь {'ingredients_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'} и т.д.
            ings = ings_dict.get('ingredients_name') # получаем назввание ингридиента, который потом сделает ключем нового словаря
            del(ings_dict['ingredients_name']) # удаляем словаря пару ключ-значение (название ингридиента)
            for k, v in ings_dict.items():
                if k == 'quantity':
                    ings_dict['quantity'] = v * person_count
            new_dict[ings] = ings_dict  # формируем новый словарь
    return new_dict


res = get_shop_list_by_dishes(cook_book, 5)

pprint.pprint(res, width=100, sort_dicts=False)



