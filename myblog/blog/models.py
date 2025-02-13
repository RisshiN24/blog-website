from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200) # A post needs a title
    content = models.TextField() # We need content of course
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Someone has to author the work
    created_at = models.DateTimeField(auto_now_add=True) # When was the post published?

    def __str__(self):
        return self.title

# Create your models here.
