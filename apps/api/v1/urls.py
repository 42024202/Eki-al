from rest_framework.routers import DefaultRouter
from django.urls import path, include

"""Catalog viewsets"""
from apps.catalog.views.product import ProductViewSet

router = DefaultRouter()

router.register("products", ProductViewSet, basename="products")

urlpatterns = router.urls

