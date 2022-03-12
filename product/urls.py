from rest_framework.routers import SimpleRouter
from product.views import ProductModelViewSet

router = SimpleRouter()

router.register("product", ProductModelViewSet, basename="product")
