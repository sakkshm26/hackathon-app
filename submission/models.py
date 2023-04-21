from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

SUBMISSION_TYPE = [
    ("IMAGE", "IMAGE"),
    ("FILE", "FILE"),
    ("LINK", "LINK"),
]

class Hackathon(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=600)
    background_image_url = models.CharField()
    hackathon_image_url = models.CharField()
    submission_type = models.CharField(choices=SUBMISSION_TYPE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    reward_prize = models.IntegerField(validators=[MinValueValidator(1)])
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_hackathon_set')
    registered_users = models.ManyToManyField(User, related_name='registered_hackathon_set', blank=True)

class Submission(models.Model):
    name = models.CharField(max_length=30)
    summary = models.CharField(max_length=300)
    accepted = models.BooleanField(default=False)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)