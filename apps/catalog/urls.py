from rest_framework.routers import DefaultRouter
from catalog.views.product import ProductViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")

urlpatterns = router.urls

