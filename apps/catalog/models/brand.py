from django.db import models
from django.utils.text import slugify


class Brand(models.Model):
    name = models.CharField(
            max_length=30,
            unique=True,
            verbose_name='Название бренда')

    slug = models.SlugField(
            unique=True)

    logo = models.ImageField(
            upload_to='brand_images/')

    is_active = models.BooleanField(
            default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)  

    def __str__(self):
        return f"{self.name}"

    
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

        ordering = ['name']

