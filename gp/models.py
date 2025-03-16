from django.db import models

# Create your models here.
class Commerce(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=70)
    message = models.CharField(max_length=500)
    def __str__(self):
        return self.name
