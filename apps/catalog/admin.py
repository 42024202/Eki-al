from django.contrib import admin

from .models import (
    Brand, Category,
    CategoryAttribute,Product,ProductImage,
    ProductAttributeValue,ProductVariant,
    VariantAttributeValue,ProductVariantImage,)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 1


class ProductVariantImageInline(admin.TabularInline):
    model = ProductVariantImage
    extra = 1


class VariantAttributeValueInline(admin.TabularInline):
    model = VariantAttributeValue
    extra = 1


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "is_active")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "parent", "is_active", "slug")
    list_filter = ("parent", "is_active")
    search_fields = ("name",)


@admin.register(CategoryAttribute)
class CategoryAttributeAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "name", "datatype", "is_variant_attribute")
    list_filter = ("category", "datatype", "is_variant_attribute")
    search_fields = ("name", "title")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand", "category", "is_active", "created_at")
    list_filter = ("brand", "category")
    search_fields = ("name",)
    inlines = [ProductImageInline, ProductAttributeValueInline]


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "sku", "price", "quantity", "created_at")
    list_filter = ("product", "price")
    search_fields = ("sku",)
    inlines = [VariantAttributeValueInline, ProductVariantImageInline]


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "attribute", "value")
    list_filter = ("attribute", "product")


@admin.register(VariantAttributeValue)
class VariantAttributeValueAdmin(admin.ModelAdmin):
    list_display = ("id", "variant", "attribute", "value")
    list_filter = ("attribute", "variant")


@admin.register(ProductVariantImage)
class ProductVariantImageAdmin(admin.ModelAdmin):
    list_display = ("id", "is_main", "created_at")
    list_filter = ("is_main",)

