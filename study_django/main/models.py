from typing import Any
from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=100)
    # end_date = models.DateTimeField()
    area = models.CharField(max_length=15)
    
    
    def to_json(self):
        return {
            "name" : self.name,
            # "end_date" : self.end_date.isoformat,
            "area" : self.area,
        }