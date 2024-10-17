from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from category import *

# Create your models here.

class Author(models.Model):
	authorUser = models.OneToOneField(User, on_delete=models.D0_NOTHING)

class Post(models.Model):
	author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
	title = models.CharField(max_length=64)
	text = RichTextField()
	datecreation = models.DateTimeField(auto_now_add=True)
	category = models.CharField(max_length=2, choices=CATEGORY_CHOICE, default=WIZARD,
								help_text='Выберите категорию')

	def __str__(self):
		return self.title

class Page(models.Model):
	authorpage = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
	text = models.TextField()
	status = models.BooleanField(default=False)
	dateCreation = models.DateTimeField(auto_now_add=True)

