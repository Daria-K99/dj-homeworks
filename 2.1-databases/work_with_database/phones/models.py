from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50, unique=True)

