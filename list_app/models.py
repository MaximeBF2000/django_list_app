from django.db import models

# Create your models here.

class List(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name


class Todo(models.Model):
  name = models.CharField(max_length=255)
  list_key = models.ForeignKey(List, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name


  