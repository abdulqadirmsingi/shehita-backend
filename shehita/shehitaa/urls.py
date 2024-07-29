from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import *


router = DefaultRouter()
router.register("product", viewset=ProductViewset, basename="product")
router.register("category", viewset=CategoryViewset, basename="category")
router.register('carts', CartViewSet)
router.register('customers', CustomerViewSet)
router.register('orders', OrderViewSet, basename='order')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', CartItemViewSet, basename='cart-items')

urlpatterns = router.urls + carts_router.urls