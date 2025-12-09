from rest_framework.viewsets import ModelViewSet
from apps.catalog.models import Product
from apps.catalog.serializers.product import (
    ProductSerializer,
    ProductCreateSerializer
)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().prefetch_related(
        "images",
        "attributes__attribute",
        "brand",
        "category",)

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return ProductCreateSerializer
        return ProductSerializer

    def perform_destroy(self, instance):
        instance.delete()

