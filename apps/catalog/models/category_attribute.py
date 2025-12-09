from django.db import models


class AttributeDataType(models.TextChoices):
    TEXT = "text", "Text"
    INTEGER = "integer", "Integer"
    FLOAT = "float", "Float"
    BOOLEAN = "boolean", "Boolean"
    DATE = "date", "Date"
    CHOICE = "choice", "Choice"


class CategoryAttribute(models.Model):
    category = models.ForeignKey(
        "catalog.Category",
        on_delete=models.CASCADE,
        verbose_name="Категория товара")

    name = models.CharField(
        max_length=50,
        verbose_name="Название атрибута для orm")

    title = models.CharField(
        max_length=50,
        verbose_name="Название атрибута для клиента")
    
    datatype = models.CharField(
        max_length=20,
        choices=AttributeDataType.choices,
        verbose_name="Тип данных")

    is_required = models.BooleanField(
        default=False,
        verbose_name="Обязательный атрибут для товара")

    is_filterable = models.BooleanField(
        default=False,
        verbose_name="Фильтр для товара")

    is_variant_attribute = models.BooleanField(
        default=False,
        verbose_name="Определяет вариант товара (SKU)")

    position = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Позиция отображении")

    created_at = models.DateTimeField(
            auto_now_add=True)

    updated_at = models.DateTimeField(
            auto_now=True)

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = 'Атрибут категории'
        verbose_name_plural = 'Атрибуты категории'

