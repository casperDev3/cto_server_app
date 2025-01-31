from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.TextField(default="https://loremflickr.com/1280/720")
    creator = models.TextField(default="John Doe")
    date_posted = models.DateTimeField(auto_now_add=True)
    reactions = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    comments_list = models.TextField(default="[]")
    category = models.TextField(default="Основні")
    tags = models.TextField(default="[]")


    def __str__(self):
        return {
            "title": self.title,
            "content": self.content,
            "photo": self.photo,
            "creator": self.creator,
            "date_posted": self.date_posted,
            "reactions": self.reactions,
            "comments": self.comments,
            "comments_list": self.comments_list,
            "tags": self.tags
        }
