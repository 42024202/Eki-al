from django.db import models 


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(
        'catalog.Product',
        on_delete=models.CASCADE,
        verbose_name='Товар',
        related_name='attributes')

    attribute = models.ForeignKey(
        'catalog.CategoryAttribute',
        on_delete=models.CASCADE,
        related_name='values')

    value = models.CharField(
        max_length=100,
        verbose_name='Значение атрибута')

    def __str__(self):
        return f"{self.product.name} - {self.attribute.name}: {self.value}"


    class Meta:
        verbose_name = 'Значение атрибута'
        verbose_name_plural = 'Значения атрибутов'

