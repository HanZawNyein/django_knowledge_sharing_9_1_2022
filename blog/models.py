from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# create-your-models-here
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('publish','Published')
    )
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("details", args=[self.publish.year,self.publish.month,self.publish.day,self.slug])
    
