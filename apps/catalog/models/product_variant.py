from django.db import models


class ProductVariant(models.Model):
    product = models.ForeignKey(
        to='catalog.Product',
        on_delete=models.CASCADE,
        related_name='variants')

    sku = models.CharField(
        max_length=50,
        blank=True)

    price = models.PositiveIntegerField(default=0)

    quantity = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(
        auto_now_add=True)

    updated_at = models.DateTimeField(
        auto_now=True)

    def generate_sku(self):
        attrs = self.variant_attributes.all()
        parts = [f"{a.attribute.name[:3].upper()}:{a.value}" for a in attrs]
        base = f"{self.product.id}-"+"-".join(parts)

        sku = base
        num = 1
        while ProductVariant.objects.filter(product=self.product, sku=sku).exists():
            sku = f"{base}-{num}"
            num += 1
        return sku

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = self.generate_sku()
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('product', 'sku')

