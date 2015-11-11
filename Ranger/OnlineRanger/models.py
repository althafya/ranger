from django.db import models
from django_image_tools.models import Image

# Create your models here.

class galleryDB(models.Model):
	
	pic = models.ForeignKey(Image)
	picName = models.CharField(max_length = 30)
	picPrice = models.CharField(max_length = 20)

	
	
