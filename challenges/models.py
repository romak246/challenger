from django.db import models


class Challenge(models.Model):
    """Базовая модель челленджа"""
    title = models.CharField(blank=False, max_length=20, unique=True)
    description = models.TextField(blank=False)
    reward = models.IntegerField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
