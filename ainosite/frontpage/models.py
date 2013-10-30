from django.db import models

# Create your models here.

class ImageFile(models.Model):
    imagefile = models.FileField(upload_to='images/%Y/%m/%d')
