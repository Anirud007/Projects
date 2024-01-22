from django.db import models

# Create your models here.
class Recepie(models.Model):
    r_name = models.CharField(max_length=225)
    r_des = models.TextField()
    r_image = models.ImageField(upload_to='rimg')

    def __str__(self):
        return self.r_name  