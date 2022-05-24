from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Interest(models.Model):
    interest_text = models.CharField(max_length=200)
    
    
    def __str__(self):
        return (self.interest_text)


class Mentor(models.Model):
    mentor_text = models.CharField(max_length=200)
    
    def __str__(self):
        return (self.mentor_text)

class UserProfile(models.Model):
    first_name = models.TextField(default="")
    second_name = models.TextField(default="")
    email_address = models.TextField(max_length=50)
    
    #other models relationship

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #notification = models.ForeignKey(Notification)

    mentoring = models.TextField(default="No")
    mentor_subjects = models.ManyToManyField(Interest, related_name="mentor_subjects")

    description = models.TextField(max_length=500, default = "")
    user_interests = models.ManyToManyField(Interest, related_name="user_interests")
    year_group = models.TextField(default="")

class Notification(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='sender_notification')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient_notification')
    message = models.TextField()
    #notes = models.TextField(default = "", max_length = 500)
    #sent_date = models.DateTimeField(auto_now_add=True)     