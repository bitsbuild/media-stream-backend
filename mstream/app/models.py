from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4 as u4
from django.core.validators import MinValueValidator,MaxValueValidator
class ContentGenre(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=u4,blank=False,unique=True)
    name = models.CharField(max_length=70,blank=False,unique=True)
    created = models.DateTimeField(auto_now_add=True,editable=False,blank=False)
    updated = models.DateField(auto_now=True,editable=False,blank=False)
class ParentalControlTags(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=u4,blank=False,unique=True)
    name = models.CharField(max_length=70,blank=False,unique=True)
    created = models.DateTimeField(auto_now_add=True,editable=False,blank=False)
    updated = models.DateField(auto_now=True,editable=False,blank=False)
class Artist(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=u4,blank=False,unique=True)
    name = models.CharField(max_length=70,blank=False,unique=True)
    about = models.CharField(max_length=350,blank=False,unique=True)
    created = models.DateTimeField(auto_now_add=True,editable=False,blank=False)
    updated = models.DateField(auto_now=True,editable=False,blank=False)
class Content(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=u4,blank=False,unique=True)
    name = models.CharField(max_length=70,blank=False,unique=True)
    about = models.CharField(max_length=350,blank=False,unique=True)
    parental_control_tags = models.ManyToManyField(ParentalControlTags,related_name='content',blank=False)
    genre = models.ManyToManyField(ContentGenre,related_name='content',blank=False)
    cast = models.ManyToManyField(Artist,related_name='content',blank=False)
    rating = models.FloatField(default=0,editable=False,blank=False)
    created = models.DateTimeField(auto_now_add=True,editable=False,blank=False)
    updated = models.DateField(auto_now=True,editable=False,blank=False)
class ContentMediaFile(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=u4,blank=False)
    name = models.CharField(max_length=70,blank=False,unique=True)
    file = models.FileField(upload_to="content",blank=False)
    content = models.ForeignKey(Content,related_name='media',on_delete=models.CASCADE,blank=False)
    created = models.DateTimeField(auto_now_add=True,editable=False,blank=False)
    updated = models.DateTimeField(auto_now=True,editable=False,blank=False)
class ArtistContentRelation(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,blank=False,default=u4,unique=True)
    artist = models.ForeignKey(Artist,related_name='relations',on_delete=models.CASCADE,blank=False)
    content = models.ForeignKey(Content,related_name='relations',on_delete=models.CASCADE,blank=False)
    relation = models.CharField(max_length=70,blank=False)
    created = models.DateTimeField(auto_now_add=True,editable=False,blank=False)
    updated = models.DateTimeField(auto_now=True,editable=False,blank=False)
class Reviews(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,blank=False,default=u4,unique=True)
    user = models.ForeignKey(User,related_name='reviews',on_delete=models.CASCADE,blank=False)
    content = models.ForeignKey(Content,related_name='reviews',on_delete=models.CASCADE,blank=False)
    title = models.CharField(max_length=70,blank=False,unique=True)
    review = models.CharField(max_length=350,blank=False,unique=True)
    rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],blank=False)
    created = models.DateTimeField(auto_now_add=True,editable=False,blank=False)
    updated = models.DateTimeField(auto_now=True,editable=False,blank=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user','content'],name='one_review_per_content_per_user')
        ]
class SubscriptionModels(models.Model):
    id = models.UUIDField(primary_key=True,default=u4,editable=False,blank=False,unique=True)
    name = models.CharField(max_length=70,blank=False,unique=True)
    created = models.DateTimeField(auto_now_add=True,editable=False,blank=False)
    updated = models.DateTimeField(auto_now=True,editable=False,blank=False)
class SubscriptionMapping(models.Model):
    id = models.UUIDField(primary_key=True,default=u4,editable=False,blank=False,unique=True)
    user = models.ForeignKey(User,related_name='map',on_delete=models.CASCADE,blank=False,unique=True)
    plan = models.ForeignKey(SubscriptionModels,related_name='map',on_delete=models.CASCADE,blank=False)
    created = models.DateTimeField(auto_now_add=True,editable=False,blank=False)
    updated = models.DateTimeField(auto_now=True,editable=False,blank=False)