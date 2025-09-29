from django.db import models

# Create your models here.
class Comic(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='comics/')

    def __str__(self):
        return self.titulo