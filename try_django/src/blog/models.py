from django.db import models
from django.conf import settings
from datetime import *
from django.utils import timezone
User = settings.AUTH_USER_MODEL

#  NOTE :
"""
from django.contrib.auth import get_user_model        # This is used to access the  user and data associated with it
User = get_user_model()
j = User.objects.first()

print(j.blogpost_set.all())       # this is used to list out all the blogposts associated with j user

"""

class BlogPostQuerySet(models.QuerySet):        # customized  inbuilt    get_queryset()  function
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()




class BlogPost(models.Model):  #blogoist_set ---> queryset
    # id = IntegerField()
    user = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    image = models.FileField(upload_to='image/', blank=True, null=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)  # hello world --> hello-world
    content = models.TextField(null = True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = BlogPostManager()
    class Meta:
        ordering = ['-pk' , '-publish_date', '-timestamp', '-updated']
    def get_absolute_url(self):
        return f"/blog/{self.slug}/"
    def get_edit_url(self):
        return f"{self.get_absolute_url()}edit/"
    def get_delete_url(self):
        return f"{self.get_absolute_url()}delete/"