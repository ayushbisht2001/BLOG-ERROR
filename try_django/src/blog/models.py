from django.db import models
from django.conf import settings
from datetime import *

User = settings.AUTH_USER_MODEL

#  NOTE :
"""
from django.contrib.auth import get_user_model        # This is used to access the  user and data associated with it
User = get_user_model()
j = User.objects.first()

print(j.blogpost_set.all())       # this is used to list out all the blogposts associated with j user

"""


class BlogPost(models.Model):  #blogoist_set ---> queryset
    # id = IntegerField()
    user = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)  # hello world --> hello-world
    content = models.TextField(null = True, blank=True)
    # publish_date = models.DateTimeField(default=datetime.now(), null=True, blank=True)
    # timestamp = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    # class Meta:
    #     ordering = ['-publish_date' , '-timestamp' , '-updated']
    def get_absolute_url(self):
        return f"/blog/{self.slug}/"
    def get_edit_url(self):
        return f"{self.get_absolute_url()}edit/"
    def get_delete_url(self):
        return f"{self.get_absolute_url()}delete/"