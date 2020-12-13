from django.db import models

class BlogPost(models.Model):
    # id = IntegerField()
    title = models.TextField()
    slug = models.SlugField(unique=True)  # hello world --> hello-world
    content = models.TextField(null = True, blank=True)


