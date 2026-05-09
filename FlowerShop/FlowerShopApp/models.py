from django.db import models
from django.contrib.auth.models import User

class Bouquet(models.Model):
    SIZE_CHOICES = [
        ("S", "Мал"),
        ("M", "Среден"),
        ("L", "Голем")
    ]
    flower_type = models.CharField(max_length=100)
    arrangement = models.CharField(max_length=100)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to="bouquet_photos/", null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    fresh = models.BooleanField()

    def __str__(self):
        return f"{self.flower_type}"


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    date_opened = models.DateField(auto_now_add=True)
    located_in_eu = models.BooleanField()

    def __str__(self):
        return f"{self.name}"