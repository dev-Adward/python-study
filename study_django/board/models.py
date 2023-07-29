from django.db import models

# Create your models here.
class Board(models.Model):
    boardTitle = models.CharField(max_length=150)
    boardContent = models.CharField(max_length=1000)
    