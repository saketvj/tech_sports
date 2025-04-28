from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    title = models.CharField(max_length=20)
    posts =  models.ManyToManyField('Post',related_name="tags")


    def __str__(self):
        return self.title 
