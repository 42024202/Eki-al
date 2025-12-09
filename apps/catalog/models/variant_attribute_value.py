from django.db import models 


class VariantAttributeValue(models.Model):
    variant = models.ForeignKey(
        to='catalog.ProductVariant',
        on_delete=models.CASCADE,
        verbose_name='Вариант товара',
        related_name='variant_attributes')

    attribute = models.ForeignKey(
        to="catalog.CategoryAttribute",
        on_delete=models.CASCADE,
        related_name="variant_values",
        verbose_name="Атрибут")

    value = models.CharField(
        max_length=255,
        verbose_name="Значение атрибута варианта")

    class Meta:
        unique_together = ("variant", "attribute")

    def __str__(self):
        return f"{self.variant.sku} → {self.attribute.title}: {self.value}"
