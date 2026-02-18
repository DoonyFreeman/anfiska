# cinema/models.py
# Импортируем модуль с классом Model, от которого будем наследовать модели:
from django.db import models

class VideoProduct(models.Model):
    title = models.CharField(max_length=128) 