from django.db import models

class Account(models.Model):
    userID = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    handle = models.CharField(max_length=200, null=True)
    profileImage = models.URLField(null=True, blank=True, max_length=200)
    
    def __str__(self):
        return self.handle

class Post(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    postID = models.AutoField(primary_key=True)
    date = models.DateTimeField('Date Posted', auto_now=True)
    description = models.TextField(blank=True, null=True)
    likes = models.IntegerField(default=0, null=True)
    comments = models.IntegerField(default=0, null=True)
    image = models.URLField(null=True, blank=True, max_length=200)
    profileImage = models.URLField(null=True, blank=True, max_length=200)
    
    def __str__(self):
        return self.description