from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False) # 여기가 True이든 False이든 상관 없이 serializer의 BooleanField의 default는 False...?
    
    def __str__(self):
        return f'Todo > title: {self.title}'    
    