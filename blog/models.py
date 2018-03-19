from django.db import models
from django.utils import timezone

class Post(models.Model):
    #Properties of the blog post model
    author = models.ForeignKey('auth.user', on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default = timezone.now
    )
    published_date = models.DateTimeField(
        blank = True,
        null = True
    )

    #Methods that are applicable when dealing with a blog post model

    #Method to record the dat of publishing the blog post & also save the content of the post
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #Method to return the title of the blog post
    def __str__(self):
        return self.title
