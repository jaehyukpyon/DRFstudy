from django.db import models
from datetime import datetime

# Create your models here.


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()

    class Meta:
        ordering = ['created']


class Comment:
    def __init__(self, email, content=None, created=None, mytext=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()
        # self.mytext = mytext or 'Comment의 init메서드 안에서 생성된 mytext'
