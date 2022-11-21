from django.urls import path
from sandwich_app.views import SandwichAppView, IngredientsListView, SandwichGeneratorView

urlpatterns = [
    path('', SandwichAppView.as_view(), name='sandwich'),
    path('ingredients/<str:ingredient_type>', IngredientsListView.as_view(), name='ingredients_list'),
    path('random', SandwichGeneratorView.as_view(), name='sandwich_generator'),
]