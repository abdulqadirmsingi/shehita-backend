from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

# Create your views here.

class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer