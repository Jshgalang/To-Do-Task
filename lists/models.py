from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Item(models.Model):
	text = models.TextField(default='')
	list = models.ForeignKey('List', default=None)

class List(models.Model): # # research more about the magic in models.Model why it can be instantiated automatically
	def get_absolute_url(self):
		return reverse('view_list', args=[self.id])
