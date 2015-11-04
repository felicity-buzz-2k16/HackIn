from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.core.validators import RegexValidator

class Design(models.Model):
	user = models.ForeignKey(User)
	design = models.ImageField(upload_to='designs')
	title=models.CharField(max_length=200,blank=False)
	def __unicode__(self):
		return unicode(self.id)
class DesignForm(ModelForm):
    class Meta:
        model = Design
        fields = ['title',
        		  'design', 
        		] 
class poll(models.Model):
	user = models.ForeignKey(User)
	design = models.ForeignKey(Design)
	def __unicode__(self):
		return unicode(self.user)