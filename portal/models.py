from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
	author = models.OneToOneField(User, on_delete=models.D0_NOTHING)

class Post(models.Model):
	title = models.CharField(max_length=64)
	text = models.TextField(help_text='Введите ваш текст здесь')
	datetime = models.DateTimeField(auto_now_add=True)

