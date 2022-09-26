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
pprint.pprint(cook_book, width=100, sort_dicts=False)

