from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  #Since we are using this model as a base class and not as a model to store data in the database

class Todo(BaseModel): #Inheriting from the BaseModel class
    todo_name = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_todos') #This is a one to many relationship. One user can have many todos

    class Meta:
        verbose_name_plural = 'Todos'

    def __str__(self):
        return f"{self.todo_name} - {self.user.username}"