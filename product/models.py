from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.PositiveIntegerField(help_text="Valor do produto em centavos")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
