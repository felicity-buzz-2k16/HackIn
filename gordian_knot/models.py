from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
	level_list = [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10), (11,11), (12,12), (13,13), (14,14), (15,15), (16,16), (17,17), (18,18), (19,19), (20,20) ]
	level = models.IntegerField (choices = level_list, default = 0)
	question_text = models.TextField ('Question', max_length = 1000)
	correct_answer = models.CharField(max_length = 100)
	def __unicode__(self):
		return unicode(self.level)

class Profile(models.Model):
	user = models.OneToOneField(User)
	score = models.IntegerField(default = 0)
	tries = models.IntegerField(default = 0)
	level = models.IntegerField()
	def __unicode__(self):
		return unicode(self.user)