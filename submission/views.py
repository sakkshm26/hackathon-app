from .serializers import HackathonSerializer, SubmissionSerializer, UserSerializer
from .models import Hackathon, Submission
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from submission.customauth import CustomAuthentication

### User ###

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#### Hackathon ####

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def create_hackathon(request):
    if request.method == 'POST':
        serializer = HackathonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def register_for_hackathon(request):
    if request.method == 'POST':
        hackathon = Hackathon.objects.get(pk=request.data['hackathon_id'])
        hackathon.registered_users.add(request.user)
        return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def get_hackathons(request):
    if request.method == 'GET':
        hackathons = Hackathon.objects.all()
        serializer = HackathonSerializer(hackathons, many=True)
        if serializer.is_valid():
          return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def get_enrolled_hackathons(request):
    if request.method == 'GET':
        enrolled_hackathons = Hackathon.objects.filter(registered_users=request.user)
        serializer = HackathonSerializer(enrolled_hackathons, many=True)
        if (serializer.is_valid()):
          return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#### Submission ####

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def create_submission(request):
    if request.method == 'POST':
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def get_user_submissions(request):
    if request.method == 'GET':
        user_submissions = Submission.objects.filter(created_by=request.user)
        serializer = SubmissionSerializer(user_submissions, many=True)
        if serializer.is_valid():
          return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)