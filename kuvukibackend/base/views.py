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
def get_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
