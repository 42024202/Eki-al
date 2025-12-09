from django.db import models


class ProductImage(models.Model):
    product = models.ForeignKey(
            'catalog.Product',
            on_delete=models.CASCADE,
            related_name='images',
            verbose_name='товар')

    image = models.ImageField(
            upload_to='images/',
            verbose_name='Фотография товара')

    is_main = models.BooleanField(
            default=False,
            verbose_name='Главная фотография')

    created_at = models.DateTimeField(
            auto_now_add=True)


    def save(self, *args, **kwargs):
        """If image becomes main, remove other main images"""
        if self.is_main:
            ProductImage.objects.filter(
                    product=self.product,
                    is_main=True
                    ).exclude(pk=self.pk).update(is_main=False)

        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Фотография товара'
        verbose_name_plural = 'Фотографии товара'

