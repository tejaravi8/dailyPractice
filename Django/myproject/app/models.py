from django.db import models

class Skills(models.Model):
    name=models.CharField(max_length=100)
    level=models.CharField(max_length=50)
    experience=models.IntegerField()
    
    def __str__(self):
        return f"{self.name} - {self.level}"