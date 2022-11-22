from django.shortcuts import render
from django.views import View
import random
from django.http import Http404

# Create your views here.
ingredients = {
    'meats': ['Ham', 'Turkey', 'Beef', 'Sasuage', 'Pepperoni', 'Bacon'],
    'cheese': ['Chedder', 'pepper jack', 'fondue', 'american', 'mozzeralla', 'swiss'],
    'toppings': ['onions', 'pickle', 'mayo', 'mustard', 'mushroom', 'ketchup', 'tomato', 'lettuce']
}

class SandwichAppView(View):
    def get(self, request):
        return render(
            request = request,
            template_name = 'sandwich_app.html',
            context = {'ingredients': ingredients.keys()}
        )

class IngredientsListView(View):
    def get(self, request, ingredient_type):

        if ingredient_type not in ingredients:
            raise Http404(f'No such ingredient: {ingredient_type}')

        return render(
            request = request,
            template_name = 'ingredients_list.html',
            context={
                'ingredients': ingredients[ingredient_type],
                'ingredient_type': ingredient_type,
            }
        )

class SandwichGeneratorView(View):
    def get(self, request):
        selected_meat = random.choice(ingredients['meats'])
        selected_cheese = random.choice(ingredients['cheese'])
        selected_toppings = random.choice(ingredients['toppings'])
        sandwich = f'{selected_meat} & {selected_cheese} with {selected_toppings}'
        
        return render(
            request = request,
            template_name = 'sandwich_generator.html',
            context = {'sandwich': sandwich}
        )

class SandwichMenuView(View):
    def get(self, request):

        sandwich_list = []

        for _ in range(150):
            selected_meat = random.choice(ingredients['meats'])
            selected_cheese = random.choice(ingredients['cheese'])
            selected_toppings = random.choice(ingredients['toppings'])

            radom_sandwich = f'{selected_meat} & {selected_cheese} with {selected_toppings}'

            if radom_sandwich not in sandwich_list:
                sandwich_list.append(radom_sandwich)

        return render(
            request = request,
            template_name = 'sandwich_menu.html',
            context = {'sandwich_list': sandwich_list}
        )
