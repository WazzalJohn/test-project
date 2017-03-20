from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username


class Entity(models.Model):
    entity_name = models.CharField(max_length=50)
    email = models.ForeignKey(User)

class Account(models.Model):
    account_name = models.CharField(max_length=20)
    entity_name = models.ForeignKey(Entity)

class UserSettings(models.Model):
    email = models.ForeignKey(User)
    last_account = models.ForeignKey(Account)
    last_share_view = models.CharField(max_length=5)
