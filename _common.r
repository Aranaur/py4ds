library(reticulate)


# products %>% 
#     mutate(name = case_when(
#         name == 'ананас' ~ 'pineapple',
#         name == 'апельсины' ~ 'oranges',
#         name == 'арбуз' ~ 'watermelon',
#         name == 'бананы' ~ 'bananas',
#         name == 'баранина' ~ 'mutton',
#         name == 'батон' ~ 'long loaf',
#         name == 'бублики' ~ 'bagels',
#         name == 'варенье' ~ 'jam',
#         name == 'вафли' ~ 'waffles',
#         name == 'виноград' ~ 'grape',
#         name == 'вода газированная' ~ 'carbonated water',
#         name == 'вода негазированная' ~ 'still water',
#         name == 'говядина' ~ 'beef',
#         name == 'горох' ~ 'peas',
#         name == 'гречка' ~ 'buckwheat',
#         name == 'груши' ~ 'pears',
#         name == 'жевательная резинка' ~ 'chewing gum',
#         name == 'иван-чай в пакетиках' ~ 'ivan-tea in bags',
#         name == 'икра' ~ 'caviar',
#         name == 'йогурт' ~ 'yogurt',
#         name == 'квас' ~ 'kvass',
#         name == 'кексы' ~ 'cupcakes',
#         name == 'кетчуп' ~ 'ketchup',
#         name == 'кофе 3 в 1' ~ 'coffee 3 in 1',
#         name == 'кофе без кофеина' ~ 'decaffeinated coffee',
#         name == 'кофе зерновой' ~ 'grain coffee',
#         name == 'кофе молотый' ~ 'ground coffee',
#         name == 'кофе растворимый' ~ 'instant coffee',
#         name == 'кофе холодный' ~ 'cold coffee',
#         name == 'курица' ~ 'chicken',
#         name == 'лаваш' ~ 'pita',
#         name == 'леденцы' ~ 'lollipops',
#         name == 'лепешка' ~ 'cake',
#         name == 'лимонад' ~ 'lemonade',
#         name == 'майонез' ~ 'mayonnaise',
#         name == 'макароны' ~ 'pasta',
#         name == 'мандарины' ~ 'tangerines',
#         name == 'мармелад' ~ 'marmalade',
#         name == 'масло кунжутное' ~ 'sesame oil',
#         name == 'масло льняное' ~ 'linseed oil',
#         name == 'масло оливковое' ~ 'olive oil',
#         name == 'масло подсолнечное' ~ 'sunflower oil',
#         name == 'мед' ~ 'honey',
#         name == 'молоко' ~ 'milk',
#         name == 'морс брусничный' ~ 'сowberry juice',
#         name == 'морс клюквенный' ~ 'cranberry juice',
#         name == 'морс черничный' ~ 'fruit drink blueberry',
#         name == 'мука' ~ 'flour',
#         name == 'овсянка' ~ 'oatmeal',
#         name == 'пакет бумажный' ~ 'paper bag',
#         name == 'печенье' ~ 'cookie',
#         name == 'рис' ~ 'rice',
#         name == 'рыба вяленая' ~ 'dried fish',
#         name == 'рыба копченая' ~ 'smoked fish',
#         name == 'рыба соленая' ~ 'salted fish',
#         name == 'сахар' ~ 'sugar',
#         name == 'свинина' ~ 'pork',
#         name == 'сгущенка' ~ 'condensed milk',
#         name == 'семечки' ~ 'seeds',
#         name == 'сливки' ~ 'cream',
#         name == 'сметана' ~ 'sour cream',
#         name == 'сок ананасовый' ~ 'pineapple juice',
#         name == 'сок апельсиновый' ~ 'orange juice',
#         name == 'сок мультифрукт' ~ 'multifruit juice',
#         name == 'сок яблочный' ~ 'apple juice',
#         name == 'соль' ~ 'salt',
#         name == 'сосиски' ~ 'sausages',
#         name == 'сухарики' ~ 'crackers',
#         name == 'сухофрукты' ~ 'dried fruits',
#         name == 'сушки' ~ 'drying',
#         name == 'телятина' ~ 'veal',
#         name == 'уксус' ~ 'vinegar',
#         name == 'хлеб' ~ 'bread',
#         name == 'чай зеленый в пакетиках' ~ 'green tea bags',
#         name == 'чай зеленый листовой' ~ 'leaf green tea',
#         name == 'чай травяной в пакетиках' ~ 'herbal tea bags',
#         name == 'чай травяной листовой' ~ 'herbal leaf tea',
#         name == 'чай холодный' ~ 'cold tea',
#         name == 'чай черный в пакетиках' ~ 'black tea bags',
#         name == 'чай черный листовой' ~ 'black leaf tea',
#         name == 'чайный гриб' ~ 'tea mushroom',
#         name == 'чипсы' ~ 'chips',
#         name == 'шоколад белый' ~ 'white chocolate',
#         name == 'шоколад черный' ~ 'black chocolate',
#         name == 'шпроты' ~ 'sprats',
#         name == 'энергетический напиток' ~ 'energy drink',
#         name == 'яблоки' ~ 'apples',
#         TRUE ~ as.character('--------------------')
#     )) %>% 
#   write_csv('00_data/sql/products2.csv')