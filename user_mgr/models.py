from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from user_mgr.model_field_choices import USER_STATUS, USER_GENDER


class FriendList(models.Model):
    owner   = models.OneToOneField('UserAccount')
    friends = models.ForeignKey(User)

    class Meta():
        verbose_name_plural  = 'FriendList'

class Address(models.Model):
    owner = models.ForeignKey('UserAccount')
    house_address = models.TextField()
    lga = models.CharField(max_length = 25)
    state = models.CharField(max_length = 25)
    country = models.CharField(max_length = 25)

    def __str__(self):
        return self.house_address

    class Meta():
        verbose_name_plural  = 'Address'

class UserAccount(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length = 15, null = True, blank = True)
    gender = models.CharField(max_length = 10, choices = USER_GENDER, null = True, blank = True)
    status = models.CharField(max_length = 10, choices = USER_STATUS, null = True, blank = True)

    def __str__(self):
        return self.user.username

    class Meta():
        verbose_name_plural  = 'UserAccount'
