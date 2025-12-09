from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(
            max_length=50)

    category = models.ForeignKey(
            'catalog.Category',
            on_delete=models.DO_NOTHING,
            verbose_name='Категория товара')

    slug = models.SlugField(
            unique=True,
            blank=True)

    description = models.TextField(
            verbose_name='Описание товара')

    brand = models.ForeignKey(
            'catalog.Brand',
            on_delete=models.DO_NOTHING,
            verbose_name='Бренд')

    is_active = models.BooleanField(
            default=True,
            verbose_name='Активность товара')
    
    created_at = models.DateTimeField(
            auto_now_add=True)

    updated_at = models.DateTimeField(
            auto_now=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            num = 1

            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1

            self.slug = slug

        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.name}"

    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

        ordering = ['-created_at']

