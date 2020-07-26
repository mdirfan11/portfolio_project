from django.db import models

# Create your models here.
class Jobs(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=30)
    discription = models.CharField(max_length=300)

    def __str__(self):
        return self.title