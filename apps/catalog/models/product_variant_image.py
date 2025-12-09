from django.db import models


class ProductVariantImage(models.Model):
    product_variant = models.ForeignKey(
            "catalog.ProductVariant",
            on_delete=models.CASCADE,
            verbose_name='Фотография варианта товара')

    image = models.ImageField(
            upload_to="product_variant_images/")

    is_main = models.BooleanField(
            default=False)

    created_at = models.DateTimeField(
            auto_now_add=True)

    updated_at = models.DateTimeField(
            auto_now=True)

    def save(self, *args, **kwargs):
        if self.is_main:

            ProductVariantImage.objects.filter(
                    variant=self.product_variant,
                    is_main=True
                    ).exclude(pk=self.pk).update(is_main=False)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Фотография варианта товара'
        verbose_name_plural = 'Фотографии вариантов товара'
        
