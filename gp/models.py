from django.db import models

# Create your models here.
class Commerce(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()
    def __str__(self):
        return self.name
class Subscriber(models.Model):

    email = models.EmailField()
    def __str__(self):
        return self.email
