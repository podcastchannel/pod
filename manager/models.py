from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator

class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_listener = models.BooleanField(default=False)
    
class Manager(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.name.username

class Listener(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.name.username

class Program(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(default='default.jpg', upload_to='pics')
    one_off = models.BooleanField(default=False)
    slug = models.SlugField(max_length=500, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name} + {self.description[:2]}')
        super().save(*args,**kwargs)
    def __str__(self):
        return self.name 

class Podcast(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(default='default.jpg', upload_to='pics')
    audio = models.FileField(upload_to='audio_files/', validators=[FileExtensionValidator(allowed_extensions=['mp3', 'm4a','wav'])])
    one_off = models.BooleanField(default=False)
    slug = models.SlugField(max_length=500, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name} + {self.description[:2]}')
        super().save(*args,**kwargs)
    def __str__(self):
        return self.name 

class Blog(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    start_date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpg', upload_to='pics')
    likes = models.ManyToManyField(Listener, related_name='blog_likes', blank=True)
    dislikes = models.ManyToManyField(Listener, related_name='blog_dislikes', blank=True)
    share_link = models.CharField(max_length=3000, default='home.html')
    social_accounts = models.CharField(max_length=1000, blank=True)
    slug = models.SlugField(max_length=500, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name} + {self.description[:2]}')
        super().save(*args,**kwargs)
    def __str__(self):
        return self.name

class Competition(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(default='default.jpg', upload_to='pics')
    likes = models.ManyToManyField(Listener, related_name='com_likes', blank=True)
    dislikes = models.ManyToManyField(Listener, related_name='com_dislikes', blank=True)
    share_link = models.CharField(max_length=3000, default='home.html')
    social_accounts = models.CharField(max_length=1000, blank=True)
    slug = models.SlugField(max_length=500, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name} + {self.description[:2]}')
        super().save(*args,**kwargs)
    def __str__(self):
        return self.name
    
