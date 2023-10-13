from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
'''
create post :-
title
author
content
image
publish_date
tags
'''

'''
model :
-fields
-html
-validation
'''
class post(models.Model):
    author= models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=500000)
    publish_date=models.DateTimeField(default=timezone.now)
    tags = TaggableManager()
    image=models.ImageField(upload_to='posts')


    def __str__(self):
        return self.title
