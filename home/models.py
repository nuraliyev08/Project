from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator
from django.db.models import Count
from django.contrib.auth.models import AbstractUser

class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    rich_text = RichTextUploadingField()

    def __str__(self):
        return self.title

class Akar(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    rich_text = RichTextUploadingField()

    def __str__(self):
        return self.title

class Carousel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/Slider',
    validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

    def __str__(self):
        return self.title

class Phone(models.Model):
    title = models.CharField(max_length=255)
    number = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def count_product(self):
        count_product_one = Product.objects.filter(category=self).aggregate(count=Count('id'))
        cnt = 0
        if count_product_one["count"] is not None:
            cnt = int(count_product_one["count"])
        return cnt


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Search(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/Slider',
    validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

    def __str__(self):
        return self.title


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    def __str__(self):
        return self.user.username




