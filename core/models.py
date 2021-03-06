from django.db import models
from django.core.urlresolvers import reverse
import PIL.Image as Image
import os
import coffeedapp.settings as settings
from django.contrib.auth.models import User
from django.db.models import Avg



# for AWS upload
# import os
# import uuid

# def upload_to_location(instance, filename):
# 	blocks = filename.split('.')
#  ext = blocks[-1]
#  filename = "%s.%s" % (uuid.uuid4(), ext)
#  instance.title = blocks[0]
#  return os.path.join('uploads/', filename)
# # for AWS upload

RATING_CHOICES = (
	(0, 'None'),
	(1, '*'),
	(2, '**'),
	(3, '***'),
	(4, '****'),
	(5, '*****'),
	)


# Create your models here.
MAIN_DIR = os.path.dirname(os.path.dirname(__file__))

class Location(models.Model):
	title = models.CharField(max_length=300)
	description = models.TextField(null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	hours = models.TextField(null=True, blank=True)
	image_file = models.ImageField(upload_to='uploads', null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)


	def __unicode__(self):
		return self.title
	         
	def get_absolute_url(self):
		return reverse(viewname="location_list", args=[self.id])

	def get_average_rating(self):
		average = self.review_set.all().aggregate(Avg('rating'))['rating__avg']
		if average == None:
			return average
		else:
			return int(average)

	def get_reviews(self):
		return self.review_set.all()

class Review(models.Model):
	location = models.ForeignKey(Location)
	user = models.ForeignKey(User)
	description = models.TextField(null=True, blank=True)
	rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
