from distutils.command import upload
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    about = models.TextField()
    headquarters = models.CharField(max_length=150)
    company_email = models.EmailField()
    twitter = models.URLField(max_length=1000, unique=True)
    linkedln = models.CharField(max_length=1000, unique=True)
    company_website = models.URLField(max_length=1000, unique=True)
    net_worth = models.CharField(max_length=100)
    area_served = models.CharField(max_length=25)
    founders = models.CharField(max_length=200)
    founded = models.DateField()
    revenue = models.CharField(max_length=150, blank=True)
    taxpayer_identification_number = models.IntegerField(blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)

class Feeback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()




