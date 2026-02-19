from django.db import models


class IceCream(models.Model):
    """Basic ice cream entry with pricing and availability."""

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "мороженое"
        verbose_name_plural = "мороженое"

    def __str__(self):
        return self.title
