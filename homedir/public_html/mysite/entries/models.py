from django.db import models
import datetime
from django.utils import timezone

class EntryManager(models.Manager):
    def unvoted_or_random(self):
        unvoted_entries = self.filter(voted = False).order_by('-pub_date')
        voted_entries = self.filter(voted = True).order_by('?')    
        if unvoted_entries:
            return unvoted_entries[:1]
        else:
            return voted_entries[:1]
    def random(self):      
        random_entries = self.filter(voted = True).order_by('?') 
        return random_entries[:1]
    #def random_low(self):      
        #random_entries = self.filter(score <= 0).order_by('?') 
        #return random_entries[:1]
            
class Entry(models.Model):
    text = models.CharField(max_length=15)
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    voted = models.BooleanField(default=False)
    def __unicode__(self):
        return self.text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    objects = EntryManager()