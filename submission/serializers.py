from rest_framework.serializers import ModelSerializer
from .models import Hackathon, Submission
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}

class HackathonSerializer(ModelSerializer):
    class Meta:
        model = Hackathon
        exclude = ['created_by']

class SubmissionSerializer(ModelSerializer):
    class Meta:
        model = Submission
        exclude = ['created_by']