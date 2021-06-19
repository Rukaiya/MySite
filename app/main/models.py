from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class ToDoList(models.Model):
    name = models.CharField(max_length=100)
    
    def get_absolute_url(self):
        return reverse("main:detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
    