from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class Data(models.Model):
    id_num = models.IntegerField()
    title = models.TextField(default="")
    link = models.TextField(validators=[URLValidator()])
    city = models.CharField(max_length=100)
    main_image = models.TextField(validators=[URLValidator()])
