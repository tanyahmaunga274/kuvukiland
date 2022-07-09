from django.urls import path
from . import views

urlpatterns = [
    path('products', views.get_products, name='get_products'),
    path('products/fruits', views.get_fruits, name='get_fruits'),
    path('products/vegetables', views.get_vegetables, name='get_vegetables'),
    path('products/groceries', views.get_groceries, name='get_groceries'),
    path('products/stationery', views.get_stationery, name='get_stationery'),
    path('products/toiletries', views.get_toiletries, name='get_toiletries'),
    path('products/beverages', views.get_beverages, name='get_beverages'),
    path('products/butchery', views.get_butchery, name='get_butchery'),

    path('products/fruits/<int:fruit_id>', views.get_fruit, name='get_fruit'),
    path('products/vegetables/<int:vegetable_id>', views.get_vegetable, name='get_vegetable'),
    path('products/groceries/<int:grocery_id>', views.get_grocery, name='get_grocery'),
    path('products/stationery/<int:stationary_id>', views.get_single_stationary, name='get_single_stationary'),
    path('products/toiletries/<int:toiletry_id>', views.get_toiletry, name='get_toiletry'),
    path('products/beverages/<int:beverage_id>', views.get_beverage, name='get_beverage'),
    path('products/butchery/<int:butchery_id>', views.get_single_butchery, name='get_single_butchery'),
]