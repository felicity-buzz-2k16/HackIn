from django.db import models
from django.contrib.auth.models import User

# Create your models here.
        
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="user_id")
    level = models.IntegerField(default=1)
    tries = models.IntegerField(default=0)
    def __unicode__(self):
        return unicode(self.user)
 
#class no_of_request(models.Model):
#    ip = models.CharField(max_length=20, default="hello")
#    tries = models.IntegerField(default=0)
#    def __unicode__(self):
#        return unicode(self.ip)
