from rest_framework import serializers
from apps.catalog.models import category_attribute
from catalog.models import (
        Product, ProductImage,
        ProductAttributeValue, CategoryAttribute,
        CategoryAttributeChoice)


"""Image"""
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_main']
        read_only_fields = ['id', 'is_main']


"""Attribute"""
class ProductAttributeValueSerializer(serializers.ModelSerializer):
    attribute_name = serializers.CharField(
            source="attribute.name",
            read_only=True)

    attribute_title = serializers.CharField(
            source="attribute.title",
            read_only=True)

    class Meta:
        model = ProductAttributeValue
        fields = ["id", "attribute", "attribute_name", "attribute_title", "value"]


"""Main serializer for product"""
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(
            many=True,
            read_only=True)

    attributes = ProductAttributeValueSerializer(
            many=True,
            read_only=True)

    category_name = serializers.CharField(
            source="category.name",
            read_only=True)

    brand_name = serializers.CharField(
            source="brand.name",
            read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "slug",
                  "description", "brand", "brand_name",
                  "category", "category_name",
                  "is_active","images", "attributes", "created_at"]


"""Serializer for product creation"""
class ProductCreateSerializer(serializers.ModelSerializer):
    attributes = serializers.DictField(
            child=serializers.CharField(), write_only=True)

    images = serializers.ListField(
            child=serializers.ImageField(), write_only=True, required=False)

    class Meta:
        model = Product
        fields = ["name", "description",
                  "brand", "category", "is_active", "attributes", "images"]

    def validate(self, data):
        category = data["category"]
        attrs_dict = data["attributes"]

        category_attrs = CategoryAttribute.objects.filter(
                category=category,
                is_variant_attribute = False)

        allowed_names = {a.name: a for a in category_attrs}

        for name, value in attrs_dict.items():
            if name not in allowed_names:
                raise serializers.ValidationError(
                    f"Attribute '{name}' does not exist for this category.")
            
            attribute = allowed_names[name]

            if attribute.datatype == "choice":
                valid_values = attribute.choices.values_list("value", flat=True)
                if value not in valid_values:
                    raise serializers.ValidationError(
                        f"Invalid choice '{value}' for attribute '{name}'. "
                        f"Allowed: {list(valid_values)}")
        return data
            

    def create(self, validated_data):
        attributes_data = validated_data.pop("attributes")
        images_data = validated_data.pop("images", [])

        product = Product.objects.create(**validated_data)

        for attr_name, value in attributes_data.items():
            attr = CategoryAttribute.objects.get(
                category=product.category, name=attr_name)

            ProductAttributeValue.objects.create(
                product=product, attribute=attr, value=value)

        for img in images_data:
            ProductImage.objects.create(product=product, image=img)

        return product
