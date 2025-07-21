from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4 as u4
from django.core.validators import MinValueValidator,MaxValueValidator
class ContentGenre(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=u4,blank=False)
    name = models.CharField(max_length=70,blank=False)
    created = models.DateTimeField(auto_now_add=True,editable=False,blank=False)
    updated = models.DateField(auto_now=True,editable=False,blank=False)
class ParentalControlTags(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=u4,blank=False)
    name = models.CharField(max_length=70,blank=False)
    created = models.DateTimeField(auto_now_add=True,editable=False,blank=False)
    updated = models.DateField(auto_now=True,editable=False,blank=False)
class Artist(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=u4,blank=False)
    name = models.CharField(max_length=70,blank=False)
    about = models.CharField(max_length=350,blank=False)
    created = models.DateTimeField(auto_now_add=True,editable=False,blank=False)
    updated = models.DateField(auto_now=True,editable=False,blank=False)
class Content(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=u4,blank=False)
    name = models.CharField(max_length=70)
    about = models.CharField(max_length=350)
    parental_control_tags = models.ManyToManyField(ParentalControlTags,related_name='content')
    genre = models.ManyToManyField(ContentGenre,related_name='content')
    cast = models.ManyToManyField(Artist,related_name='content')
    rating = models.FloatField(default=0,editable=False,blank=False)
    created = models.DateTimeField(auto_now_add=True,editable=False,blank=False)
    updated = models.DateField(auto_now=True,editable=False,blank=False)
class ContentMediaFile(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=u4)
    name = models.CharField(max_length=70)
    name = models.FileField(upload_to="content")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
class ArtistContentRelation(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=u4)
    artist = models.ForeignKey(Artist,related_name='relations',on_delete=models.CASCADE)
    content = models.ForeignKey(Content,related_name='relations',on_delete=models.CASCADE)
    relation = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
class Reviews(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=u4)
    user = models.ForeignKey(User,related_name='reviews',on_delete=models.CASCADE)
    content = models.ForeignKey(Content,related_name='reviews',on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    review = models.CharField(max_length=350)
    rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
class SubscriptionModels(models.Model):
    id = models.UUIDField(primary_key=True,default=u4,editable=False)
    name = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
class SubscriptionMapping(models.Model):
    id = models.UUIDField(primary_key=True,default=u4,editable=False)
    user = models.ForeignKey(User,related_name='map',on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionModels,related_name='map',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)