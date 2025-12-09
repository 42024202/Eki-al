from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(
            max_length=30,
            unique=True,
            verbose_name='Название категории')

    parent = models.ForeignKey(
            "self",
            null=True,
            blank=True,
            related_name="children",
            on_delete=models.CASCADE,)

    is_active = models.BooleanField(
            default=True,
            verbose_name='Активность категории')

    slug = models.SlugField(
            unique=True,
            verbose_name='Slug категории')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)    
    
    def __str__(self):
        return f"{self.name}"

