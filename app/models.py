from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True

class Task(BaseModel):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='tasks')
    title=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return f'{self.title}'