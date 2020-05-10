from django.db import models
from django.core.urlresolvers import reverse
class Company(models.Model):
    name=models.CharField(max_length=256)
    location=models.CharField(max_length=236)
    ceo=models.CharField(max_length=236)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
