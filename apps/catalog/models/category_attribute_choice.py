from django.db import models 


class CategoryAttributeChoice(models.Model):
    attribute = models.ForeignKey(
        'catalog.CategoryAttribute',
        on_delete=models.CASCADE,
        related_name='choices')

    value = models.CharField(
            max_length=50)

    def __str__(self):
        return f"{self.value}"


    class Meta:
        unique_together = ('attribute', 'value')
        verbose_name = 'Вариант атрибута'
        verbose_name_plural = 'Варианты атрибута'
    
