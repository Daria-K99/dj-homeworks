from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'pizza': {
        'яйца, шт': 2,
        'сметана, ст.л': 4,
        'майонез, ст.л': 3,
        'мука, ст.л': 9,
        'соль, ч.л.': 1.5,
        'томатный соус, г': 100,
        'сыр, г': 150,
        'колбаса, г': 100,
        'грибы, г': 75,
    }
}

def get_recipe(request, recipe_name):
    servings = int(request.GET.get('servings',1))

    recipe = {
        ingredient: amount * servings
        for ingredient, amount in DATA[recipe_name].items()
    }

    context = {'recipe': recipe}

    return render(request, 'calculator/index.html', context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
