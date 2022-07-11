from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from rest_framework.response import Response
from .models import Product

@api_view(http_method_names=['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def get_fruit(request, fruit_id):
    try:
        fruit = Product.objects.get(id=fruit_id, category='FRUITS')
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(fruit)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def get_vegetable(request, vegetable_id):
    try:
        vegetable = Product.objects.get(id=vegetable_id, category='VEGETABLES')
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(vegetable)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def get_grocery(request, grocery_id):
    try:
        grocery = Product.objects.get(id=grocery_id, category='GROCERIES')
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(grocery)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def get_single_stationary(request, stationary_id):
    try:
        single_stationery = Product.objects.get(id=stationary_id, category='STATIONERY')
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(single_stationery)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def get_toiletry(request, toiletry_id):
    try:
        toiletry = Product.objects.get(id=toiletry_id, category='TOILETRIES')
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(toiletry)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def get_beverage(request, beverage_id):
    try:
        beverage = Product.objects.get(id=beverage_id, category='BEVERAGES')
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(beverage)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def get_single_butchery(request, butchery_id):
    try:
        single_butchery = Product.objects.get(id=butchery_id, category='BUTCHERY')
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(single_butchery)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def get_fruits(request):
    try:
        fruits = Product.objects.get(category='FRUITS')
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(fruits)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def get_vegetables(request):
    try:
        vegetables = Product.objects.get(category='VEGETABLES')
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(vegetables)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def get_groceries(request):
    try:
        groceries = Product.objects.get(category='GROCERIES')
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(groceries)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def get_stationery(request):
    try:
        stationery = Product.objects.get(category='STATIONERY')
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(stationery)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def get_toiletries(request):
    try:
        toiletries = Product.objects.get(category='TOILETRIES')
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(toiletries)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def get_beverages(request):
    try:
        beverages = Product.objects.get(category='BEVERAGES')
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(beverages)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def get_butchery(request):
    try:
        butchery = Product.objects.get(category='BUTCHERY')
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(butchery)
    return Response(serializer.data)

