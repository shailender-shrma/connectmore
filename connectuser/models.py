from django.db import models

# Create your models here.


class CurrentUser(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    sent_mails = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    activity_time = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Pdf(models.Model):
    name = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='pdfs')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
