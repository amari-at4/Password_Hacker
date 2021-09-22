import itertools


dishes_product = itertools.product(main_courses, desserts, drinks)
prices_product = itertools.product(price_main_courses, price_desserts, price_drinks)
my_money = 30
for dishes, prices in zip(dishes_product, prices_product):
    total = sum(prices)
    if total <= my_money:
        print(*dishes, total)
