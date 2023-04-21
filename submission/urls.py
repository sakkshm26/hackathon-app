from django.urls import path
from .views import register_user, create_hackathon, register_for_hackathon, get_hackathons, get_enrolled_hackathons, create_submission, get_user_submissions

urlpatterns = [
    path('user/signup', register_user), 
    path('hackathon/create', create_hackathon), 
    path('hackathon/register', register_for_hackathon), 
    path('hackathon/list', get_hackathons), 
    path('hackathon/list-enrolled', get_enrolled_hackathons), 
    path('submission/create', create_submission), 
    path('submission/list-submissions', get_user_submissions), 
]