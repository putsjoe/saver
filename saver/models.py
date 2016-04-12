from django.db import models


class Url(models.Model):
    url_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=350)
    url_title = models.CharField(max_length=200)
    time_added = models.DateTimeField(auto_now_add=True) #, blank=True)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    salt = models.CharField(max_length=100)
    hashpass = models.CharField(max_length=100)

class Active(models.Model):
    active_id = models.AutoField(primary_key=True)
    url_id = models.ForeignKey(Url, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    time = models.DateTimeField(auto_now_add=True) #, blank=True)

class Session(models.Model):
    uid = models.ForeignKey(User, on_delete=models.PROTECT)
    sessid = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True) #, blank=True)



