from django.db import models
import datetime
from django.utils import timezone
#* code below is for User model and forms excersizes
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    the_question = models.CharField(max_length=200)
    published = models.DateField('date of publication')
    #*code bellow is used to create plural names
    class Meta():
        verbose_name_plural = 'Questions(Pytania)'

    def was_published_recently(self):
        return self.published >= timezone.now() - datetime.timedelta(days=1)

    #*string method
    def __str__(self):
        return self.the_question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    the_choice = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.the_choice

#*Some data to use Faker
class User1s(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)

class User2s(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)


#* USER Model excersizes
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.user.username
